# Empirical Engineering Design Trade Space: Concrete Slump Experiments

> **Empirical Research Bundle** · **Portfolio Track: Engineering Management Research** · Systems Engineering / Trade-Space Analysis / Decision Analysis

Empirical multi-objective trade-space analysis of 103 UCI concrete slump experiments using an explicit Pareto frontier.

![Empirical workflow](assets/architecture.svg)

## Study status

**Completed secondary empirical analysis.** Reported findings were calculated from the named public source on 25 September 2026. The rebuild script contains **no synthetic fallback**. Raw source data are not republished unless source terms permit it; `data/source_manifest.json` records provenance, retrieval details, licensing notes, and the claim boundary.

## Research question

> What engineering alternatives remain non-dominated when cement is minimized while slump and 28-day compressive strength are maximized?

## Design

- **Design:** Secondary multi-objective analysis of 103 laboratory mixture experiments
- **Source:** UCI Concrete Slump Test
- **Source page:** https://archive.ics.uci.edu/dataset/182/concrete%2Bslump%2Btest
- **Direct data endpoint:** `https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/slump/slump_test.data`
- **Retrieval / analysis date:** 2026-09-25
- **Licensing / reuse note:** CC BY 4.0; dataset DOI 10.24432/C5FG7D.

## Hypotheses

1. H1: the observed design space contains multiple non-dominated mixtures rather than one universally best mixture.
2. H2: low-cement and high-strength alternatives occupy different parts of the frontier, demonstrating a genuine engineering trade-off.

## Empirical method

Parse all 103 experiments, define three explicit objectives (minimize cement; maximize slump; maximize 28-day strength), and identify an observation as Pareto-efficient only when no other observed mixture is at least as good on all three objectives and strictly better on at least one.

![Method](assets/method.svg)

## Headline empirical finding

Twenty-three of 103 observed experiments (22.3%) are non-dominated under the stated three-objective rule. The frontier contains both low-cement and high-strength alternatives, so reporting a single “best” mix would hide decision-relevant trade-offs.

### Headline metrics

- **n experiments**: 103
- **cement mean**: 229.89
- **strength mean mpa**: 36.04
- **slump mean cm**: 18.05
- **pareto count**: 23
- **pareto fraction**: 0.223
- **max strength mpa**: 58.53
- **min cement kg m3**: 137.0

The packaged derived tables are documented in `docs/data_dictionary.md`. That document states explicitly whether each CSV is a complete analysis table or a diagnostic subset.

![Research evidence](assets/research_design.svg)

## What this study can and cannot claim

**Can claim:** the computations in this repository summarize the named public dataset under the documented operationalization.

**Cannot claim:** This is an empirical trade-space demonstration, not a concrete design recommendation. Maximizing slump is an analytical objective here, not a universal engineering requirement; application-specific constraints, durability, cost, safety, and uncertainty are not modeled.

![Finding and boundary](assets/evaluation.svg)

## Reproduce

Offline verification of packaged empirical results:

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
```

Recompute the empirical analysis from the public source (internet required):

```bash
python scripts/fetch_and_analyze.py
```

The online rebuild calls study-specific functions from `research/model.py`; the offline test suite recomputes the Pareto frontier from all 103 packaged objective observations and checks the exact 23 frontier IDs. Figures can be regenerated with `python scripts/generate_figures.py`.

## Research bundle contents

- `README.md` — study overview and bounded findings
- `EMPIRICAL_STUDY.md` — protocol, validity, and interpretation
- `data/source_manifest.json` — provenance, license note, and claim boundary
- `data/derived/objective_observations.csv` — all 103 objective observations used for offline frontier recomputation\n- `data/derived/primary_results.csv` — the complete 23-point Pareto frontier
- `results/empirical_summary.json` — machine-readable headline results
- `scripts/fetch_and_analyze.py` — public-source rebuild and source-consistency check\n- `scripts/generate_figures.py` — dependency-free SVG figure regeneration
- `research/model.py` — reusable study-specific analysis functions
- `tests/` — behavioral and scientific-invariant tests
- `docs/` — analysis plan, data dictionary, paper blueprint, references, originality map
- `assets/` — four study-specific SVG figures

## Research integrity

This bundle distinguishes **source data**, **operationalization**, **result**, and **interpretation**. The analysis plan documents the released analysis; it is **not described as preregistered**. Public data do not automatically validate a construct, so proxy and external-validity limits are explicit.
