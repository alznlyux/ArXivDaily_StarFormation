# coding: utf-8
"""v2.3 free NLI reranker for the ISM literature recommender.

Architecture:
1. v2.2 SPECTER2 + domain gate provides a high-recall candidate pool.
2. A small local NLI model reads title + abstract only for the ambiguous pool.
3. NLI asks whether the *primary scientific focus* is ISM / star formation,
   versus another domain that merely shares words such as turbulence/shock/MHD.

No external inference API is used. The model runs on the GitHub Actions CPU
runner and is cached with the other Hugging Face models.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Iterable

import numpy as np
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


NLI_MODEL = "cross-encoder/nli-deberta-v3-xsmall"

# These hypotheses intentionally define the science at a high level rather
# than enumerating every possible ISM keyword. This lets e.g. OB-star feedback
# on atomic H I gas count as relevant without requiring "molecular cloud".
POSITIVE_HYPOTHESES = [
    "The primary scientific focus of this paper is the interstellar medium or star-forming interstellar matter.",
    "The paper primarily studies atomic or molecular interstellar gas, dust, clouds, H II regions, or the physical state and structure of the interstellar medium.",
    "The paper primarily studies star formation, or physical processes such as feedback, shocks, turbulence, magnetic fields, chemistry, cosmic rays, or radiation specifically as they act on interstellar gas or star-forming environments.",
]

NEGATIVE_HYPOTHESES = [
    "The primary scientific focus of this paper is another domain such as solar, stellar, planetary, compact-object, relativistic-plasma, galaxy-evolution, cosmological, or nuclear physics rather than the interstellar medium or star formation.",
    "The paper is primarily about generic instrumentation, generic numerical methods, or plasma and MHD theory without a direct interstellar-medium or star-formation science objective.",
]

PRIORITY_RANK = {"SKIP": 0, "C": 1, "B": 2, "A": 3}
RANK_PRIORITY = {0: "SKIP", 1: "C", 2: "B", 3: "A"}


def latest_domain_json(output_dir: Path) -> Path:
    files = sorted(output_dir.glob("*-domain-gated.json"))
    if not files:
        raise FileNotFoundError("No *-domain-gated.json found. Run v2_domain_gated.py first.")
    return files[-1]


def load_nli():
    print(f"[INFO] Loading NLI model: {NLI_MODEL}")
    tokenizer = AutoTokenizer.from_pretrained(NLI_MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(NLI_MODEL)
    model.eval()
    return model, tokenizer


def entailment_index(model) -> int:
    # The model card documents [contradiction, entailment, neutral]. We still
    # inspect config labels first so this remains robust to explicit label names.
    for idx, label in model.config.id2label.items():
        if "entail" in str(label).lower():
            return int(idx)
    return 1


def entailment_scores(
    model,
    tokenizer,
    premises: list[str],
    hypotheses: list[str],
    batch_size: int = 16,
    max_length: int = 384,
) -> np.ndarray:
    """Return shape (n_premises, n_hypotheses) of entailment probabilities."""
    pairs: list[tuple[int, str, str]] = []
    for i, premise in enumerate(premises):
        for hypothesis in hypotheses:
            pairs.append((i, premise, hypothesis))

    eidx = entailment_index(model)
    values = np.zeros((len(premises), len(hypotheses)), dtype=float)

    with torch.no_grad():
        for start in range(0, len(pairs), batch_size):
            batch = pairs[start:start + batch_size]
            a = [x[1] for x in batch]
            b = [x[2] for x in batch]
            inputs = tokenizer(
                a,
                b,
                padding=True,
                truncation=True,
                max_length=max_length,
                return_tensors="pt",
            )
            logits = model(**inputs).logits
            probs = torch.softmax(logits, dim=-1)[:, eidx].cpu().numpy()
            for local_i, prob in enumerate(probs):
                global_i = start + local_i
                paper_i = pairs[global_i][0]
                hyp_i = global_i % len(hypotheses)
                values[paper_i, hyp_i] = float(prob)
    return values


def should_run_nli(paper: dict) -> bool:
    """NLI is for plausible or ambiguous candidates, not the entire astro-ph feed."""
    if paper.get("priority") != "SKIP":
        return True
    if paper.get("base_contrastive_priority") in {"A", "B"}:
        return True
    if float(paper.get("domain_evidence_score", 0.0)) >= 4.0:
        return True
    if float(paper.get("title_domain_score", 0.0)) >= 3.0:
        return True
    return False


def one_level_down(priority: str) -> str:
    return RANK_PRIORITY[max(0, PRIORITY_RANK[priority] - 1)]


def nli_decision(paper: dict, pos: float, neg: float) -> tuple[str, str]:
    """Conservative NLI adjustment of the v2.2 result.

    Strong direct ISM-object evidence is deliberately allowed to protect a paper
    from a generic NLI false negative. Promotions from SKIP are capped at B.
    """
    old = paper["priority"]
    domain = float(paper.get("domain_evidence_score", 0.0))
    title_domain = float(paper.get("title_domain_score", 0.0))
    margin = pos - neg
    strong_object = domain >= 6.0 or title_domain >= 3.0

    if old in {"A", "B"}:
        # Clear negative-domain verdict and weak object evidence: remove.
        if neg >= 0.72 and margin <= -0.18 and not strong_object:
            return "SKIP", "NLI strongly favors non-ISM domain"
        # Moderate disagreement: downgrade rather than hard-delete.
        if (neg >= 0.62 and margin <= -0.08) or (pos < 0.30 and not strong_object):
            return one_level_down(old), "NLI weakens ISM interpretation"
        # If both readings are plausible, retain but cap weakly evidenced A items.
        if old == "A" and margin < 0.02 and domain < 4.0:
            return "B", "NLI ambiguous; A capped at B"
        return old, "NLI consistent or protected by direct object evidence"

    if old == "C":
        if pos >= 0.70 and margin >= 0.12 and domain >= 2.0:
            return "B", "NLI promotes strong ISM interpretation"
        if neg >= 0.75 and margin <= -0.20 and not strong_object:
            return "SKIP", "NLI strongly favors non-ISM domain"
        return "C", "NLI leaves borderline candidate in C"

    # Near-miss rescue. We require both strong NLI evidence and some concrete
    # object evidence; a semantic model alone cannot resurrect a paper.
    if old == "SKIP":
        if pos >= 0.78 and margin >= 0.18 and domain >= 3.0:
            return "B", "NLI rescues high-confidence ISM near-miss"
        if pos >= 0.68 and margin >= 0.10 and domain >= 4.0:
            return "C", "NLI rescues plausible ISM near-miss"
    return old, "NLI does not change decision"


def final_score(old_score: float, pos: float, neg: float) -> float:
    # Human-readable ranking only; not a probability.
    nli_component = 50.0 + 50.0 * (pos - neg)
    return float(np.clip(0.70 * float(old_score) + 0.30 * nli_component, 0.0, 100.0))


def run(input_json: Path, output_dir: Path) -> None:
    payload = json.loads(input_json.read_text(encoding="utf-8"))
    papers = payload["papers"]
    selected_idx = [i for i, p in enumerate(papers) if should_run_nli(p)]
    print(f"[INFO] NLI shortlist: {len(selected_idx)} / {len(papers)} papers")

    if not selected_idx:
        raise RuntimeError("NLI shortlist is empty")

    model, tokenizer = load_nli()
    premises = [
        "Title: " + papers[i]["title"] + "\nAbstract: " + papers[i]["abstract"]
        for i in selected_idx
    ]
    pos_matrix = entailment_scores(model, tokenizer, premises, POSITIVE_HYPOTHESES)
    neg_matrix = entailment_scores(model, tokenizer, premises, NEGATIVE_HYPOTHESES)

    evaluated = set(selected_idx)
    promoted = 0
    downgraded = 0

    for local_i, paper_i in enumerate(selected_idx):
        p = papers[paper_i]
        pos = float(np.max(pos_matrix[local_i]))
        neg = float(np.max(neg_matrix[local_i]))
        pos_h = int(np.argmax(pos_matrix[local_i]))
        neg_h = int(np.argmax(neg_matrix[local_i]))
        old = p["priority"]
        new, reason = nli_decision(p, pos, neg)
        if PRIORITY_RANK[new] > PRIORITY_RANK[old]:
            promoted += 1
        elif PRIORITY_RANK[new] < PRIORITY_RANK[old]:
            downgraded += 1

        p["pre_nli_priority"] = old
        p["priority"] = new
        p["nli_positive"] = round(pos, 4)
        p["nli_negative"] = round(neg, 4)
        p["nli_margin"] = round(pos - neg, 4)
        p["nli_positive_hypothesis"] = POSITIVE_HYPOTHESES[pos_h]
        p["nli_negative_hypothesis"] = NEGATIVE_HYPOTHESES[neg_h]
        p["nli_reason"] = reason
        p["score"] = round(final_score(p.get("score", 50.0), pos, neg), 1)

    for i, p in enumerate(papers):
        if i not in evaluated:
            p["pre_nli_priority"] = p["priority"]
            p["nli_positive"] = None
            p["nli_negative"] = None
            p["nli_margin"] = None
            p["nli_reason"] = "not evaluated: safely outside semantic/domain shortlist"

    papers.sort(key=lambda p: (PRIORITY_RANK[p["priority"]], float(p.get("score", 0.0))), reverse=True)

    summary = {
        "generated_utc": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "source": input_json.name,
        "candidate_count": len(papers),
        "nli_evaluated": len(selected_idx),
        "A": sum(p["priority"] == "A" for p in papers),
        "B": sum(p["priority"] == "B" for p in papers),
        "C": sum(p["priority"] == "C" for p in papers),
        "SKIP": sum(p["priority"] == "SKIP" for p in papers),
        "promoted_by_nli": promoted,
        "downgraded_by_nli": downgraded,
        "nli_model": NLI_MODEL,
        "method": "v2.2 SPECTER2/domain gate followed by local zero-shot NLI on the ambiguous shortlist only",
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.utcnow().strftime("%Y-%m-%d")
    json_path = output_dir / f"{stamp}-nli-reranked.json"
    md_path = output_dir / f"{stamp}-nli-reranked.md"
    json_path.write_text(json.dumps({"summary": summary, "papers": papers}, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# ISM Literature Recommender v2.3 — SPECTER2 + NLI",
        "",
        f"Generated: {summary['generated_utc']}",
        f"Source: `{summary['source']}`",
        "",
        "## Summary",
        "",
        f"- Candidates: **{summary['candidate_count']}**",
        f"- NLI evaluated: **{summary['nli_evaluated']}**",
        f"- A: **{summary['A']}**",
        f"- B: **{summary['B']}**",
        f"- C: **{summary['C']}**",
        f"- SKIP: **{summary['SKIP']}**",
        f"- Promoted by NLI: **{summary['promoted_by_nli']}**",
        f"- Downgraded by NLI: **{summary['downgraded_by_nli']}**",
        f"- NLI model: `{NLI_MODEL}`",
        "",
        "## A/B candidates",
        "",
    ]

    for p in [x for x in papers if x["priority"] in {"A", "B"}]:
        nli_text = "not evaluated" if p["nli_positive"] is None else (
            f"pos {p['nli_positive']:.3f} / neg {p['nli_negative']:.3f} / margin {p['nli_margin']:+.3f}"
        )
        lines.extend([
            f"### [{p['priority']}] {p['score']:.1f} — {p['title']}",
            f"- **arXiv:** [{p['id']}]({p['main_page']})",
            f"- **Primary:** {p.get('primary_category') or 'unknown'}",
            f"- **SPECTER2:** `{p.get('best_positive_topic')}` {p.get('best_positive_semantic')} vs `{p.get('best_negative_topic')}` {p.get('best_negative_semantic')} (margin {p.get('semantic_margin'):+.4f})",
            f"- **Domain evidence:** {p.get('domain_evidence_score')} — `{p.get('gate_reason')}`",
            f"- **NLI:** {nli_text}",
            f"- **Decision:** {p['pre_nli_priority']} → {p['priority']} — {p['nli_reason']}",
            f"- **Abstract:** {p['abstract']}",
            "",
        ])

    downgraded_items = [
        p for p in papers
        if PRIORITY_RANK[p["priority"]] < PRIORITY_RANK[p["pre_nli_priority"]]
    ]
    promoted_items = [
        p for p in papers
        if PRIORITY_RANK[p["priority"]] > PRIORITY_RANK[p["pre_nli_priority"]]
    ]
    uncertain = [
        p for p in papers
        if p.get("nli_margin") is not None and abs(float(p["nli_margin"])) < 0.08
    ]

    lines.extend(["## NLI downgraded", ""])
    if downgraded_items:
        for p in downgraded_items[:80]:
            lines.append(
                f"- **{p['pre_nli_priority']} → {p['priority']}** — {p['title']} — "
                f"NLI {p['nli_positive']:.3f}/{p['nli_negative']:.3f} — [{p['id']}]({p['main_page']})"
            )
    else:
        lines.append("- None")

    lines.extend(["", "## NLI promoted / rescued", ""])
    if promoted_items:
        for p in promoted_items[:80]:
            lines.append(
                f"- **{p['pre_nli_priority']} → {p['priority']}** — {p['title']} — "
                f"NLI {p['nli_positive']:.3f}/{p['nli_negative']:.3f} — [{p['id']}]({p['main_page']})"
            )
    else:
        lines.append("- None")

    lines.extend(["", "## NLI uncertain boundary cases", ""])
    if uncertain:
        for p in uncertain[:80]:
            lines.append(
                f"- **[{p['priority']}] {p['title']}** — margin {p['nli_margin']:+.3f}, "
                f"domain {p.get('domain_evidence_score')} — [{p['id']}]({p['main_page']})"
            )
    else:
        lines.append("- None")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("[OK] Wrote", md_path)
    print("[OK] Wrote", json_path)
    print(json.dumps(summary, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-json", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=Path("v2_results"))
    args = parser.parse_args()
    source = args.input_json or latest_domain_json(args.output_dir)
    run(source, args.output_dir)


if __name__ == "__main__":
    main()
