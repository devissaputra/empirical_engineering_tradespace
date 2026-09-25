# Empirical Study Protocol

## Study
Empirical Engineering Design Trade Space: Concrete Slump Experiments

## Research questions
1. Which observed alternatives are non-dominated when cement is minimized while slump and 28-day compressive strength are maximized?
2. How stable is that decision set when slump is removed as an objective or treated as an eligibility threshold?

## Design and source
Secondary multi-objective analysis of 103 laboratory mixture experiments from the UCI Concrete Slump Test dataset. Analysis/retrieval date: 2026-09-25.

## Primary operationalization
The baseline minimizes cement and maximizes both slump and 28-day compressive strength. An observation is Pareto-efficient only when no other observed mixture is at least as good on all three objectives and strictly better on at least one.

## Sensitivity operationalizations
Three alternative specifications test dependence on the treatment of slump:

1. minimize cement and maximize strength, with slump omitted as an objective;
2. the same two objectives among observations with slump >= 10 cm;
3. the same two objectives among observations with slump >= 20 cm.

The two thresholds are analytical robustness probes, not universal design requirements.

## Primary empirical result
Twenty-three of 103 observed experiments (22.3%) are non-dominated under the baseline rule.

## Sensitivity result
The baseline frontier is not invariant to the operationalization of slump. Omitting slump as an objective yields a 10-point frontier with 43.5% retention of the baseline frontier. Requiring slump >= 10 cm also yields 10 points with 43.5% baseline retention. Requiring slump >= 20 cm yields 8 points with 34.8% baseline retention.

## Interpretation
The sensitivity result strengthens the study's engineering-management interpretation: a trade space is partly defined by its objectives and constraints. The analysis therefore reports a decision set conditional on declared preferences rather than a universal optimum.

## Validity and claim boundary
This is an empirical trade-space demonstration, not a concrete design recommendation. Durability, cost, safety, uncertainty, curing conditions, and project-specific workability targets are not modeled.

## Reproducibility status
The repository packages the complete objective table, the baseline frontier, deterministic sensitivity outputs, study-specific analysis functions, an internet-enabled source rebuild, evidence hashes, and tests for computational and scientific invariants. The released analysis was documented after dataset selection and must not be represented as preregistered.
