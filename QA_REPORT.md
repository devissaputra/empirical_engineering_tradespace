# Final QA Report

**Research bundle status: PASS.**  
**GitHub Actions status: PASS.**  
**Live GitHub administration status: About/topics still require repository-page authentication.**

## Checks completed
- provenance and source identity reviewed;
- licensing/reuse note recorded;
- complete MIT license restored and recognized by GitHub;
- all 103 objective observations packaged as a derived analysis table;
- the Pareto frontier independently recomputed from the full 103-row objective table;
- recomputed frontier matches the packaged 23 experiment IDs exactly;
- `results/empirical_summary.json` reconciled with packaged evidence;
- README/report language reconciled with the numerical results;
- study-specific methods live in `research/model.py`;
- tests exercise dominance logic, sample completeness, exact frontier IDs, and bundle consistency;
- internet rebuild script has no synthetic fallback and supports `--check`;
- four SVG assets are present and a dependency-free figure regeneration script is included;
- CI workflow installed and completed successfully;
- public-source empirical rebuild workflow installed and completed successfully against the UCI endpoint;
- local Markdown links and citation metadata were previously checked;
- no preregistration, peer-review, or primary-data-collection claim is made.

## Numerical verification
- source experiments represented in the offline objective table: **103**
- recomputed Pareto-efficient experiments: **23**
- packaged Pareto-efficient experiments: **23**
- exact frontier-ID agreement: **PASS**
- reported Pareto fraction: **0.223**

## GitHub-hosted verification
The repository's GitHub Actions checks have executed successfully on the repaired research bundle:

- **CI / test:** PASS
- **Empirical source rebuild / rebuild-check:** PASS

The CI job runs the study-specific tests, bundle validator, and SVG figure-generation smoke test. The source rebuild fetches the public UCI dataset and checks the released headline metrics and frontier IDs against a fresh rebuild.

## Final empirical finding
Twenty-three of 103 observed experiments (22.3%) are non-dominated under the stated three-objective rule. The frontier contains both low-cement and high-strength alternatives, so reporting a single “best” mix would hide decision-relevant trade-offs.

## Required interpretation boundary
This is an empirical trade-space demonstration, not a concrete design recommendation. Maximizing slump is an analytical objective here, not a universal engineering requirement; application-specific constraints, durability, cost, safety, and uncertainty are not modeled.

## Remaining GitHub UI-only metadata
The connected GitHub file API cannot edit repository About/topics, and the separate browser session was not authenticated for repository administration. The intended values are recorded in `GITHUB_METADATA.md`.

No research, code, data, test, CI, license, or reproducibility defect remains open in this QA report.
