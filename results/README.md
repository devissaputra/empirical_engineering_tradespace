# Results

- `empirical_summary.json` contains the primary sample statistics and baseline Pareto result.
- `sensitivity_summary.json` contains all four analysis specifications, exact frontier IDs, overlap counts, retention fractions, and Jaccard similarity relative to the baseline.

Both files are deterministic outputs of the documented analysis. `python scripts/run_sensitivity.py --check` verifies the packaged sensitivity result against a fresh recomputation.
