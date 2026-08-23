# coding: utf-8
from bs4 import BeautifulSoup

from semantic_daily import _daily_submission_lists, _extract_categories, apply_final_scope_guard
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

    # Parser regression: include new + cross-lists but exclude replacements.
    html = """
    <div id='content'>
      <h3>Showing new listings</h3>
      <h3>New submissions</h3><dl id='new'></dl>
      <h3>Cross-lists</h3><dl id='cross'></dl>
      <h3>Replacements</h3><dl id='replace'></dl>
    </div>
    """
    content = BeautifulSoup(html, "html.parser").find("div", id="content")
    section_ids = [x.get("id") for x in _daily_submission_lists(content)]
    assert section_ids == ["new", "cross"], section_ids

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
        paper(
            "test.0005",
            "A model for the enhanced production rate of early-type hypervelocity stars in the Galactic halo",
            "The stars were ejected from the Galactic center by a black-hole gravitational slingshot. We constrain their stellar formation history and orbital dynamics in the nuclear star cluster.",
            "astro-ph.GA",
        ),
    ]

    scored, summary = score_papers(papers)
    scored, summary = apply_final_scope_guard(scored, summary)
    by_id = {p["id"]: p for p in scored}
    for p in scored:
        print(p["id"], p["priority"], p["score"], p["best_positive_topic"], p["scope_reason"])

    assert by_id["test.0001"]["priority"] in {"A", "B"}, by_id["test.0001"]
    assert by_id["test.0002"]["priority"] in {"A", "B"}, by_id["test.0002"]
    assert by_id["test.0003"]["priority"] in {"C", "SKIP"}, by_id["test.0003"]
    assert by_id["test.0004"]["priority"] in {"C", "SKIP"}, by_id["test.0004"]
    assert by_id["test.0005"]["priority"] in {"C", "SKIP"}, by_id["test.0005"]
    assert summary["candidate_count"] == 5
    print("[OK] semantic smoke test passed")


if __name__ == "__main__":
    main()
