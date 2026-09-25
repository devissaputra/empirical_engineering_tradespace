# Data Dictionary

## Provenance
See `data/source_manifest.json`. The repository records the public source, dataset DOI, license note, retrieval date, integrity policy, and hashes of packaged derived evidence.

## `data/derived/objective_observations.csv`
Complete four-column analysis table for all 103 experiments:
- `experiment_id`
- `cement`
- `slump_cm`
- `strength_mpa`

This is the authoritative offline input for the baseline and sensitivity analyses.

## `data/derived/primary_results.csv`
Complete baseline Pareto frontier containing all 23 non-dominated observations under the three-objective rule.

## `data/derived/sensitivity_results.csv`
One row per analysis specification with:
- eligible sample size;
- Pareto count;
- overlap with the baseline;
- baseline-retention fraction;
- Jaccard similarity;
- complete frontier experiment IDs.

## `results/empirical_summary.json`
Machine-readable primary sample sizes, summary statistics, and baseline finding.

## `results/sensitivity_summary.json`
Machine-readable definitions and results for all four operationalizations.

## Construct boundary
Higher slump is treated as preferable only in the baseline specification. The sensitivity analyses explicitly test the consequences of that choice. The 10 cm and 20 cm thresholds are analytical probes, not universal engineering requirements.
