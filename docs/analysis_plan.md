# Analysis Plan

## Status

This document records the released analysis. It is not a preregistration.

## Decision problem

The study treats the 103 laboratory experiments as a finite set of observed engineering alternatives. The objective is not to predict unobserved mixtures but to identify which observed alternatives remain non dominated under declared decision formulations.

## Primary estimand

The exact set of experiment IDs on the observed Pareto frontier when:

- cement is minimized;
- slump is maximized;
- 28 day compressive strength is maximized.

Secondary summaries are frontier size and frontier fraction.

## Robustness estimands

For each alternative treatment of slump, estimate:

- eligible sample size;
- exact frontier IDs;
- frontier size;
- overlap with the baseline;
- baseline retention;
- Jaccard similarity.

## Baseline specification

Use all 103 observations. No weighting, normalization, imputation, synthetic augmentation, or learned surrogate is used for frontier membership.

Dominance requires weak improvement on all declared objectives and strict improvement on at least one.

## Sensitivity specifications

1. Minimize cement and maximize strength with slump omitted.
2. Apply the same two objectives to observations with slump ≥ 10 cm.
3. Apply the same two objectives to observations with slump ≥ 20 cm.

The thresholds are stress tests of decision formulation, not field standards.

## Missingness and exclusions

All 103 observations enter the baseline. Threshold analyses exclude only observations below the declared cutoff. No other exclusion is applied.

## Released outputs

The release must contain:

1. source identity, DOI, license, and retrieval metadata;
2. complete objective table;
3. exact baseline frontier;
4. complete sensitivity summary;
5. machine readable results;
6. data integrity hashes;
7. reproducible code and tests;
8. scientific figures generated from packaged evidence;
9. explicit validity and claim boundaries.

## Interpretation constraints

A Pareto efficient observation is not automatically recommended. The study cannot infer stakeholder utility or field suitability from frontier membership alone.

Cement is not treated as a complete estimate of cost or embodied carbon. Slump is not treated as universally preferable at larger values outside the baseline stress test.

## Change control

Any future change to an objective, threshold, source variable, exclusion rule, or dominance definition should be documented as a new analysis version rather than silently replacing the released formulation.
