# Reproducibility

## Offline verification

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
python scripts/run_sensitivity.py --check
```

The offline suite recomputes the baseline Pareto frontier from all 103 observations, checks the exact 23 baseline frontier IDs, recomputes all sensitivity specifications, and verifies the packaged JSON/CSV robustness outputs.

## Public-source rebuild

With internet access:

```bash
python scripts/fetch_and_analyze.py --check
```

The rebuild downloads the UCI source, computes the SHA-256 digest of the retrieved bytes, prints that digest in the run output, and fails if source-derived headline metrics or baseline frontier IDs differ from the packaged release.

## Packaged evidence hashes

`data/source_manifest.json` pins SHA-256 digests for the packaged complete objective table and sensitivity table. These hashes protect the exact evidence used for offline verification.

## Figures

Regenerate all five SVG figures:

```bash
python scripts/generate_figures.py
```

The generator uses only the Python standard library plus the packaged empirical tables and JSON outputs.

## Continuous integration

`.github/workflows/ci.yml` runs:
- unit and scientific-invariant tests;
- bundle validation;
- packaged sensitivity-output verification;
- figure-generation smoke tests.

`.github/workflows/empirical-rebuild.yml` performs the internet-enabled UCI source rebuild when analysis-relevant files change or when manually dispatched.
