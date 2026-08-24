# coding: utf-8
"""v2.2 domain-gated ISM literature recommender.

Adds research-object evidence and arXiv primary-category gating on top of the
v2.1 contrastive SPECTER2 score. The goal is to distinguish papers that share
physics words (turbulence, shocks, magnetic fields) from papers actually about
ISM / molecular-cloud / star-formation science.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path

import numpy as np

from v2_experiment import (
    current_keyword_baseline,
    embed_texts,
    fetch_recent_astro_ph,
    lexical_topic_scores,
    load_specter2,
    safe_cosine_scores,
)
from v2_contrastive import classify_priority, display_score


# High-precision domain evidence. Broad physics words such as turbulence,
# magnetic field, shock, feedback, jet, and outflow are deliberately omitted.
DOMAIN_PATTERNS = [
    (r"\binterstellar medium\b", 2.5),
    (r"\bISM\b", 2.0),
    (r"\bmolecular clouds?\b", 3.0),
    (r"\bmolecular gas\b", 2.5),
    (r"\bgiant molecular clouds?\b", 3.0),
    (r"\bneutral hydrogen\b", 3.0),
    (r"\bH\s*I\s*(?:21\s*-?\s*cm|emission|absorption|cloud|gas)\b", 3.0),
    (r"\bHISA\b", 3.0),
    (r"\bHINSA\b", 3.0),
    (r"\bcold neutral (?:medium|gas)\b", 3.0),
    (r"\batomic[- ]to[- ]molecular\b", 3.0),
    (r"\bstar[- ]forming regions?\b", 2.5),
    (r"\bstar formation\b", 1.5),
    (r"\bprotostars?\b", 2.0),
    (r"\bprotostellar\b", 2.0),
    (r"\bprestellar\b", 2.0),
    (r"\byoung stellar objects?\b", 2.0),
    (r"\bYSOs?\b", 2.0),
    (r"\binfrared dark clouds?\b", 3.0),
    (r"\bIRDCs?\b", 3.0),
    (r"\bH\s*II regions?\b", 2.5),
    (r"\bHII regions?\b", 2.5),
    (r"\bsuperbubbles?\b", 2.0),
    (r"\bdense cores?\b", 2.0),
    (r"\bdense clumps?\b", 2.0),
    (r"\bfilamentary molecular\b", 2.0),
    (r"\b13CO\b", 1.5),
    (r"\bC18O\b", 1.5),
    (r"\bNH3\b", 1.0),
    (r"\bHCO\+\b", 1.0),
    (r"\bcosmic[- ]ray ionization\b", 2.0),
    (r"\b3D dust\b", 1.5),
    (r"\bGalactic plane\b", 1.0),
    (r"\bmolecular[- ]line (?:survey|observations?|emission)\b", 2.0),
]

DIRECT_TITLE_PATTERNS = [
    r"\bmolecular clouds?\b",
    r"\bmolecular gas\b",
    r"\binterstellar\b",
    r"\bHISA\b",
    r"\bHINSA\b",
    r"\bneutral gas\b",
    r"\bstar formation\b",
    r"\bstar[- ]forming\b",
    r"\bprotostars?\b",
    r"\bprotostellar\b",
    r"\bprestellar\b",
    r"\bIRDCs?\b",
    r"\binfrared dark clouds?\b",
    r"\bH\s*II region\b",
    r"\bHII region\b",
]

SPECIAL_NEGATIVES = {
    "solar_physics",
    "stellar_atmospheres_evolution",
    "planetary_disks_exoplanets",
    "compact_objects_transients",
    "relativistic_plasma_transients",
    "generic_mhd_plasma_theory",
    "dense_nuclear_matter",
    "generic_instrumentation",
}

SECONDARY_ASTRO = {"astro-ph.HE", "astro-ph.IM", "astro-ph.CO", "astro-ph.EP"}


def domain_evidence(paper: dict) -> tuple[float, float, list[str]]:
    title = paper["title"]
    abstract = paper["abstract"]
    total = 0.0
    title_score = 0.0
    hits = []
    for pattern, weight in DOMAIN_PATTERNS:
        title_hit = re.search(pattern, title, flags=re.I) is not None
        abstract_hit = re.search(pattern, abstract, flags=re.I) is not None
        if title_hit:
            title_score += 1.5 * weight
            total += 1.5 * weight
            hits.append("title:" + pattern)
        elif abstract_hit:
            total += weight
            hits.append("abstract:" + pattern)
    return total, title_score, hits


def direct_title_signal(title: str) -> bool:
    return any(re.search(p, title, flags=re.I) for p in DIRECT_TITLE_PATTERNS)


def rank_value(priority: str) -> int:
    return {"A": 3, "B": 2, "C": 1, "SKIP": 0}[priority]


def gate_priority(
    paper: dict,
    base_priority: str,
    pos_sem: float,
    neg_sem: float,
    pos_lex: float,
    neg_lex: float,
    best_negative: str,
    domain_score: float,
    title_domain_score: float,
) -> tuple[str, str]:
    """Apply category/domain rules, returning (priority, reason)."""
    margin = pos_sem - neg_sem
    primary = paper.get("primary_category", "") or ""
    title_direct = direct_title_signal(paper["title"])

    priority = base_priority
    reason = "contrastive"

    # Cross-lists whose primary category is not astrophysics need strong direct
    # ISM evidence. This removes nuclear/particle papers that happen to mention
    # supernovae or magnetic/turbulent language.
    if not primary.startswith("astro-ph."):
        if domain_score < 4.0 or margin < 0.0:
            return "SKIP", "non-astro primary without strong ISM evidence"
        if priority == "A" and domain_score < 6.0:
            priority = "B"
            reason = "non-astro primary capped at B"

    # HE/IM/CO/EP are allowed, but A/B requires concrete ISM-object evidence.
    if primary in SECONDARY_ASTRO and domain_score < 2.5:
        if priority in {"A", "B"}:
            if margin >= 0.035 and domain_score >= 1.0:
                priority = "C"
                reason = "secondary astro category; weak ISM evidence"
            else:
                return "SKIP", "secondary astro category without direct ISM evidence"

    # Within SR/GA, a strong negative interpretation plus weak object evidence
    # means the paper is likely solar/stellar/planetary/plasma rather than ISM.
    if best_negative in SPECIAL_NEGATIVES and domain_score < 2.0:
        if neg_sem >= pos_sem - 0.020:
            return "SKIP", "negative-domain match with weak ISM evidence"
        if priority == "A":
            priority = "C"
            reason = "weak ISM evidence despite positive semantic margin"

    # High-confidence title/object evidence can rescue papers that are close to
    # the planetary/protostellar boundary. This is intentionally conservative.
    if priority in {"SKIP", "C"}:
        if title_direct and domain_score >= 4.0 and pos_sem >= 0.70 and margin >= -0.025:
            priority = "B"
            reason = "rescued by direct ISM/star-formation title evidence"
        elif domain_score >= 6.0 and pos_sem >= 0.71 and margin >= -0.020:
            priority = "C"
            reason = "rescued by strong multi-signal ISM evidence"

    # Do not let broad single-word physics evidence alone create top-tier items.
    if priority == "A" and domain_score < 1.5 and title_domain_score == 0:
        priority = "C"
        reason = "A capped: insufficient direct ISM-object evidence"

    return priority, reason


def run(days: int, output_dir: Path, profile_path: Path) -> None:
    config = json.loads(profile_path.read_text(encoding="utf-8"))
    positive = config["topics"]
    negative = config["negative_topics"]

    papers = fetch_recent_astro_ph(days)
    if not papers:
        raise RuntimeError("No recent astro-ph papers returned by arXiv")

    model, tokenizer = load_specter2()
    positive_names = list(positive)
    negative_names = list(negative)

    model.set_active_adapters("adhoc_query")
    pos_queries = [positive[n]["description"] for n in positive_names]
    neg_queries = [negative[n]["description"] for n in negative_names]
    pos_q = embed_texts(model, tokenizer, pos_queries, batch_size=8)
    neg_q = embed_texts(model, tokenizer, neg_queries, batch_size=8)

    model.set_active_adapters("proximity")
    paper_texts = [p["title"] + tokenizer.sep_token + p["abstract"] for p in papers]
    paper_e = embed_texts(model, tokenizer, paper_texts, batch_size=16)

    pos_sem = safe_cosine_scores(pos_q, paper_e)
    neg_sem = safe_cosine_scores(neg_q, paper_e)
    pos_lex = lexical_topic_scores(papers, positive)
    neg_lex = lexical_topic_scores(papers, negative)

    results = []
    for i, paper in enumerate(papers):
        p_idx = int(np.argmax(pos_sem[i]))
        n_idx = int(np.argmax(neg_sem[i]))
        best_pos = float(pos_sem[i, p_idx])
        best_neg = float(neg_sem[i, n_idx])
        best_pos_lex = float(np.max(pos_lex[i]))
        best_neg_lex = float(np.max(neg_lex[i]))
        base = classify_priority(best_pos, best_neg, best_pos_lex, best_neg_lex)
        dscore, title_dscore, dhits = domain_evidence(paper)
        final, gate_reason = gate_priority(
            paper, base, best_pos, best_neg, best_pos_lex, best_neg_lex,
            negative_names[n_idx], dscore, title_dscore,
        )

        raw_display = display_score(best_pos, best_neg, best_pos_lex, best_neg_lex)
        # Small bonus for concrete object evidence; still not a probability.
        final_display = float(np.clip(raw_display + min(dscore, 6.0) * 1.5, 0, 100))

        top_idx = np.argsort(pos_sem[i])[::-1][:3]
        results.append({
            **paper,
            "current_keyword_selected": current_keyword_baseline(paper),
            "base_contrastive_priority": base,
            "priority": final,
            "gate_reason": gate_reason,
            "score": round(final_display, 1),
            "best_positive_topic": positive_names[p_idx],
            "best_positive_semantic": round(best_pos, 4),
            "best_negative_topic": negative_names[n_idx],
            "best_negative_semantic": round(best_neg, 4),
            "semantic_margin": round(best_pos - best_neg, 4),
            "positive_lexical": round(best_pos_lex, 4),
            "negative_lexical": round(best_neg_lex, 4),
            "domain_evidence_score": round(dscore, 2),
            "title_domain_score": round(title_dscore, 2),
            "domain_hits": dhits,
            "top_positive_topics": [
                {"topic": positive_names[int(j)], "semantic_raw": round(float(pos_sem[i, j]), 4)}
                for j in top_idx
            ],
        })

    results.sort(key=lambda r: (rank_value(r["priority"]), r["score"]), reverse=True)

    summary = {
        "generated_utc": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "lookback_days": days,
        "candidate_count": len(results),
        "current_keyword_selected": sum(r["current_keyword_selected"] for r in results),
        "A": sum(r["priority"] == "A" for r in results),
        "B": sum(r["priority"] == "B" for r in results),
        "C": sum(r["priority"] == "C" for r in results),
        "SKIP": sum(r["priority"] == "SKIP" for r in results),
        "downgraded_by_gate": sum(rank_value(r["priority"]) < rank_value(r["base_contrastive_priority"]) for r in results),
        "rescued_by_gate": sum(rank_value(r["priority"]) > rank_value(r["base_contrastive_priority"]) for r in results),
        "method": "v2.1 contrastive SPECTER2 + explicit ISM object evidence + primary-category gating + conservative rescue rules",
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.utcnow().strftime("%Y-%m-%d")
    json_path = output_dir / f"{stamp}-domain-gated.json"
    md_path = output_dir / f"{stamp}-domain-gated.md"
    json_path.write_text(json.dumps({"summary": summary, "papers": results}, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# ISM Literature Recommender v2.2 — Domain-Gated SPECTER2",
        "",
        f"Generated: {summary['generated_utc']}",
        f"Lookback: last {days} days",
        "",
        "## Summary",
        "",
        f"- Candidates: **{summary['candidate_count']}**",
        f"- Current keyword baseline: **{summary['current_keyword_selected']}**",
        f"- A: **{summary['A']}**",
        f"- B: **{summary['B']}**",
        f"- C: **{summary['C']}**",
        f"- SKIP: **{summary['SKIP']}**",
        f"- Downgraded by domain gate: **{summary['downgraded_by_gate']}**",
        f"- Rescued by domain evidence: **{summary['rescued_by_gate']}**",
        "",
        "## A/B candidates",
        "",
    ]

    for r in [x for x in results if x["priority"] in {"A", "B"}][:120]:
        top_topics = ", ".join(f"{x['topic']} ({x['semantic_raw']:.4f})" for x in r["top_positive_topics"])
        lines.extend([
            f"### [{r['priority']}] {r['score']:.1f} — {r['title']}",
            f"- **arXiv:** [{r['id']}]({r['main_page']})",
            f"- **Primary:** {r['primary_category'] or 'unknown'}",
            f"- **Positive / negative:** `{r['best_positive_topic']}` {r['best_positive_semantic']:.4f} / `{r['best_negative_topic']}` {r['best_negative_semantic']:.4f}",
            f"- **Margin:** {r['semantic_margin']:+.4f}",
            f"- **Domain evidence:** {r['domain_evidence_score']:.2f} (title {r['title_domain_score']:.2f})",
            f"- **Gate:** {r['base_contrastive_priority']} → {r['priority']} — {r['gate_reason']}",
            f"- **Top positive topics:** {top_topics}",
            f"- **Current keyword:** {'YES' if r['current_keyword_selected'] else 'NO'}",
            f"- **Abstract:** {r['abstract']}",
            "",
        ])

    downgraded = [r for r in results if rank_value(r["priority"]) < rank_value(r["base_contrastive_priority"])]
    rescued = [r for r in results if rank_value(r["priority"]) > rank_value(r["base_contrastive_priority"])]
    old_skip = [r for r in results if r["current_keyword_selected"] and r["priority"] == "SKIP"]
    new_ab = [r for r in results if not r["current_keyword_selected"] and r["priority"] in {"A", "B"}]

    lines.extend(["## Domain-gate downgrades", ""])
    lines.extend([
        f"- **{r['title']}** — {r['base_contrastive_priority']}→{r['priority']}; `{r['best_negative_topic']}`; evidence {r['domain_evidence_score']:.2f} — [{r['id']}]({r['main_page']})"
        for r in downgraded[:80]
    ] or ["- None"])

    lines.extend(["", "## Domain-evidence rescues", ""])
    lines.extend([
        f"- **{r['title']}** — {r['base_contrastive_priority']}→{r['priority']}; evidence {r['domain_evidence_score']:.2f} — [{r['id']}]({r['main_page']})"
        for r in rescued[:80]
    ] or ["- None"])

    lines.extend(["", "## Old keyword selected, v2.2 SKIP", ""])
    lines.extend([
        f"- **{r['title']}** — [{r['id']}]({r['main_page']})"
        for r in old_skip[:80]
    ] or ["- None"])

    lines.extend(["", "## v2.2 A/B, old keyword missed", ""])
    lines.extend([
        f"- **[{r['priority']}] {r['score']:.1f} — {r['title']}** — `{r['best_positive_topic']}` — [{r['id']}]({r['main_page']})"
        for r in new_ab[:80]
    ] or ["- None"])

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("[OK]", md_path)
    print("[OK]", json_path)
    print("[SUMMARY]", json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=10)
    parser.add_argument("--output-dir", default="v2_results")
    parser.add_argument("--profile", default="v2/topic_profiles.json")
    args = parser.parse_args()
    run(args.days, Path(args.output_dir), Path(args.profile))
