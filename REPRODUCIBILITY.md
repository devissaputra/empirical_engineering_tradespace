# Reproducibility

## Offline verification

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
```

The offline suite recomputes the Pareto frontier from all 103 observations in `data/derived/objective_observations.csv` and checks that it exactly matches the 23 packaged frontier experiments.

## Public-source rebuild

With internet access:

```bash
python scripts/fetch_and_analyze.py --check
```

This fetches the UCI source and fails if the source-derived headline metrics or frontier IDs differ from the packaged release.

## Figures

Regenerate all four SVG figures:

```bash
python scripts/generate_figures.py
```

The generator uses only the Python standard library plus the packaged empirical tables.

## Continuous integration

`.github/workflows/ci.yml` runs offline scientific tests, the bundle validator, and a figure-generation smoke test on pushes and pull requests. `.github/workflows/empirical-rebuild.yml` provides a manual internet-enabled source rebuild check.
