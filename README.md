# ArXivDaily ISM

A free, automated arXiv recommender for interstellar-medium and star-formation research.

The project retrieves the latest `astro-ph` submissions, ranks them semantically, archives the scored candidate pool, creates a GitHub Issue, and can email the recommended papers to a research group. It runs entirely in GitHub Actions and does not require a paid model API or a continuously running local computer.

## What it does

1. Fetches recent `astro-ph` submissions through the official arXiv Atom API.
2. Uses **SPECTER2** scientific embeddings to compare each title + abstract with configurable research topics.
3. Contrasts relevant topics against explicit non-target astronomy domains to reduce false positives.
4. Uses a small local **zero-shot NLI** model to re-check ambiguous candidates.
5. Applies domain and scope guards for ISM / molecular-cloud / star-formation research.
6. Assigns each paper a priority:
   - **A** — strong recommendation
   - **B** — recommended
   - **C** — boundary candidate, archived for auditing
   - **SKIP** — screened out
7. Writes the daily report and full score archive to the repository.
8. Optionally sends the A/B recommendations by email.

## Main files

- `daily.py` — standalone production entry point.
- `semantic_daily.py` — arXiv ingestion, report generation, and email helpers.
- `semantic_recommender.py` — semantic ranking and scope-classification engine.
- `semantic_topics.json` — research-scope configuration.
- `semantic_smoke_test.py` — regression / smoke tests.
- `github_issue.py` — repository-independent GitHub Issue helper.
- `.github/workflows/daily_arxiv.yml` — scheduled production workflow.
- `.github/workflows/semantic_production_test.yml` — CI smoke test.

Generated outputs:

- `LATEST.md` — latest human-readable recommendation report.
- `Arxiv_Daily_Notice/` — dated report archive.
- `semantic_results/` — full daily scoring results in JSON.

## Quick start

### 1. Create your own repository

Create a new GitHub repository and copy this standalone project into it. GitHub Actions will automatically detect the repository owner and repository name; no source-code edits are required for that.

### 2. Configure research interests

Edit `semantic_topics.json`.

The configuration contains positive research topics, lexical cues, negative/background domains, and group-scope information. Topic descriptions should describe the science you actually want to receive rather than just list isolated keywords.

The default configuration is tuned for Galactic/local ISM, molecular clouds, cold atomic and molecular gas, dense structures, star formation, turbulence, magnetic fields, feedback, chemistry, and related observational work.

### 3. Configure email delivery (optional)

In **Settings → Secrets and variables → Actions**, add these repository secrets:

| Secret | Meaning |
| --- | --- |
| `SMTP_USERNAME` | SMTP login / sending account |
| `SMTP_PASSWORD` | SMTP password or app password |
| `SMTP_FROM` | From address |
| `EMAIL_TO` | Recipient address(es) |

The supplied workflow uses Gmail SMTP (`smtp.gmail.com`, port `465`). For Gmail, use an App Password rather than the normal account password.

If SMTP secrets are omitted, the recommender can still run and archive results on GitHub.

### 4. Enable GitHub Actions

The default workflow runs on weekdays at **09:30 Beijing time (UTC 01:30)** and also supports manual runs through **Actions → arXiv ISM Daily → Run workflow**.

To use another schedule, edit the cron expression in `.github/workflows/daily_arxiv.yml`.

### 5. Run a production test

The repository includes a smoke-test workflow and `semantic_smoke_test.py`. Run the test before changing model names, thresholds, or the topic configuration substantially.

## Models

The default system uses:

- Scientific embeddings: `allenai/specter2_base` with SPECTER2 adapters.
- Ambiguous-case classification: `cross-encoder/nli-deberta-v3-xsmall`.

Models are downloaded from Hugging Face and cached by GitHub Actions. The first run is therefore heavier than later runs.

## Design principles

### Semantic recommendation instead of substring matching

A paper is evaluated from its title, abstract, categories, domain evidence, semantic similarity, contrast with non-target domains, and ambiguous-case NLI score. This is intended to catch relevant cross-listed papers while avoiding papers that happen to contain generic words such as *shock*, *turbulence*, *feedback*, or *magnetic field* in an unrelated context.

### Stable research scope

This project does not retrain a model every day. The main personalization layer is the stable research-scope definition in `semantic_topics.json`. For a research group with reasonably stable interests, it should need only occasional review.

### Auditable results

A/B papers are the recommendations. C papers and the complete scored candidate pool are retained so false positives, false negatives, and threshold choices can be inspected later.

## Local use

Python 3.11 is recommended.

```bash
pip install -r requirements.txt
python semantic_smoke_test.py
python daily.py
```

Without GitHub or SMTP credentials, local runs can still be used to test retrieval and scoring; delivery steps that lack credentials are skipped.

## Customization ideas

The current project is deliberately simple enough to maintain in a research group. Useful extensions include:

- separate topic profiles for different group members;
- per-recipient recommendation emails;
- representative-paper prototypes;
- explicit thumbs-up / thumbs-down feedback;
- weekly digests in addition to daily delivery;
- HTML report pages or a lightweight dashboard.

## Project status

The semantic recommender, arXiv Atom ingestion, GitHub Actions automation, score archiving, and SMTP delivery have been exercised in production on the original development repository. This `standalone-v1` branch is the cleaned, repository-independent release candidate intended for migration into a fresh non-fork repository.

## Acknowledgements

The recommender relies on arXiv metadata, Hugging Face model hosting, AllenAI SPECTER2, open-source Transformers/Adapters tooling, and GitHub Actions.
