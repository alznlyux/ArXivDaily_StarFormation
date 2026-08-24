# coding: utf-8
"""v2.6 stable group-scope calibration for the ISM recommender.

This is not a learned model and is not intended to change daily. It encodes the
current group scope: Galactic/local ISM and star-formation science are primary;
CGM, high-redshift galaxy-evolution, and broad extragalactic survey papers are
kept as lower-priority boundary material unless their title is explicitly about
an ISM object/process.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path

RANK = {"SKIP": 0, "C": 1, "B": 2, "A": 3}


def latest_nli_json(output_dir: Path) -> Path:
    files = sorted(output_dir.glob("*-zero-shot-reranked.json"))
    if not files:
        raise FileNotFoundError("No *-zero-shot-reranked.json found")
    return files[-1]


def has(pattern: str, text: str) -> bool:
    return re.search(pattern, text, flags=re.I) is not None


def calibrate(p: dict) -> tuple[str, str]:
    old = p.get("priority", "SKIP")
    title = p.get("title", "")
    abstract = p.get("abstract", "")
    text = title + "\n" + abstract

    # Explicit Galactic/local ISM rescues. A Galactic-centre mention alone is
    # not enough: the same region hosts stellar-dynamics/SMBH papers. Require a
    # direct gas/cloud/ISM object signal, not merely "star formation".
    fermi_hi = (
        has(r"Fermi Bubbles?", text)
        and has(r"\b(?:neutral gas|neutral clouds?|H\s*I\s+(?:data|clouds?|gas|emission)|N[_ ]?HI)\b", text)
    )
    cmz_title = has(r"\b(?:CMZ|Central Molecular Zone)\b", title)
    galactic_center_gas = (
        has(r"\bGalactic Cent(?:re|er)\b", text)
        and has(
            r"\b(?:molecular gas|molecular clouds?|atomic gas|neutral gas|gas cloud|gas clouds|"
            r"interstellar medium|ISM|dense gas|CMZ|Central Molecular Zone)\b",
            text,
        )
    )
    interstellar_magnetic = has(
        r"\binterstellar\b.*\b(?:magnetic|reconnection|filament|gas|medium)\b|"
        r"\b(?:magnetic|reconnection|filament)\b.*\binterstellar\b",
        title,
    )
    explicit_hi_title = has(
        r"\b(?:neutral gas|neutral hydrogen|H\s*I\s+(?:clouds?|gas|emission|absorption|survey))\b",
        title,
    )

    if old in {"SKIP", "C"} and (
        fermi_hi or cmz_title or galactic_center_gas or interstellar_magnetic or explicit_hi_title
    ):
        return "B", "stable-scope rescue: explicit Galactic/local ISM object in title/abstract"

    # External-galaxy CGM is not the group's core daily-reading scope even when
    # the tracer is H I.
    external_cgm = has(r"\b(?:circumgalactic medium|CGM)\b", text) and not has(
        r"\b(?:Milky Way|Galactic Centre|Galactic Center|Fermi Bubbles?)\b", text
    )
    if external_cgm and old in {"A", "B"}:
        return "C", "stable-scope cap: external-galaxy CGM rather than Galactic/local ISM"

    # High-z galaxy morphology/evolution papers can contain resolved ISM and SF
    # language, but the primary scientific target is still galaxy evolution.
    highz_galaxy = (
        has(r"\b(?:high[- ]redshift|early Universe|reionization|z\s*[=~>]\s*[4-9])\b", text)
        and has(r"\bgalax(?:y|ies)\b", title)
    )
    if highz_galaxy and old in {"A", "B"}:
        return "C", "stable-scope cap: high-redshift galaxy-evolution focus"

    # Broad samples of external galaxies are kept in the archive as C unless
    # the title itself names a molecular cloud / ISM structure as the target.
    plural_external_galaxies = has(r"\bgalaxies\b", title) and not has(r"\bGalactic\b", title)
    direct_ism_title = has(
        r"\b(?:molecular cloud|interstellar medium|neutral hydrogen|H\s*I\s+(?:gas|cloud|emission)|"
        r"dense core|H\s*II region|star[- ]forming region)\b",
        title,
    )
    if plural_external_galaxies and not direct_ism_title and old in {"A", "B"}:
        return "C", "stable-scope cap: broad external-galaxy sample"

    return old, "stable-scope calibration leaves decision unchanged"


def run(input_json: Path, output_dir: Path) -> None:
    payload = json.loads(input_json.read_text(encoding="utf-8"))
    papers = payload["papers"]
    promoted = downgraded = 0

    for p in papers:
        old = p.get("priority", "SKIP")
        new, reason = calibrate(p)
        promoted += int(RANK[new] > RANK[old])
        downgraded += int(RANK[new] < RANK[old])
        p["pre_scope_priority"] = old
        p["priority"] = new
        p["scope_reason"] = reason

    papers.sort(key=lambda p: (RANK[p["priority"]], float(p.get("score", 0.0))), reverse=True)
    summary = {
        "generated_utc": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "source": input_json.name,
        "candidate_count": len(papers),
        "A": sum(p["priority"] == "A" for p in papers),
        "B": sum(p["priority"] == "B" for p in papers),
        "C": sum(p["priority"] == "C" for p in papers),
        "SKIP": sum(p["priority"] == "SKIP" for p in papers),
        "promoted_by_scope": promoted,
        "downgraded_by_scope": downgraded,
        "scope": "Galactic/local ISM and star formation primary; external CGM/high-z galaxy evolution/broad galaxy surveys secondary",
        "method": "SPECTER2 + domain gate + zero-shot NLI + stable group-scope calibration",
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.utcnow().strftime("%Y-%m-%d")
    json_path = output_dir / f"{stamp}-final-calibrated.json"
    md_path = output_dir / f"{stamp}-final-calibrated.md"
    json_path.write_text(json.dumps({"summary": summary, "papers": papers}, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# ISM Literature Recommender v2.6 — Final Calibrated Benchmark",
        "",
        f"Generated: {summary['generated_utc']}",
        f"Source: `{summary['source']}`",
        "",
        "## Summary",
        "",
        f"- Candidates: **{summary['candidate_count']}**",
        f"- A: **{summary['A']}**",
        f"- B: **{summary['B']}**",
        f"- C: **{summary['C']}**",
        f"- SKIP: **{summary['SKIP']}**",
        f"- Scope promotions: **{summary['promoted_by_scope']}**",
        f"- Scope downgrades: **{summary['downgraded_by_scope']}**",
        "",
        "## A/B candidates",
        "",
    ]
    for p in [x for x in papers if x["priority"] in {"A", "B"}]:
        lines.extend([
            f"### [{p['priority']}] {float(p.get('score', 0)):.1f} — {p['title']}",
            f"- **arXiv:** [{p['id']}]({p['main_page']})",
            f"- **Primary:** {p.get('primary_category') or 'unknown'}",
            f"- **Topic:** `{p.get('best_positive_topic')}`",
            f"- **Scope:** {p.get('pre_scope_priority')} → {p.get('priority')} — {p.get('scope_reason')}",
            f"- **Abstract:** {p.get('abstract', '')}",
            "",
        ])

    changed = [p for p in papers if p["priority"] != p["pre_scope_priority"]]
    lines.extend(["## Scope changes", ""])
    if changed:
        for p in changed:
            lines.append(
                f"- **{p['pre_scope_priority']} → {p['priority']}** — {p['title']} — {p['scope_reason']} — [{p['id']}]({p['main_page']})"
            )
    else:
        lines.append("- None")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("[OK]", md_path)
    print("[OK]", json_path)
    print("[SUMMARY]", json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=None)
    parser.add_argument("--output-dir", default="v2_results")
    args = parser.parse_args()
    out = Path(args.output_dir)
    source = Path(args.input) if args.input else latest_nli_json(out)
    run(source, out)
