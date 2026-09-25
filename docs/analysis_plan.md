# Analysis Plan

## Status
This document describes the analysis released in this repository. It is **not a preregistration**.

## Primary descriptive target
Identify the observed non-dominated alternatives when cement is minimized while slump and 28-day compressive strength are maximized.

## Secondary robustness target
Quantify how much the observed decision set changes when slump is no longer maximized and is instead omitted or used as an eligibility threshold.

## Baseline specification
Use all 103 observations. Minimize cement, maximize slump, and maximize 28-day strength. Apply pairwise Pareto dominance with weak improvement on all objectives and strict improvement on at least one.

## Sensitivity specifications
1. Minimize cement and maximize strength; slump omitted.
2. Same two objectives among observations with slump >= 10 cm.
3. Same two objectives among observations with slump >= 20 cm.

The 10 cm and 20 cm thresholds are analytical sensitivity probes. They are not asserted to be field standards.

## Prespecified release outputs
1. sample size and provenance;
2. complete baseline frontier;
3. baseline frontier fraction;
4. complete sensitivity summary;
5. overlap and Jaccard similarity relative to the baseline;
6. explicit construct and external-validity limitations;
7. reproducibility and source-drift checks.

## Missingness / exclusions
UCI reports no missing values for the 103 experiments used here. All 103 rows enter the baseline. Threshold-based sensitivity analyses exclude only observations below their declared slump cutoffs. No imputation or synthetic augmentation is used.

## Interpretation boundary
Frontier membership is conditional on the declared objectives and constraints. The study is not a field concrete-design recommendation and does not model durability, cost, safety, uncertainty, or project-specific acceptance criteria.
