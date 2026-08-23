# coding: utf-8
from semantic_daily import _extract_categories
from semantic_recommender import score_papers


def paper(pid, title, abstract, primary):
    return {
        "id": pid,
        "title": title,
        "abstract": abstract,
        "authors": ["Test Author"],
        "subjects": primary,
        "categories": [primary],
        "primary_category": primary,
        "main_page": f"https://arxiv.org/abs/{pid}",
        "pdf": f"https://arxiv.org/pdf/{pid}.pdf",
    }


def main():
    cats = _extract_categories(
        "Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR); Plasma Physics (physics.plasm-ph)"
    )
    assert cats == ["astro-ph.GA", "astro-ph.SR", "physics.plasm-ph"], cats

    papers = [
        paper(
            "test.0001",
            "Dense molecular cloud kinematics and chemistry in an infrared dark cloud",
            "We use molecular-line observations of NH3, HCO+ and C18O to study dense clumps, infall, turbulence, and early massive star formation in an IRDC.",
            "astro-ph.GA",
        ),
        paper(
            "test.0002",
            "High Velocity Neutral Gas in the Fermi Bubbles",
            "We use H I data to study neutral clouds entrained in the Milky Way nuclear wind and their kinematics above the Galactic Centre.",
            "astro-ph.GA",
        ),
        paper(
            "test.0003",
            "Operational Solar Flare Peak Flux Nowcasting",
            "We predict solar flare peak X-ray flux from Solar Orbiter and GOES observations using machine learning for space weather.",
            "astro-ph.SR",
        ),
        paper(
            "test.0004",
            "Outflows in steep density gradients in tidal disruption events",
            "We model shocks and turbulent outflows from tidal disruption events and luminous fast blue optical transients around compact objects.",
            "astro-ph.HE",
        ),
    ]

    scored, summary = score_papers(papers)
    by_id = {p["id"]: p for p in scored}
    for p in scored:
        print(p["id"], p["priority"], p["score"], p["best_positive_topic"], p["scope_reason"])

    assert by_id["test.0001"]["priority"] in {"A", "B"}, by_id["test.0001"]
    assert by_id["test.0002"]["priority"] in {"A", "B"}, by_id["test.0002"]
    assert by_id["test.0003"]["priority"] in {"C", "SKIP"}, by_id["test.0003"]
    assert by_id["test.0004"]["priority"] in {"C", "SKIP"}, by_id["test.0004"]
    assert summary["candidate_count"] == 4
    print("[OK] semantic smoke test passed")


if __name__ == "__main__":
    main()
