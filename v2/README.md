# v2 experiment

This branch is an isolated benchmark for replacing the production binary keyword filter with a group-oriented semantic recommender.

It does **not** send email, create issues, or modify `main.py`.

## Methods compared

1. **Current production baseline** — exact GA/SR + include/exclude substring logic.
2. **BM25** — lexical retrieval against each ISM group topic.
3. **SPECTER2 hybrid** — scientific semantic retrieval with:
   - 80% normalized SPECTER2 semantic similarity;
   - 20% exact specialist-term signal.

SPECTER2 uses the `adhoc_query` adapter to encode group-topic descriptions and the `proximity` adapter to encode candidate scientific papers.

## Outputs

Each run writes:

- `v2_results/YYYY-MM-DD-comparison.md`
- `v2_results/YYYY-MM-DD-comparison.json`

The Markdown report contains the highest-ranked candidates and explicit disagreement sets. The JSON preserves the full scored candidate pool for later quantitative evaluation.

## Calibration

The first experiment is intentionally uncalibrated. The next step is human labeling of a shared candidate sample, for example:

- strongly relevant
- relevant
- maybe
- irrelevant

Those labels can then tune topic definitions, thresholds, lexical weights, and later individual or group-specific profiles.
