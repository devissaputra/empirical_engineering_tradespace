# Empirical Study Protocol

## Study title

**Empirical Engineering Design Trade Space: Concrete Slump Experiments**

## Study type

Secondary, deterministic, multiobjective analysis of a public laboratory dataset.

This document records the released protocol. It is not a preregistration.

## Research questions

**RQ1.** Which observed mixtures are non dominated when cement is minimized while slump and 28 day compressive strength are maximized?

**RQ2.** How much does the observed efficient set change when slump is removed as an objective or represented as an eligibility threshold?

## Data

Source: UCI Concrete Slump Test, DOI 10.24432/C5FG7D.

Unit of analysis: one laboratory mixture experiment.

Released sample: all 103 observations.

Missingness: no imputation is used. The baseline includes all 103 observations.

## Baseline operationalization

For observation i, define the objective vector as:

- minimize cement content;
- maximize slump;
- maximize 28 day compressive strength.

Observation a dominates observation b when a is no worse than b on all three objectives and strictly better on at least one.

The baseline estimand is the set of observed experiment IDs that are not dominated under this rule.

## Sensitivity operationalizations

The analysis then changes the role of slump while leaving the observed data unchanged.

1. Minimize cement and maximize strength; omit slump from the objective vector.
2. Apply the same two objectives after restricting eligibility to slump ≥ 10 cm.
3. Apply the same two objectives after restricting eligibility to slump ≥ 20 cm.

The thresholds are robustness probes. They are not asserted to be universal engineering requirements.

## Comparison metrics

For each specification the release reports:

- eligible sample size;
- frontier size;
- overlap count with the baseline frontier;
- baseline retention, defined as overlap divided by baseline frontier size;
- Jaccard similarity, defined as intersection divided by union;
- exact frontier experiment IDs.

## Released findings

The baseline frontier contains 23 of 103 observations, or 22.3%.

The alternative frontiers contain 10, 10, and 8 observations. They retain 43.5%, 43.5%, and 34.8% of the baseline frontier respectively.

## Interpretation rule

The project treats Pareto efficiency as conditional on the declared decision model. It does not convert frontier membership into a recommendation without an additional preference model and application specific constraints.

## Validity boundaries

The model does not include cost, lifecycle carbon, durability, safety factors, measurement uncertainty, curing conditions, constructability, codes, or stakeholder utility.

Cement content is not equivalent to carbon or cost. Slump is context dependent and is intentionally stress tested rather than assumed to be a universal utility dimension.

The analysis describes observed alternatives only. It does not generate new mixtures, fit a predictive surrogate, or estimate causal effects.

## Reproducibility

The repository packages the complete objective table, exact baseline frontier, sensitivity outputs, analysis functions, public source rebuild, integrity hashes, tests, and deterministic figure generation.

The scientific report in `REPORT.md` is the primary narrative interpretation of this protocol.
