# Reproducibility Guide

## Reproducibility goal

A reader should be able to verify the released results in two ways:

1. offline from the packaged objective table;
2. online by rebuilding the headline analysis from the named UCI source.

These routes are intentionally separate so that verification does not silently depend on network availability.

## Environment

The analysis is intentionally lightweight. Install the pinned project requirements with:

```bash
python -m pip install -r requirements.txt
```

## Offline verification

Run:

```bash
pytest -q
python run_demo.py
python scripts/run_sensitivity.py --check
```

The offline route checks:

- 103 packaged observations;
- exact 23 member baseline frontier;
- baseline frontier fraction;
- all four sensitivity specifications;
- exact sensitivity frontier IDs;
- packaged JSON and CSV agreement;
- SHA 256 integrity of the complete objective and sensitivity tables.

## Public source rebuild

With internet access:

```bash
python scripts/fetch_and_analyze.py --check
```

The script downloads the UCI source, calculates a SHA 256 digest of the retrieved bytes, reconstructs the three analysis variables, recomputes the baseline frontier, and fails if the headline metrics or exact frontier IDs differ from the packaged release.

A fixed upstream byte hash is not treated as a permanent truth because a public repository can legitimately correct a file. Research relevant drift is instead guarded by exact released metrics and frontier membership.

## Figure regeneration

```bash
python scripts/generate_figures.py
```

The figures are generated from the packaged objective and result files. They do not contain hand entered result values that differ from the release.

## Continuous integration

`.github/workflows/ci.yml` checks the code, scientific invariants, packaged sensitivity outputs, bundle validation, and figure generation.

`.github/workflows/empirical-rebuild.yml` runs the internet enabled source rebuild when analysis relevant files change or when manually dispatched.

## Evidence map

| Claim | Primary evidence |
|---|---|
| n = 103 | `data/derived/objective_observations.csv` |
| Baseline frontier = 23 | `data/derived/primary_results.csv` |
| Sensitivity counts | `results/sensitivity_summary.json` |
| Exact implementation | `research/model.py` |
| Public source consistency | `scripts/fetch_and_analyze.py --check` |
| Packaged release integrity | `data/source_manifest.json` and tests |

## Reproducibility boundary

The release verifies computational reproducibility for this dataset and these decision rules. It does not establish experimental replication, external validity, or field performance of any concrete mixture.
