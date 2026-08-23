# coding: utf-8
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import smtplib
import ssl
from email.message import EmailMessage

import markdown
import requests
from bs4 import BeautifulSoup

from config import NEW_SUB_URL
from github_issue import make_github_issue
from semantic_recommender import score_papers


def _extract_categories(subjects: str) -> list[str]:
    """Extract arXiv category codes from the parenthesized subject labels."""
    categories = []
    for value in re.findall(r"\(([^()]+)\)", subjects):
        value = value.strip()
        if re.fullmatch(r"[A-Za-z0-9.-]+", value):
            categories.append(value)
    return categories


def fetch_daily_papers() -> tuple[str, list[dict]]:
    """Read the official astro-ph new-list page, but do not keyword-filter it."""
    headers = {"User-Agent": "ArXivDaily-ISM/2.0 (+https://github.com/alznlyux/ArXivDaily_StarFormation)"}
    response = requests.get(NEW_SUB_URL, headers=headers, timeout=120)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.body.find("div", {"id": "content"})
    if content is None or content.find("h3") is None or content.dl is None:
        raise RuntimeError("Could not parse the arXiv new-list page")

    issue_title = content.find("h3").get_text(" ", strip=True)
    dt_list = content.dl.find_all("dt")
    dd_list = content.dl.find_all("dd")
    if len(dt_list) != len(dd_list):
        raise RuntimeError("arXiv listing dt/dd lengths differ")

    papers = []
    for dtnode, ddnode in zip(dt_list, dd_list):
        a_abs = dtnode.find("a", title="Abstract")
        title_node = ddnode.find("div", {"class": "list-title mathjax"})
        authors_node = ddnode.find("div", {"class": "list-authors"})
        subjects_node = ddnode.find("div", {"class": "list-subjects"})
        abstract_node = ddnode.find("p", {"class": "mathjax"})
        if not all([a_abs, title_node, authors_node, subjects_node, abstract_node]):
            continue

        paper_id = a_abs["href"].rstrip("/").split("/")[-1]
        title = title_node.get_text(" ", strip=True).replace("Title:", "", 1).strip()
        authors_text = authors_node.get_text(" ", strip=True).replace("Authors:", "", 1).strip()
        subjects = subjects_node.get_text(" ", strip=True).replace("Subjects:", "", 1).strip()
        abstract = re.sub(r"\s+", " ", abstract_node.get_text(" ", strip=True)).strip()
        categories = _extract_categories(subjects)
        astro_categories = [c for c in categories if c.startswith("astro-ph.")]
        primary = categories[0] if categories else (astro_categories[0] if astro_categories else "")

        papers.append({
            "id": paper_id,
            "title": title,
            "authors": [x.strip() for x in authors_text.split(",") if x.strip()],
            "subjects": subjects,
            "categories": categories,
            "primary_category": primary,
            "abstract": abstract,
            "main_page": f"https://arxiv.org/abs/{paper_id}",
            "pdf": f"https://arxiv.org/pdf/{paper_id}.pdf",
        })
    if not papers:
        raise RuntimeError("No papers parsed from astro-ph/new")
    print(f"[INFO] Parsed {len(papers)} papers from astro-ph/new")
    return issue_title, papers


def paper_block(p: dict) -> str:
    authors = ", ".join(p.get("authors", []))
    top_topics = ", ".join(p.get("top_topics", [])[:3])
    return "\n".join([
        f"#### [{p['priority']}] {p['title']}",
        f"- **Score:** {p['score']:.1f}  ",
        f"- **Topics:** {top_topics}  ",
        f"- **Authors:** {authors}  ",
        f"- **Subjects:** {p.get('subjects', '')}  ",
        f"- **ArXiv:** [{p['main_page']}]({p['main_page']})  ",
        f"- **PDF:** [{p['pdf']}]({p['pdf']})  ",
        f"- **Abstract:** {p['abstract']}",
        "",
    ])


