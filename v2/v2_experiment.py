# coding: utf-8
"""
Experimental ISM literature recommender.

This script deliberately does not modify the production daily pipeline.
It compares three views of the same recent astro-ph candidate set:

1. Current production keyword logic (GA/SR + include/exclude substring rules).
2. BM25 lexical retrieval against group research-topic queries.
3. SPECTER2 semantic retrieval, blended with a conservative lexical signal.

Outputs:
- v2_results/<date>-comparison.md
- v2_results/<date>-comparison.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlencode

import numpy as np
import requests
import torch
from adapters import AutoAdapterModel
from rank_bm25 import BM25Okapi
from transformers import AutoTokenizer


ARXIV_API = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"

# Exact production baseline, intentionally preserved for the comparison.
CURRENT_INCLUDE = [
    "star formation", "molecular cloud", "interstellar medium", "dust",
    "cloud", "clump", "core", "filament", "atomic gas", "H$_2$", "HI",
    "N-PDF", "bubble", "shell", "feedback", "jet", "outflow", "protostar",
]
CURRENT_EXCLUDE = [
    "galaxies", "galaxy clusters", "AGN", "black hole", "lensing",
    "dark matter", "dark energy", "fast radio burst", "pulsar",
    "neutron star", "white dwarf", "AGB", " z ", "lightcurve",
]


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def tokenize(text: str) -> List[str]:
    return re.findall(r"[a-z0-9]+(?:[-_][a-z0-9]+)*", text.lower())


def fetch_recent_astro_ph(days: int) -> List[dict]:
    """Fetch recent astro-ph papers through the official arXiv Atom API."""
    end = dt.datetime.utcnow()
    start = end - dt.timedelta(days=days)

    query = (
        "cat:astro-ph.* AND submittedDate:["
        + start.strftime("%Y%m%d%H%M")
        + " TO "
        + end.strftime("%Y%m%d%H%M")
        + "]"
    )

    params = {
        "search_query": query,
        "start": 0,
        "max_results": 2000,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    url = ARXIV_API + "?" + urlencode(params)
    print("[INFO] Fetching:", url)
    response = requests.get(url, timeout=120)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    papers = []

    for entry in root.findall(f"{ATOM}entry"):
        raw_id = normalize_text(entry.findtext(f"{ATOM}id", default=""))
        paper_id = raw_id.rsplit("/", 1)[-1]
        paper_id = re.sub(r"v\d+$", "", paper_id)

        title = normalize_text(entry.findtext(f"{ATOM}title", default=""))
        abstract = normalize_text(entry.findtext(f"{ATOM}summary", default=""))
        published = normalize_text(entry.findtext(f"{ATOM}published", default=""))

        authors = [
            normalize_text(author.findtext(f"{ATOM}name", default=""))
            for author in entry.findall(f"{ATOM}author")
        ]

        categories = [
            node.attrib.get("term", "")
            for node in entry.findall(f"{ATOM}category")
            if node.attrib.get("term", "")
        ]
        primary_node = entry.find(f"{ARXIV}primary_category")
        primary_category = (
            primary_node.attrib.get("term", "") if primary_node is not None else ""
        )

        if not any(cat.startswith("astro-ph.") for cat in categories):
            continue

        papers.append(
            {
                "id": paper_id,
                "title": title,
                "abstract": abstract,
                "authors": authors,
                "categories": categories,
                "primary_category": primary_category,
                "published": published,
                "main_page": f"https://arxiv.org/abs/{paper_id}",
                "pdf": f"https://arxiv.org/pdf/{paper_id}.pdf",
            }
        )

    dedup = {}
    for paper in papers:
        dedup[paper["id"]] = paper
    papers = list(dedup.values())

    print(f"[INFO] Retrieved {len(papers)} unique astro-ph papers.")
    return papers


def current_keyword_baseline(paper: dict) -> bool:
    """Reproduce the production include/exclude behavior exactly."""
    subjects = " ".join(paper.get("categories", []))
    if "astro-ph.GA" not in subjects and "astro-ph.SR" not in subjects:
        return False

    title = paper["title"].lower()
    abstract = paper["abstract"].lower()

    include = any(keyword.lower() in abstract for keyword in CURRENT_INCLUDE)
    include = include or any(keyword.lower() in title for keyword in CURRENT_INCLUDE)

    if any(keyword.lower() in abstract for keyword in CURRENT_EXCLUDE):
        include = False
    if any(keyword.lower() in title for keyword in CURRENT_EXCLUDE):
        include = False

    return include


def safe_cosine_scores(query_embeddings: np.ndarray, paper_embeddings: np.ndarray) -> np.ndarray:
    query_norm = query_embeddings / np.clip(
        np.linalg.norm(query_embeddings, axis=1, keepdims=True), 1e-12, None
    )
    paper_norm = paper_embeddings / np.clip(
        np.linalg.norm(paper_embeddings, axis=1, keepdims=True), 1e-12, None
    )
    return paper_norm @ query_norm.T


def embed_texts(model, tokenizer, texts: List[str], batch_size: int = 16) -> np.ndarray:
    """CLS embeddings following the official SPECTER2 example."""
    vectors = []
    model.eval()

    with torch.no_grad():
        for start in range(0, len(texts), batch_size):
            batch = texts[start:start + batch_size]
            inputs = tokenizer(
                batch,
                padding=True,
                truncation=True,
                max_length=512,
                return_tensors="pt",
                return_token_type_ids=False,
            )
            outputs = model(**inputs)
            vectors.append(outputs.last_hidden_state[:, 0, :].cpu().numpy())

    return np.concatenate(vectors, axis=0)


def load_specter2():
    print("[INFO] Loading SPECTER2 base + query/proximity adapters.")
    tokenizer = AutoTokenizer.from_pretrained("allenai/specter2_base")
    model = AutoAdapterModel.from_pretrained("allenai/specter2_base")

    model.load_adapter(
        "allenai/specter2_adhoc_query",
        source="hf",
        load_as="adhoc_query",
        set_active=True,
    )
    model.load_adapter(
        "allenai/specter2",
        source="hf",
        load_as="proximity",
        set_active=False,
    )
    return model, tokenizer


def bm25_topic_scores(papers: List[dict], topics: Dict[str, dict]) -> np.ndarray:
    corpus = [tokenize(p["title"] + " " + p["abstract"]) for p in papers]
    bm25 = BM25Okapi(corpus)
    all_scores = []

    for topic in topics.values():
        query = tokenize(topic["description"] + " " + " ".join(topic.get("lexical_terms", [])))
        score = bm25.get_scores(query).astype(float)
        max_score = float(score.max()) if len(score) else 0.0
        if max_score > 0:
            score /= max_score
        all_scores.append(score)

    return np.stack(all_scores, axis=1)


def lexical_topic_scores(papers: List[dict], topics: Dict[str, dict]) -> np.ndarray:
    rows = []
    for paper in papers:
        text = (paper["title"] + " " + paper["abstract"]).lower()
        topic_scores = []
        for topic in topics.values():
            hits = 0.0
            for term in topic.get("lexical_terms", []):
                if re.search(r"(?<!\w)" + re.escape(term.lower()) + r"(?!\w)", text):
                    hits += 1.0
            topic_scores.append(1.0 - math.exp(-hits / 3.0))
        rows.append(topic_scores)
    return np.asarray(rows, dtype=float)


def semantic_topic_scores(papers: List[dict], topics: Dict[str, dict]) -> np.ndarray:
    model, tokenizer = load_specter2()

    model.set_active_adapters("adhoc_query")
    query_texts = [topic["description"] for topic in topics.values()]
    query_embeddings = embed_texts(model, tokenizer, query_texts, batch_size=8)

    model.set_active_adapters("proximity")
    paper_texts = [p["title"] + tokenizer.sep_token + p["abstract"] for p in papers]
    paper_embeddings = embed_texts(model, tokenizer, paper_texts, batch_size=16)

    return safe_cosine_scores(query_embeddings, paper_embeddings)


def minmax_per_topic(scores: np.ndarray) -> np.ndarray:
    lo = scores.min(axis=0, keepdims=True)
    hi = scores.max(axis=0, keepdims=True)
    return (scores - lo) / np.clip(hi - lo, 1e-12, None)


def priority_from_score(score: float) -> str:
    if score >= 75:
        return "A"
    if score >= 60:
        return "B"
    if score >= 45:
        return "C"
    return "SKIP"


def make_report(papers, topics, semantic_raw, bm25_scores, lexical_scores, output_dir, days):
    topic_names = list(topics.keys())
    semantic = minmax_per_topic(semantic_raw)
    hybrid = 0.80 * semantic + 0.20 * lexical_scores
    hybrid_max = hybrid.max(axis=1)
    hybrid_topic_idx = np.argsort(hybrid, axis=1)[:, ::-1]
    bm25_max = bm25_scores.max(axis=1)

    results = []
    for i, paper in enumerate(papers):
        ranked_topics = []
        for idx in hybrid_topic_idx[i, :3]:
            ranked_topics.append({
                "topic": topic_names[int(idx)],
                "hybrid_topic_score": round(float(hybrid[i, idx] * 100), 1),
                "semantic_raw": round(float(semantic_raw[i, idx]), 4),
                "bm25_score": round(float(bm25_scores[i, idx]), 4),
                "lexical_score": round(float(lexical_scores[i, idx]), 4),
            })
        final_score = float(hybrid_max[i] * 100)
        results.append({
            **paper,
            "current_keyword_selected": current_keyword_baseline(paper),
            "bm25_score": round(float(bm25_max[i] * 100), 1),
            "semantic_score": round(float(semantic[i].max() * 100), 1),
            "hybrid_score": round(final_score, 1),
            "priority": priority_from_score(final_score),
            "top_topics": ranked_topics,
        })

    results.sort(key=lambda x: x["hybrid_score"], reverse=True)
    stamp = dt.datetime.utcnow().strftime("%Y-%m-%d")
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / f"{stamp}-comparison.json"
    md_path = output_dir / f"{stamp}-comparison.md"

    summary = {
        "generated_utc": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "lookback_days": days,
        "candidate_count": len(results),
        "current_keyword_selected": sum(p["current_keyword_selected"] for p in results),
        "priority_A": sum(p["priority"] == "A" for p in results),
        "priority_B": sum(p["priority"] == "B" for p in results),
        "priority_C": sum(p["priority"] == "C" for p in results),
        "topics": topic_names,
        "method": {
            "current": "Exact production GA/SR + include/exclude substring baseline.",
            "bm25": "Topic-query lexical retrieval, normalized independently per topic.",
            "hybrid": "80% normalized SPECTER2 semantic score + 20% exact specialist-term score.",
        },
    }
    json_path.write_text(json.dumps({"summary": summary, "papers": results}, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = [
        "# ISM Literature Recommender v2 — Experiment", "",
        f"Generated: {summary['generated_utc']}",
        f"Lookback: last {days} days", "",
        "## Candidate summary", "",
        f"- All recent astro-ph candidates: **{summary['candidate_count']}**",
        f"- Current production keyword baseline selected: **{summary['current_keyword_selected']}**",
        f"- Hybrid Priority A: **{summary['priority_A']}**",
        f"- Hybrid Priority B: **{summary['priority_B']}**",
        f"- Hybrid Priority C: **{summary['priority_C']}**", "",
        "## Scoring design", "",
        "- **Current baseline**: exact reproduction of the production `GA/SR + keyword include/exclude` logic.",
        "- **BM25**: independent lexical ranking against each group-topic description.",
        "- **Hybrid**: 80% SPECTER2 semantic similarity + 20% exact specialist-term signal.",
        "- Topic scores are relative ranking scores within this experiment, not calibrated probabilities.", "",
        "## Group topics", "",
    ]
    for name, topic in topics.items():
        lines.append(f"- **{name}** — {topic['description']}")

    lines.extend(["", "## Highest-ranked hybrid candidates", ""])
    for paper in results:
        if paper["priority"] == "SKIP":
            continue
        topics_text = ", ".join(f"{x['topic']} ({x['hybrid_topic_score']:.1f})" for x in paper["top_topics"])
        baseline = "YES" if paper["current_keyword_selected"] else "NO"
        lines.extend([
            f"### [{paper['priority']}] {paper['hybrid_score']:.1f} — {paper['title']}",
            f"- **arXiv:** [{paper['id']}]({paper['main_page']})",
            f"- **Primary category:** {paper['primary_category'] or 'unknown'}",
            f"- **Categories:** {', '.join(paper['categories'])}",
            f"- **Top topics:** {topics_text}",
            f"- **Current keyword baseline:** {baseline}",
            f"- **BM25 max:** {paper['bm25_score']:.1f}",
            f"- **Semantic max:** {paper['semantic_score']:.1f}",
            f"- **Abstract:** {paper['abstract']}", "",
        ])

    current_only = [p for p in results if p["current_keyword_selected"] and p["priority"] == "SKIP"]
    hybrid_new = [p for p in results if not p["current_keyword_selected"] and p["priority"] in {"A", "B"}]

    lines.extend(["## Disagreement set: current keyword selected, hybrid skipped", ""])
    lines.extend([f"- **{p['title']}** — hybrid {p['hybrid_score']:.1f} — [{p['id']}]({p['main_page']})" for p in current_only[:50]] or ["- None in this run."])
    lines.extend(["", "## Disagreement set: hybrid A/B, current keyword missed", ""])
    lines.extend([f"- **[{p['priority']}] {p['hybrid_score']:.1f} — {p['title']}** [{p['id']}]({p['main_page']})" for p in hybrid_new[:100]] or ["- None in this run."])
    lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print("[INFO] Wrote:", md_path)
    print("[INFO] Wrote:", json_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=10)
    parser.add_argument("--topics", default="v2/topic_profiles.json")
    parser.add_argument("--output-dir", default="v2_results")
    args = parser.parse_args()
    if args.days < 1 or args.days > 30:
        raise ValueError("--days must be between 1 and 30")

    topics = json.loads(Path(args.topics).read_text(encoding="utf-8"))["topics"]
    papers = fetch_recent_astro_ph(args.days)
    if not papers:
        raise RuntimeError("No astro-ph papers returned by arXiv API.")

    bm25_scores = bm25_topic_scores(papers, topics)
    lexical_scores = lexical_topic_scores(papers, topics)
    semantic_raw = semantic_topic_scores(papers, topics)
    make_report(papers, topics, semantic_raw, bm25_scores, lexical_scores, Path(args.output_dir), args.days)


if __name__ == "__main__":
    main()
