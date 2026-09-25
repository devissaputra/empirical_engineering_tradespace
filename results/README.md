# Released Results

This directory contains machine readable results that are synchronized with the scientific report and tests.

## `empirical_summary.json`

Contains:

- study title;
- sample size;
- mean cement;
- mean slump;
- mean 28 day strength;
- baseline frontier count;
- baseline frontier fraction;
- maximum observed strength;
- minimum observed cement;
- a bounded baseline finding statement.

## `sensitivity_summary.json`

Contains all four decision formulations with:

- formulation description;
- eligible sample size;
- frontier size;
- exact frontier experiment IDs;
- overlap with the baseline;
- baseline retention;
- Jaccard similarity.

## Verification

Run:

```bash
python scripts/run_sensitivity.py --check
```

to recompute and compare the packaged sensitivity release.

Run:

```bash
python scripts/fetch_and_analyze.py --check
```

with internet access to compare the headline baseline results and exact frontier membership with a fresh fetch of the public UCI source.

## Interpretation

These files are deterministic outputs for the declared dataset and decision rules. They are not evidence of universal concrete performance or field suitability.
