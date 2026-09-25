# Analysis Plan

## Status
This file documents the analysis released in this repository. It is **not a preregistration** and should not be described as one.

## Primary estimand / descriptive target
What engineering alternatives remain non-dominated when cement is minimized while slump and 28-day compressive strength are maximized?

## Analysis
Parse all 103 experiments, define three explicit objectives (minimize cement; maximize slump; maximize 28-day strength), and identify an observation as Pareto-efficient only when no other observed mixture is at least as good on all three objectives and strictly better on at least one.

## Specified outputs for this release
1. source/sample size and provenance;
2. primary derived metric(s);
3. comparator, cross-group, cross-time, or frontier contrast where applicable;
4. uncertainty, sensitivity, or error information supported by the source;
5. explicit construct and external-validity limitations.

## Missingness / exclusions

The UCI dataset reports no missing values for the 103 experiments used here. All 103 rows are included as observed; no imputation or synthetic augmentation is performed.

## Interpretation boundary
This is an empirical trade-space demonstration, not a concrete design recommendation. Maximizing slump is an analytical objective here, not a universal engineering requirement; application-specific constraints, durability, cost, safety, and uncertainty are not modeled.
