# coding: utf-8
"""v2.5 conservative relative zero-shot NLI reranker.

The domain ontology is intentionally stable rather than trained every day.
SPECTER2 supplies semantic recall; v2.2 supplies concrete object evidence; this
stage asks a small local NLI model which broad scientific domain best describes
the paper. Promotions are deliberately conservative so an incidental mention of
"ISM" cannot rescue a cosmology/galaxy paper.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

import numpy as np
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


NLI_MODEL = "cross-encoder/nli-deberta-v3-xsmall"

POSITIVE_LABELS = [
    "interstellar atomic and molecular gas",
    "molecular clouds, dense cores, and star formation",
    "neutral hydrogen, cold neutral gas, and the atomic interstellar medium",
    "expanding H II regions, bubbles, shells, and stellar feedback acting on surrounding interstellar gas",
    "interstellar turbulence, magnetic fields, and astrochemistry",
    "Galactic gas and dust structure and interstellar-medium surveys",
]

NEGATIVE_LABELS = [
    "solar physics and the solar atmosphere",
    "individual stellar atmospheres, interiors, and stellar evolution",
    "planet formation, circumstellar disks, and planetary systems",
    "compact objects, relativistic transients, and high-energy plasma physics",
    "galaxy evolution, active galactic nuclei, and high-redshift galaxy populations",
    "the intergalactic medium, reionization, and cosmological 21-cm physics",
    "cosmology and large-scale structure",
    "nuclear and particle physics of dense matter",
    "generic telescope instrumentation, calibration, and data-processing methods",
    "generic plasma, shock, turbulence, and MHD theory without an interstellar-medium target",
]

ALL_LABELS = POSITIVE_LABELS + NEGATIVE_LABELS
N_POS = len(POSITIVE_LABELS)
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
    for idx, label in model.config.id2label.items():
        if "entail" in str(label).lower():
            return int(idx)
    return 1


def zero_shot_scores(
    model,
    tokenizer,
    premises: list[str],
    labels: list[str],
    batch_size: int = 16,
    max_length: int = 384,
) -> np.ndarray:
    hypotheses = [f"This paper is primarily about {label}." for label in labels]
    pairs: list[tuple[int, int, str, str]] = []
    for paper_i, premise in enumerate(premises):
        for label_i, hypothesis in enumerate(hypotheses):
            pairs.append((paper_i, label_i, premise, hypothesis))

    eidx = entailment_index(model)
    entail_logits = np.zeros((len(premises), len(labels)), dtype=float)
    with torch.no_grad():
        for start in range(0, len(pairs), batch_size):
            batch = pairs[start:start + batch_size]
            inputs = tokenizer(
                [x[2] for x in batch],
                [x[3] for x in batch],
                padding=True,
                truncation=True,
                max_length=max_length,
                return_tensors="pt",
            )
            logits = model(**inputs).logits[:, eidx].cpu().numpy()
            for item, value in zip(batch, logits):
                entail_logits[item[0], item[1]] = float(value)

    shifted = entail_logits - entail_logits.max(axis=1, keepdims=True)
    exp = np.exp(shifted)
    return exp / np.clip(exp.sum(axis=1, keepdims=True), 1e-12, None)


def should_run_nli(paper: dict) -> bool:
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


def zero_shot_decision(paper: dict, pos: float, neg: float) -> tuple[str, str]:
    old = paper["priority"]
    domain = float(paper.get("domain_evidence_score", 0.0))
    title_domain = float(paper.get("title_domain_score", 0.0))
    primary = paper.get("primary_category", "") or ""
    share = pos / max(pos + neg, 1e-12)

    # Abstract mentions can be incidental. Title-level evidence is strongest;
    # otherwise require a fairly dense set of direct object signals.
    strong_object = title_domain >= 3.0 or domain >= 8.0

    if old in {"A", "B"}:
        if share < 0.32 and not strong_object:
            return "SKIP", "zero-shot classifier strongly favors a non-ISM domain"
        if share < 0.48 and not strong_object:
            return one_level_down(old), "zero-shot classifier weakens ISM interpretation"
        if share < 0.60 and domain < 4.0 and title_domain == 0.0:
            return one_level_down(old), "weak relative ISM preference without direct object evidence"
        if old == "A" and share < 0.50 and domain < 6.0:
            return "B", "A capped because the broad-domain classification is ambiguous"
        return old, "zero-shot classification and object evidence are consistent"

    if old == "C":
        # C -> B needs both relative semantic confidence and concrete science
        # evidence. High-z/IGM papers should not be promoted by one shared term.
        if share >= 0.72 and (title_domain >= 3.0 or domain >= 6.0) and primary in {"astro-ph.GA", "astro-ph.SR", "astro-ph.HE"}:
            return "B", "zero-shot classifier promotes a strongly evidenced ISM candidate"
        if share < 0.28 and not strong_object:
            return "SKIP", "zero-shot classifier strongly favors a non-ISM domain"
        return "C", "zero-shot classifier leaves the paper as a boundary candidate"

    if old == "SKIP":
        # A previous SKIP is hard to overturn. Require title-level direct ISM/SF
        # evidence for B, or a very strong GA/SR object case for C.
        if share >= 0.78 and title_domain >= 3.0 and primary in {"astro-ph.GA", "astro-ph.SR", "astro-ph.HE"}:
            return "B", "zero-shot classifier rescues a title-confirmed ISM near-miss"
        if share >= 0.70 and (
            title_domain >= 3.0 or (primary in {"astro-ph.GA", "astro-ph.SR"} and domain >= 6.0)
        ):
            return "C", "zero-shot classifier rescues a conservative ISM near-miss"
    return old, "zero-shot classifier does not change the decision"


def combined_score(old_score: float, share: float) -> float:
    return float(np.clip(0.70 * float(old_score) + 0.30 * (100.0 * share), 0.0, 100.0))


def run(input_json: Path, output_dir: Path) -> None:
    payload = json.loads(input_json.read_text(encoding="utf-8"))
    papers = payload["papers"]
    selected_idx = [i for i, p in enumerate(papers) if should_run_nli(p)]
    print(f"[INFO] Zero-shot shortlist: {len(selected_idx)} / {len(papers)} papers")
    if not selected_idx:
        raise RuntimeError("Zero-shot shortlist is empty")

    model, tokenizer = load_nli()
    premises = [
        "Title: " + papers[i]["title"] + "\nAbstract: " + papers[i]["abstract"]
        for i in selected_idx
    ]
    scores = zero_shot_scores(model, tokenizer, premises, ALL_LABELS)

    evaluated = set(selected_idx)
    promoted = 0
    downgraded = 0
    for local_i, paper_i in enumerate(selected_idx):
        p = papers[paper_i]
        positive_scores = scores[local_i, :N_POS]
        negative_scores = scores[local_i, N_POS:]
        pos_i = int(np.argmax(positive_scores))
        neg_i = int(np.argmax(negative_scores))
        pos = float(positive_scores[pos_i])
        neg = float(negative_scores[neg_i])
        share = pos / max(pos + neg, 1e-12)

        old = p["priority"]
        new, reason = zero_shot_decision(p, pos, neg)
        promoted += int(PRIORITY_RANK[new] > PRIORITY_RANK[old])
        downgraded += int(PRIORITY_RANK[new] < PRIORITY_RANK[old])

        p["pre_nli_priority"] = old
        p["priority"] = new
        p["zero_shot_positive_label"] = POSITIVE_LABELS[pos_i]
        p["zero_shot_positive_score"] = round(pos, 4)
        p["zero_shot_negative_label"] = NEGATIVE_LABELS[neg_i]
        p["zero_shot_negative_score"] = round(neg, 4)
        p["zero_shot_ism_share"] = round(share, 4)
        p["nli_reason"] = reason
        p["score"] = round(combined_score(p.get("score", 50.0), share), 1)

    for i, p in enumerate(papers):
        if i not in evaluated:
            p["pre_nli_priority"] = p["priority"]
            p["zero_shot_positive_label"] = None
            p["zero_shot_positive_score"] = None
            p["zero_shot_negative_label"] = None
            p["zero_shot_negative_score"] = None
            p["zero_shot_ism_share"] = None
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
        "method": "v2.2 SPECTER2/domain gate + conservative relative zero-shot NLI broad-domain competition",
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.utcnow().strftime("%Y-%m-%d")
    json_path = output_dir / f"{stamp}-zero-shot-reranked.json"
    md_path = output_dir / f"{stamp}-zero-shot-reranked.md"
    json_path.write_text(json.dumps({"summary": summary, "papers": papers}, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# ISM Literature Recommender v2.5 — Conservative SPECTER2 + Zero-Shot NLI",
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
        if p["zero_shot_ism_share"] is None:
            zs = "not evaluated"
        else:
            zs = (
                f"ISM `{p['zero_shot_positive_label']}` {p['zero_shot_positive_score']:.3f} vs "
                f"non-ISM `{p['zero_shot_negative_label']}` {p['zero_shot_negative_score']:.3f}; "
                f"ISM share {p['zero_shot_ism_share']:.3f}"
            )
        lines.extend([
            f"### [{p['priority']}] {p['score']:.1f} — {p['title']}",
            f"- **arXiv:** [{p['id']}]({p['main_page']})",
            f"- **Primary:** {p.get('primary_category') or 'unknown'}",
            f"- **SPECTER2:** `{p.get('best_positive_topic')}` {p.get('best_positive_semantic')} vs `{p.get('best_negative_topic')}` {p.get('best_negative_semantic')} (margin {p.get('semantic_margin'):+.4f})",
            f"- **Domain evidence:** {p.get('domain_evidence_score')} — `{p.get('gate_reason')}`",
            f"- **Zero-shot:** {zs}",
            f"- **Decision:** {p['pre_nli_priority']} → {p['priority']} — {p['nli_reason']}",
            f"- **Abstract:** {p['abstract']}",
            "",
        ])

    downgraded_items = [p for p in papers if PRIORITY_RANK[p["priority"]] < PRIORITY_RANK[p["pre_nli_priority"]]]
    promoted_items = [p for p in papers if PRIORITY_RANK[p["priority"]] > PRIORITY_RANK[p["pre_nli_priority"]]]
    uncertain = [p for p in papers if p.get("zero_shot_ism_share") is not None and 0.43 <= float(p["zero_shot_ism_share"]) <= 0.57]

    lines.extend(["## Zero-shot downgraded", ""])
    if downgraded_items:
        for p in downgraded_items[:80]:
            lines.append(f"- **{p['pre_nli_priority']} → {p['priority']}** — {p['title']} — ISM share {p['zero_shot_ism_share']:.3f} — [{p['id']}]({p['main_page']})")
    else:
        lines.append("- None")

    lines.extend(["", "## Zero-shot promoted / rescued", ""])
    if promoted_items:
        for p in promoted_items[:80]:
            lines.append(f"- **{p['pre_nli_priority']} → {p['priority']}** — {p['title']} — ISM share {p['zero_shot_ism_share']:.3f} — [{p['id']}]({p['main_page']})")
    else:
        lines.append("- None")

    lines.extend(["", "## Zero-shot uncertain boundary cases", ""])
    if uncertain:
        for p in uncertain[:80]:
            lines.append(f"- **[{p['priority']}] {p['title']}** — ISM share {p['zero_shot_ism_share']:.3f}; domain {p.get('domain_evidence_score')} — [{p['id']}]({p['main_page']})")
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
    run(args.input_json or latest_domain_json(args.output_dir), args.output_dir)


if __name__ == "__main__":
    main()
