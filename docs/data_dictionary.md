# Data Dictionary

## Provenance
See `data/source_manifest.json`. Raw source observations are not silently republished.

## `data/derived/objective_observations.csv`
A four-column derived analysis table containing all 103 source experiment IDs and the three declared objective variables used by this study: cement, slump, and 28-day compressive strength. This table exists so the full Pareto frontier can be recomputed offline without redistributing unrelated source variables.

## `data/derived/primary_results.csv`
All 23 Pareto-efficient observations from the 103-row source dataset. Additional mixture variables are retained here to make the frontier interpretable.

## `results/empirical_summary.json`
Machine-readable headline sample sizes, estimates, and the release finding. Values must agree with README text and the derived CSVs.

## Construct boundary
This is an empirical trade-space demonstration, not a concrete design recommendation. Maximizing slump is an analytical objective here, not a universal engineering requirement; application-specific constraints, durability, cost, safety, and uncertainty are not modeled.
