# Data Dictionary

## Source

Primary source: UCI Concrete Slump Test, DOI 10.24432/C5FG7D.

The public dataset contains mixture inputs and three measured outputs. This repository uses cement, slump, and 28 day compressive strength for the released Pareto analysis while preserving the broader source context in the packaged frontier table.

## Analysis variables

| Variable | Unit | Role | Interpretation |
|---|---|---|---|
| experiment_id | integer | Identifier | Original experiment number |
| cement | kg/m³ | Objective | Minimized in every specification |
| slump_cm | cm | Objective or eligibility variable | Maximized in baseline, thresholded or omitted in sensitivity analyses |
| strength_mpa | MPa | Objective | 28 day compressive strength, maximized |

## Source variables retained in the baseline frontier table

`data/derived/primary_results.csv` retains the source mixture information for each baseline frontier observation:

- experiment ID;
- cement;
- slag;
- fly ash;
- water;
- superplasticizer;
- coarse aggregate;
- fine aggregate;
- slump;
- flow;
- 28 day compressive strength.

These additional columns support interpretation of frontier observations but do not enter the released dominance rule unless explicitly listed above.

## Packaged files

### `data/derived/objective_observations.csv`

Complete 103 row offline input to the baseline and sensitivity analyses.

Columns:

- `experiment_id`
- `cement`
- `slump_cm`
- `strength_mpa`

### `data/derived/primary_results.csv`

Complete 23 observation baseline Pareto frontier with source mixture variables retained for interpretation.

### `data/derived/sensitivity_results.csv`

One row per decision formulation with:

- `specification`;
- `eligible_n`;
- `pareto_count`;
- `baseline_overlap_count`;
- `baseline_retention`;
- `jaccard_with_baseline`;
- exact `frontier_ids`.

### `results/empirical_summary.json`

Machine readable headline sample statistics and baseline result.

### `results/sensitivity_summary.json`

Machine readable decision formulation definitions and exact robustness results.

## Construct cautions

Cement is a material quantity, not a complete estimate of lifecycle carbon or cost.

Slump is a context dependent workability response. Larger values are treated as preferable only in the baseline specification to make the operationalization sensitivity visible.

The threshold values of 10 cm and 20 cm are analytical probes and are not universal engineering standards.
