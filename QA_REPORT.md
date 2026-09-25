# Final QA Report

**Research bundle status: PASS after robustness upgrade.**  
**GitHub Actions status before this upgrade: PASS.**  
**Post-upgrade workflows must pass on the new commit before this report should be treated as a green release.**  
**GitHub About/topics remain repository-UI metadata and are recorded in `GITHUB_METADATA.md`.**

## Repairs completed
- fixed literal `\\n` artifacts in the README bundle list;
- added an executed sensitivity analysis rather than a future-work note;
- added exact alternative frontier IDs, overlap, baseline retention, and Jaccard similarity;
- added `results/sensitivity_summary.json` and `data/derived/sensitivity_results.csv`;
- added `scripts/run_sensitivity.py --check`;
- expanded scientific tests to cover the sensitivity specifications;
- added a fifth empirical SVG figure for robustness results;
- updated the figure generator to reproduce five figures;
- added SHA-256 protection for packaged objective and sensitivity evidence;
- added raw-source SHA-256 reporting on every public-source rebuild;
- expanded the literature positioning for trade-space and concrete multi-objective optimization;
- strengthened the research questions and paper blueprint around operationalization sensitivity;
- removed the stale reference to the deleted `student_grade_regression` repository;
- synchronized README, protocol, research design, data dictionary, reproducibility guide, manifest, citation metadata, and bundle definition;
- upgraded the bundle version to 1.1.0.

## Primary numerical verification
- source experiments represented offline: **103**
- baseline Pareto-efficient experiments: **23**
- baseline Pareto fraction: **0.223**
- exact baseline frontier-ID agreement: **required**

## Sensitivity verification
- baseline three-objective frontier: **23**
- cement + strength only: **10**
- cement + strength, slump >= 10 cm: **10**
- cement + strength, slump >= 20 cm: **8**
- baseline retention across alternatives: **0.435, 0.435, 0.348**

## Interpretation
The robustness analysis shows that the decision set depends materially on the way slump is operationalized. The repository therefore treats frontier membership as conditional on declared objectives and constraints rather than as a universal engineering optimum.

## Remaining GitHub UI metadata
Set the repository About text and topics to the values in `GITHUB_METADATA.md`. No repository file can substitute for those GitHub UI fields.

## Release condition
The upgraded bundle is ready when the new CI and empirical-source rebuild runs both complete successfully.
