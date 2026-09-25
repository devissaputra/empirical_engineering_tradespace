# Scientific Report

## Empirical Engineering Design Trade Space: Concrete Slump Experiments

### Executive summary

This repository studies a narrow but important systems engineering question: how much does the observed set of efficient engineering alternatives depend on the way objectives and constraints are defined?

The analysis uses all 103 laboratory experiments in the UCI Concrete Slump Test dataset. The baseline formulation minimizes cement content while maximizing slump and 28 day compressive strength. Under that formulation, 23 of 103 observed mixtures are Pareto efficient. The project then changes only the treatment of slump. When slump is removed as an objective, the efficient set contracts to 10 observations. When slump is instead used as an eligibility threshold of at least 10 cm or at least 20 cm, the efficient set contains 10 and 8 observations respectively.

The central result is therefore not a recommended concrete mixture. It is an empirical demonstration that frontier membership is conditional on the decision model. In this dataset, changing the role of workability removes more than half of the baseline frontier. This makes objective definition and sensitivity analysis part of the engineering decision problem rather than a cosmetic modeling choice.

### Research questions

1. Which observed mixtures are non dominated when cement is minimized while slump and 28 day compressive strength are maximized?
2. How stable is that observed frontier when slump is removed as an objective or represented as an eligibility constraint?

### Data source and provenance

The study uses the UCI Concrete Slump Test dataset created by I Cheng Yeh. UCI reports 103 instances, no missing values, DOI 10.24432/C5FG7D, and a CC BY 4.0 license.

The repository does not depend on synthetic observations. The internet enabled rebuild downloads the public source, calculates a SHA 256 digest of the retrieved bytes, recomputes the released headline metrics, and checks the exact baseline frontier IDs. The packaged objective table and sensitivity table are also protected by hashes recorded in `data/source_manifest.json`.

### Unit of analysis

One laboratory concrete mixture experiment.

### Variables used in the decision model

| Variable | Role in this study | Direction |
|---|---|---|
| Cement, kg/m³ | Material intensity proxy within this dataset | Minimize |
| Slump, cm | Workability related observed response | Maximize in baseline only |
| 28 day compressive strength, MPa | Mechanical performance response | Maximize |

Cement content is not treated as a complete cost or embodied carbon measure. Slump is not assumed to be universally better when larger. Those limitations motivate the sensitivity analysis.

### Baseline decision rule

For two observed alternatives a and b, a dominates b when a uses no more cement, has no lower slump, and has no lower 28 day strength, with strict improvement on at least one of those dimensions.

The baseline Pareto frontier contains every observation for which no other observed experiment satisfies that dominance rule.

### Baseline results

| Metric | Value |
|---|---:|
| Experiments | 103 |
| Mean cement | 229.89 kg/m³ |
| Mean slump | 18.05 cm |
| Mean 28 day strength | 36.04 MPa |
| Maximum observed strength | 58.53 MPa |
| Minimum observed cement | 137.0 kg/m³ |
| Pareto efficient observations | 23 |
| Pareto fraction | 22.3% |

The frontier contains qualitatively different profiles rather than one obvious winner. For example, experiment 35 combines the minimum observed cement content on the frontier, 137 kg/m³, with 27.5 cm slump and 34.45 MPa strength. Experiment 49 reaches the maximum observed strength, 58.53 MPa, but uses 332 kg/m³ cement and has 0 cm slump. Experiment 103 combines 29 cm slump with 48.77 MPa strength at 348.7 kg/m³ cement. These examples show why collapsing the problem into a single unreported weighting scheme would hide meaningful tradeoffs.

### Sensitivity analysis

Three alternative operationalizations were evaluated.

| Specification | Eligible n | Frontier n | Baseline retained | Jaccard vs baseline |
|---|---:|---:|---:|---:|
| Baseline: minimize cement, maximize slump and strength | 103 | 23 | 100.0% | 1.000 |
| Minimize cement and maximize strength, omit slump | 103 | 10 | 43.5% | 0.435 |
| Same two objectives, require slump ≥ 10 cm | 84 | 10 | 43.5% | 0.435 |
| Same two objectives, require slump ≥ 20 cm | 63 | 8 | 34.8% | 0.348 |

All three alternative frontiers are subsets of the baseline frontier in this release. That is why baseline retention and Jaccard similarity have the same numerical values for the alternatives.

The result is substantively important. More than half of the baseline efficient set disappears when workability is no longer maximized. A systems engineering interpretation should therefore treat the frontier as conditional evidence under a declared decision formulation, not as an intrinsic property of the mixtures.

### Relation to prior work

Concrete mixture design is commonly framed as a multiobjective problem because strength, workability, cost, environmental impact, durability, and material quantities can conflict. Prior studies have combined machine learning with multiobjective optimization to search for candidate mixture designs. This repository takes a deliberately smaller empirical route. It does not train a predictive surrogate and does not generate new mixtures. It asks what can be learned from the finite set of observed laboratory alternatives, then stress tests that answer against alternative formulations of workability.

That distinction is the main methodological value of the project. The study is closer to an observed alternative trade study than to a concrete optimization engine.

### Threats to validity

**Construct validity.** Cement content is only one material quantity and is not equivalent to lifecycle carbon, cost, or environmental burden. Slump is a context dependent workability measure rather than a universal utility scale.

**Internal validity.** The analysis is deterministic and descriptive. It does not estimate causal effects. Frontier membership follows directly from measured values and the declared dominance rule.

**Measurement uncertainty.** The released analysis treats recorded measurements as exact. Replicate uncertainty, laboratory measurement error, and uncertainty intervals are not available in the packaged decision model.

**External validity.** The 103 experiments do not represent every concrete family, climate, structural application, curing regime, material supply chain, or construction practice.

**Decision validity.** A field design would normally include additional requirements such as durability, safety margins, cost, embodied carbon, constructability, codes, and project specific workability ranges.

### Reproducibility

Offline verification:

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
python scripts/run_sensitivity.py --check
```

Public source rebuild:

```bash
python scripts/fetch_and_analyze.py --check
```

Figure regeneration:

```bash
python scripts/generate_figures.py
```

### Research integrity statement

This is a secondary analysis of a public dataset. It is not preregistered, peer reviewed, externally validated, or based on original data collection. The repository separates source provenance, analysis code, derived evidence, sensitivity analysis, interpretation, and QA so that readers can inspect where each claim comes from.
