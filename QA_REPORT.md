# Final QA Report

## Release verdict

**Status: PASS for a reproducible portfolio research package.**

This QA document verifies consistency. It is not the scientific report. The paper facing narrative is in [REPORT.md](REPORT.md).

## Scope checked

The release was checked for agreement across:

- public source identity and license metadata;
- packaged objective observations;
- baseline Pareto frontier;
- sensitivity specifications;
- machine readable results;
- analysis code;
- tests;
- continuous integration;
- reproducibility instructions;
- figures;
- README and scientific report claims;
- paper blueprint and research design;
- validity and integrity statements.

## Numerical consistency

| Check | Released value | Status |
|---|---:|---|
| Total observations | 103 | PASS |
| Baseline frontier count | 23 | PASS |
| Baseline frontier fraction | 0.223 | PASS |
| Cement and strength frontier | 10 | PASS |
| Slump ≥ 10 cm frontier | 10 | PASS |
| Slump ≥ 20 cm frontier | 8 | PASS |
| Exact baseline frontier IDs | 23 IDs | PASS |
| Packaged objective table hash | pinned | PASS |
| Packaged sensitivity table hash | pinned | PASS |

## Scientific consistency

The documentation now uses one consistent interpretation: frontier membership is conditional on the declared objectives and constraints. No document presents a Pareto efficient observation as a universal optimum.

The role of slump is explicitly treated as a modeling choice. The 10 cm and 20 cm thresholds are described only as analytical stress tests. They are not described as field standards.

Cement content is described as a material intensity variable, not as a direct estimate of cost or lifecycle carbon.

## Evidence chain

1. `scripts/fetch_and_analyze.py` downloads the UCI source and recomputes the released baseline metrics.
2. `data/derived/objective_observations.csv` provides the complete offline objective table.
3. `research/model.py` implements the dominance rules and bundle validation.
4. `scripts/run_sensitivity.py --check` recomputes all four specifications.
5. `results/*.json` and `data/derived/*.csv` store deterministic released outputs.
6. `scripts/generate_figures.py` regenerates the study figures from packaged evidence.
7. Tests verify exact frontier IDs, sensitivity counts, and release invariants.

## Presentation repairs completed

- replaced the portfolio explanation with cleaner prose without dash punctuation;
- replaced the portfolio Report MD target with a real scientific `REPORT.md`;
- rebuilt the trade space figure with labeled axes, scale ticks, a frontier legend, and a quantitative caption;
- rebuilt the method figure into a research pipeline that distinguishes source validation, baseline analysis, sensitivity analysis, and interpretation;
- expanded the scientific report, protocol, research design, analysis plan, data notes, reproducibility guide, and manuscript blueprint;
- strengthened the distinction between empirical evidence and engineering recommendation;
- retained explicit provenance, licensing, and non preregistration statements.

## Remaining limitations

A PASS means the repository is internally coherent and reproducible for its stated scope. It does not mean the study is peer reviewed, publication accepted, externally validated, or sufficient for field concrete design.
