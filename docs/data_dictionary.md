# Data Dictionary

## Provenance
See `data/source_manifest.json`. Raw source observations are not silently republished.

## `data/derived/primary_results.csv`
All 23 Pareto-efficient observations from the 103-row source dataset.

## `data/derived/secondary_results.csv`
When present and non-empty, this contains a second derived table needed to reproduce a reported comparison. If empty, no second packaged table is required.

## `results/empirical_summary.json`
Machine-readable headline sample sizes, estimates, and the release finding. Values must agree with README text and the derived CSVs.

## Construct boundary
This is an empirical trade-space demonstration, not a concrete design recommendation. Maximizing slump is an analytical objective here, not a universal engineering requirement; application-specific constraints, durability, cost, safety, and uncertainty are not modeled.