def build_reports(issue_title: str, scored: list[dict], summary: dict) -> tuple[str, str]:
    selected = [p for p in scored if p["priority"] in {"A", "B"}]
    boundary = [p for p in scored if p["priority"] == "C"]
    date = dt.date.today().isoformat()

    header = [
        f"# {issue_title}",
        "",
        "Free semantic ISM / star-formation screening: **SPECTER2 + local zero-shot NLI**.",
        "No paid model API is used.",
        "",
        f"### Today: {len(selected)} recommended papers",
        f"- Priority A: **{summary['A']}**",
        f"- Priority B: **{summary['B']}**",
        f"- Boundary C (archive only): **{summary['C']}**",
        f"- Screened astro-ph candidates: **{summary['candidate_count']}**",
        "",
    ]
    if not selected:
        header.extend(["There is no A/B recommendation today.", ""])

    selected_text = "\n".join(paper_block(p) for p in selected)
    email_report = "\n".join(header) + selected_text
    email_report += f"\n\nGenerated {date}.\n"

    full_report = email_report
    full_report += "\n\n### Boundary candidates (C; not emailed as recommendations)\n\n"
    if boundary:
        for p in boundary:
            full_report += f"- **{p['title']}** — `{p.get('best_positive_topic')}` — [{p['id']}]({p['main_page']})\n"
    else:
        full_report += "- None\n"
    full_report += "\n\nby Al.Zn (Xin Lyu).\n"
    return full_report, email_report


def send_email(markdown_text: str, n_selected: int) -> None:
    host = os.environ.get("SMTP_HOST")
    port = int(os.environ.get("SMTP_PORT", "465"))
    user = os.environ.get("SMTP_USERNAME")
    pwd = os.environ.get("SMTP_PASSWORD")
    sender = os.environ.get("SMTP_FROM")
    recipients = os.environ.get("EMAIL_TO")
    if not all([host, user, pwd, sender, recipients]):
        print("[WARN] SMTP not configured; skip email")
        return

    html_body = markdown.markdown(
        markdown_text,
        extensions=["extra", "nl2br", "sane_lists", "toc", "pymdownx.magiclink"],
    )
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
    body {{ font:14px/1.6 -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial; color:#111 }}
    a {{ text-decoration:none }} code,pre {{ font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace }}
    </style></head><body>{html_body}</body></html>"""

    msg = EmailMessage()
    msg["Subject"] = f"arXiv ISM Daily · {dt.date.today().isoformat()} · {n_selected} papers"
    msg["From"] = sender
    msg["To"] = recipients
    msg.set_content(markdown_text)
    msg.add_alternative(html, subtype="html")

    if port == 465:
        with smtplib.SMTP_SSL(host, port, context=ssl.create_default_context()) as smtp:
            smtp.login(user, pwd)
            smtp.send_message(msg)
    else:
        with smtplib.SMTP(host, port) as smtp:
            smtp.ehlo()
            smtp.starttls(context=ssl.create_default_context())
            smtp.login(user, pwd)
            smtp.send_message(msg)
    print("[OK] Mail sent to", recipients)


def main(token: str) -> None:
    issue_title, papers = fetch_daily_papers()
    scored, summary = score_papers(papers)
    selected = [p for p in scored if p["priority"] in {"A", "B"}]
    full_report, email_report = build_reports(issue_title, scored, summary)

    date = dt.date.today().isoformat()
    notice_dir = pathlib.Path("Arxiv_Daily_Notice")
    score_dir = pathlib.Path("semantic_results")
    notice_dir.mkdir(exist_ok=True)
    score_dir.mkdir(exist_ok=True)
    notice_path = notice_dir / f"{date}-Arxiv-Daily-Paper.md"
    notice_path.write_text(full_report, encoding="utf-8")
    pathlib.Path("README.md").write_text(full_report, encoding="utf-8")
    (score_dir / f"{date}-scores.json").write_text(
        json.dumps({"summary": summary, "papers": scored}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Email first. If SMTP fails, the workflow can safely fall back to the
    # legacy pipeline without creating a duplicate semantic issue beforehand.
    send_email(email_report, len(selected))
    make_github_issue(
        title=f"{issue_title} · semantic ISM",
        body=full_report,
        labels=None,
        TOKEN=token,
    )
    print("[SUMMARY]", json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", required=True)
    args = parser.parse_args()
    main(args.token)
