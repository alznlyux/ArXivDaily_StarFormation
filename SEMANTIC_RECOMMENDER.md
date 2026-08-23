# Free semantic ISM recommender

The production semantic pipeline is designed to run entirely in GitHub Actions without a paid model API or a local computer.

## Daily pipeline

1. Read the full `astro-ph/new` listing.
2. SPECTER2 compares each title + abstract with positive ISM/star-formation topics and explicit non-ISM topics.
3. Direct research-object evidence and arXiv categories prevent generic `shock`, `turbulence`, `feedback`, or `magnetic field` papers from being treated as ISM automatically.
4. A small local zero-shot NLI model re-checks ambiguous abstracts.
5. Stable group-scope calibration prioritizes Galactic/local ISM and star formation while keeping external CGM, high-redshift galaxy evolution, and broad galaxy surveys as secondary material.
6. Priority A/B papers are emailed. Priority C papers remain in the GitHub archive for recall auditing.
7. If the semantic pipeline fails, the legacy keyword pipeline runs automatically for that day.

## This is not daily model training

No model is retrained every day. `semantic_topics.json` is a stable research-scope configuration, not a continuously updated training set.

If the group membership and research directions are stable, the topic configuration can remain unchanged for many months. A practical maintenance schedule is:

- **Daily:** no manual maintenance.
- **Every 1–3 months:** optionally glance at obvious false positives / false negatives; change nothing if performance is fine.
- **When a new research direction or group member is added:** add or revise the relevant topic description.
- **Every 6–12 months:** review the group scope once.

Representative-paper prototypes or explicit thumbs-up / thumbs-down feedback can be added later, but they are optional and are not required for the current system to run.

## Free models

- Scientific embedding: `allenai/specter2_base` + SPECTER2 query/proximity adapters.
- Zero-shot NLI: `cross-encoder/nli-deberta-v3-xsmall`.

The Hugging Face model cache is stored through GitHub Actions cache. The first run downloads the models; later runs restore the cache when available.

## Files

- `semantic_topics.json` — stable group topic/scope definitions.
- `semantic_recommender.py` — semantic scoring and classification engine.
- `semantic_daily.py` — daily arXiv ingestion, report, GitHub issue, and email delivery.
- `semantic_results/YYYY-MM-DD-scores.json` — full scored daily candidate pool for later auditing.
