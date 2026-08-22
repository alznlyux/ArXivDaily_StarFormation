# coding: utf-8
"""Contrastive SPECTER2 ranking for the ISM literature recommender.

This v2.1 experiment compares the best positive ISM topic similarity against
explicit negative-topic similarities. It deliberately avoids per-topic min-max
normalization, which can force unrelated papers to the top of a daily ranking.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

import numpy as np

from v2_experiment import (
    bm25_topic_scores,
    current_keyword_baseline,
    embed_texts,
    fetch_recent_astro_ph,
    lexical_topic_scores,
    load_specter2,
    safe_cosine_scores,
)


def classify_priority(pos_sem: float, neg_sem: float, pos_lex: float, neg_lex: float) -> str:
    """Rule-based gate on raw semantic contrast plus specialist-term evidence.

    Thresholds are intentionally explicit and will be calibrated against human
    labels later. Raw cosine values are not interpreted as probabilities.
    """
    margin = pos_sem - neg_sem
    lex_margin = pos_lex - neg_lex

    if (margin >= 0.045 and pos_sem >= 0.70) or (
        margin >= 0.020 and pos_sem >= 0.69 and pos_lex >= 0.45 and lex_margin > 0
    ):
        return "A"
    if (margin >= 0.020 and pos_sem >= 0.68) or (
        margin >= 0.000 and pos_sem >= 0.67 and pos_lex >= 0.28 and lex_margin > 0
    ):
        return "B"
    if (margin >= 0.000 and pos_sem >= 0.66) or (
        margin >= -0.015 and pos_sem >= 0.66 and pos_lex >= 0.45 and lex_margin > 0.15
    ):
        return "C"
    return "SKIP"


def display_score(pos_sem: float, neg_sem: float, pos_lex: float, neg_lex: float) -> float:
    """Human-readable ranking score; not a probability."""
    margin = pos_sem - neg_sem
    lex_margin = pos_lex - neg_lex
    score = 50.0 + 450.0 * margin + 12.0 * lex_margin
    return float(np.clip(score, 0.0, 100.0))


def run(days: int, output_dir: Path, profile_path: Path) -> None:
    config = json.loads(profile_path.read_text(encoding="utf-8"))
    positive = config["topics"]
    negative = config["negative_topics"]

    papers = fetch_recent_astro_ph(days)
    if not papers:
        raise RuntimeError("No recent astro-ph papers were returned by arXiv.")

    model, tokenizer = load_specter2()

    # All anchor descriptions use the query adapter.
    model.set_active_adapters("adhoc_query")
    positive_names = list(positive.keys())
    negative_names = list(negative.keys())
    positive_queries = [positive[name]["description"] for name in positive_names]
    negative_queries = [negative[name]["description"] for name in negative_names]
    pos_query_embeddings = embed_texts(model, tokenizer, positive_queries, batch_size=8)
    neg_query_embeddings = embed_texts(model, tokenizer, negative_queries, batch_size=8)

    # Papers use the proximity adapter.
    model.set_active_adapters("proximity")
    paper_texts = [p["title"] + tokenizer.sep_token + p["abstract"] for p in papers]
    paper_embeddings = embed_texts(model, tokenizer, paper_texts, batch_size=16)

    pos_sem = safe_cosine_scores(pos_query_embeddings, paper_embeddings)
    neg_sem = safe_cosine_scores(neg_query_embeddings, paper_embeddings)
    pos_lex = lexical_topic_scores(papers, positive)
    neg_lex = lexical_topic_scores(papers, negative)
    pos_bm25 = bm25_topic_scores(papers, positive)

    results = []
    for i, paper in enumerate(papers):
        p_idx = int(np.argmax(pos_sem[i]))
        n_idx = int(np.argmax(neg_sem[i]))
        p_lex_idx = int(np.argmax(pos_lex[i]))

        best_pos_sem = float(pos_sem[i, p_idx])
        best_neg_sem = float(neg_sem[i, n_idx])
        best_pos_lex = float(np.max(pos_lex[i]))
        best_neg_lex = float(np.max(neg_lex[i]))
        semantic_margin = best_pos_sem - best_neg_sem

        top_pos_indices = np.argsort(pos_sem[i])[::-1][:3]
        top_positive = [
            {
                "topic": positive_names[int(j)],
                "semantic_raw": round(float(pos_sem[i, j]), 4),
                "lexical_score": round(float(pos_lex[i, j]), 4),
                "bm25_score": round(float(pos_bm25[i, j]), 4),
            }
            for j in top_pos_indices
        ]

        priority = classify_priority(best_pos_sem, best_neg_sem, best_pos_lex, best_neg_lex)
        score = display_score(best_pos_sem, best_neg_sem, best_pos_lex, best_neg_lex)

        results.append({
            **paper,
            "current_keyword_selected": current_keyword_baseline(paper),
            "contrastive_score": round(score, 1),
            "priority": priority,
            "best_positive_topic": positive_names[p_idx],
            "best_positive_semantic": round(best_pos_sem, 4),
            "best_negative_topic": negative_names[n_idx],
            "best_negative_semantic": round(best_neg_sem, 4),
            "semantic_margin": round(semantic_margin, 4),
            "positive_lexical": round(best_pos_lex, 4),
            "negative_lexical": round(best_neg_lex, 4),
            "lexical_margin": round(best_pos_lex - best_neg_lex, 4),
            "top_positive_topics": top_positive,
            "strongest_lexical_positive": positive_names[p_lex_idx],
        })

    results.sort(key=lambda x: (x["priority"] != "SKIP", x["contrastive_score"]), reverse=True)

    margins = np.asarray([r["semantic_margin"] for r in results], dtype=float)
    quantiles = {
        str(q): round(float(np.quantile(margins, q)), 4)
        for q in [0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95]
    }

    summary = {
        "generated_utc": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "lookback_days": days,
        "candidate_count": len(results),
        "current_keyword_selected": sum(r["current_keyword_selected"] for r in results),
        "priority_A": sum(r["priority"] == "A" for r in results),
        "priority_B": sum(r["priority"] == "B" for r in results),
        "priority_C": sum(r["priority"] == "C" for r in results),
        "priority_SKIP": sum(r["priority"] == "SKIP" for r in results),
        "semantic_margin_quantiles": quantiles,
        "method": "Raw SPECTER2 best-positive minus best-negative semantic margin, with specialist lexical evidence as a secondary gate. No per-topic min-max normalization.",
    }

    stamp = dt.datetime.utcnow().strftime("%Y-%m-%d")
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / f"{stamp}-contrastive.json"
    md_path = output_dir / f"{stamp}-contrastive.md"
    json_path.write_text(json.dumps({"summary": summary, "papers": results}, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = [
        "# ISM Literature Recommender v2.1 — Contrastive SPECTER2",
        "",
        f"Generated: {summary['generated_utc']}",
        f"Lookback: last {days} days",
        "",
        "## Summary",
        "",
        f"- All recent astro-ph candidates: **{summary['candidate_count']}**",
        f"- Current production keyword baseline selected: **{summary['current_keyword_selected']}**",
        f"- Contrastive Priority A: **{summary['priority_A']}**",
        f"- Contrastive Priority B: **{summary['priority_B']}**",
        f"- Contrastive Priority C: **{summary['priority_C']}**",
        f"- Contrastive SKIP: **{summary['priority_SKIP']}**",
        f"- Semantic-margin quantiles: `{summary['semantic_margin_quantiles']}`",
        "",
        "## Method",
        "",
        "For every paper, SPECTER2 computes similarity to both positive ISM/star-formation topic anchors and explicit negative anchors (solar physics, stellar atmospheres/evolution, planetary science, compact objects, galaxy evolution/AGN, cosmology, generic instrumentation).",
        "",
        "The primary signal is `best positive cosine - best negative cosine`. Exact specialist terms provide secondary evidence. Raw cosine values are retained; there is **no per-topic min-max normalization** and the display score is not a probability.",
        "",
        "## Highest-ranked A/B candidates",
        "",
    ]

    for paper in [r for r in results if r["priority"] in {"A", "B"}][:120]:
        pos_topics = ", ".join(
            f"{x['topic']} ({x['semantic_raw']:.4f})" for x in paper["top_positive_topics"]
        )
        lines.extend([
            f"### [{paper['priority']}] {paper['contrastive_score']:.1f} — {paper['title']}",
            f"- **arXiv:** [{paper['id']}]({paper['main_page']})",
            f"- **Primary category:** {paper['primary_category'] or 'unknown'}",
            f"- **Positive anchor:** {paper['best_positive_topic']} = {paper['best_positive_semantic']:.4f}",
            f"- **Negative anchor:** {paper['best_negative_topic']} = {paper['best_negative_semantic']:.4f}",
            f"- **Semantic margin:** {paper['semantic_margin']:+.4f}",
            f"- **Lexical positive/negative:** {paper['positive_lexical']:.4f} / {paper['negative_lexical']:.4f}",
            f"- **Top positive topics:** {pos_topics}",
            f"- **Current keyword baseline:** {'YES' if paper['current_keyword_selected'] else 'NO'}",
            f"- **Abstract:** {paper['abstract']}",
            "",
        ])

    old_false_positive_candidates = [
        r for r in results if r["current_keyword_selected"] and r["priority"] == "SKIP"
    ]
    semantic_recoveries = [
        r for r in results if (not r["current_keyword_selected"]) and r["priority"] in {"A", "B"}
    ]

    lines.extend(["## Disagreement: old keyword selected, contrastive SKIP", ""])
    lines.extend([
        f"- **{r['title']}** — margin {r['semantic_margin']:+.4f}, negative `{r['best_negative_topic']}` — [{r['id']}]({r['main_page']})"
        for r in old_false_positive_candidates[:80]
    ] or ["- None in this run."])

    lines.extend(["", "## Disagreement: contrastive A/B, old keyword missed", ""])
    lines.extend([
        f"- **[{r['priority']}] {r['contrastive_score']:.1f} — {r['title']}** — `{r['best_positive_topic']}` vs `{r['best_negative_topic']}`, margin {r['semantic_margin']:+.4f} — [{r['id']}]({r['main_page']})"
        for r in semantic_recoveries[:80]
    ] or ["- None in this run."])

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("[OK] Wrote", md_path)
    print("[OK] Wrote", json_path)
    print("[SUMMARY]", json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=10)
    parser.add_argument("--output-dir", default="v2_results")
    parser.add_argument("--profile", default="v2/topic_profiles.json")
    args = parser.parse_args()
    run(args.days, Path(args.output_dir), Path(args.profile))
