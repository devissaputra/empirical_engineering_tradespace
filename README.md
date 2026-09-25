# Empirical Engineering Design Trade Space: Concrete Slump Experiments

[![CI](https://github.com/devissaputra/empirical_engineering_tradespace/actions/workflows/ci.yml/badge.svg)](https://github.com/devissaputra/empirical_engineering_tradespace/actions/workflows/ci.yml)
[![Empirical source rebuild](https://github.com/devissaputra/empirical_engineering_tradespace/actions/workflows/empirical-rebuild.yml/badge.svg)](https://github.com/devissaputra/empirical_engineering_tradespace/actions/workflows/empirical-rebuild.yml)

> **System Engineering Research Package** · Engineering Management Research · Trade Space Analysis · Decision Analysis

This repository is a reproducible secondary study of 103 concrete mixture experiments from the UCI Concrete Slump Test dataset. It uses observed laboratory alternatives to identify Pareto efficient tradeoffs and then tests how much the decision set changes when the role of slump is changed.

![Observed trade space](assets/research_design.svg)

## Start here

- [Scientific report](REPORT.md)
- [Empirical study protocol](EMPIRICAL_STUDY.md)
- [Paper blueprint](docs/paper_blueprint.md)
- [Research design](docs/research_design.md)
- [Analysis plan](docs/analysis_plan.md)
- [Reproducibility guide](REPRODUCIBILITY.md)
- [Data provenance](data/README.md)
- [Final QA evidence](QA_REPORT.md)

## Research questions

1. Which observed alternatives are non dominated when cement is minimized while slump and 28 day compressive strength are maximized?
2. How stable is that frontier when slump is omitted as an objective or treated as an eligibility threshold?

## Empirical source

| Item | Value |
|---|---|
| Dataset | UCI Concrete Slump Test |
| Instances | 103 laboratory experiments |
| DOI | 10.24432/C5FG7D |
| License | CC BY 4.0 |
| Analysis date | 25 September 2026 |
| Synthetic fallback | None |

The packaged release contains the complete objective table needed for offline verification while the internet enabled workflow can rebuild the headline findings from the public UCI source.

## Baseline formulation

The baseline minimizes cement and maximizes slump and 28 day compressive strength. An observation is Pareto efficient when no other observed experiment is at least as good on every declared objective and strictly better on at least one.

![Analysis workflow](assets/method.svg)

## Headline results

| Metric | Value |
|---|---:|
| Experiments | 103 |
| Mean cement | 229.89 kg/m³ |
| Mean slump | 18.05 cm |
| Mean 28 day strength | 36.04 MPa |
| Baseline frontier | 23 observations |
| Baseline frontier fraction | 22.3% |
| Maximum observed strength | 58.53 MPa |
| Minimum observed cement | 137.0 kg/m³ |

The result should be read as a set of observed tradeoffs, not as one recommended concrete mixture.

## Sensitivity to the treatment of slump

| Specification | Eligible n | Frontier n | Baseline retained |
|---|---:|---:|---:|
| Baseline, three objectives | 103 | 23 | 100.0% |
| Cement and strength only | 103 | 10 | 43.5% |
| Cement and strength with slump ≥ 10 cm | 84 | 10 | 43.5% |
| Cement and strength with slump ≥ 20 cm | 63 | 8 | 34.8% |

The alternative frontiers are much smaller than the baseline frontier. In this dataset, the efficient set therefore depends materially on how workability enters the decision model.

![Sensitivity analysis](assets/sensitivity.svg)

## What is new in this repository

The contribution is not a new Pareto algorithm and not a new concrete design standard. The repository provides a transparent observed alternative trade study with four features:

1. exact Pareto analysis over real laboratory alternatives rather than synthetic candidates;
2. explicit separation between objectives and eligibility constraints;
3. frontier membership sensitivity quantified with overlap, retention, and Jaccard similarity;
4. evidence integrity checks that connect the public source, packaged tables, code, figures, and released claims.

## Claim boundary

This analysis does not prescribe a field ready mix. It does not model cost, embodied carbon, durability, safety factors, curing conditions, uncertainty, constructability, or project specific acceptance rules. Cement is not a complete environmental proxy, and larger slump is not assumed to be universally preferable outside the baseline stress test.

## Reproduce

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
python scripts/run_sensitivity.py --check
```

With internet access:

```bash
python scripts/fetch_and_analyze.py --check
```

Regenerate the figures:

```bash
python scripts/generate_figures.py
```

## Repository map

- `REPORT.md`: paper facing scientific report
- `EMPIRICAL_STUDY.md`: protocol, operationalization, findings, and validity
- `docs/paper_blueprint.md`: manuscript structure and writing plan
- `docs/analysis_plan.md`: estimands, decision rules, and release outputs
- `docs/research_design.md`: research design and inference boundaries
- `docs/data_dictionary.md`: variable and output definitions
- `data/source_manifest.json`: source identity, license, and integrity hashes
- `data/derived/`: objective table, baseline frontier, and sensitivity table
- `results/`: machine readable released results
- `research/model.py`: dominance and validation logic
- `scripts/`: source rebuild, sensitivity analysis, and figure generation
- `tests/`: behavioral and scientific invariant tests
- `QA_REPORT.md`: release verification evidence

## Research integrity

This is a documented secondary analysis, not a preregistration. It is not presented as peer reviewed or externally validated. Claims are intentionally limited to the named dataset and declared decision rules.
