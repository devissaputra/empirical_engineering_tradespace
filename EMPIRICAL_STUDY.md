# Empirical Study Protocol

## Study
Empirical Engineering Design Trade Space: Concrete Slump Experiments

## Research question
What engineering alternatives remain non-dominated when cement is minimized while slump and 28-day compressive strength are maximized?

## Design and source
Secondary multi-objective analysis of 103 laboratory mixture experiments. Source: UCI Concrete Slump Test. Analysis/retrieval date: 2026-09-25.

## Hypotheses
1. H1: the observed design space contains multiple non-dominated mixtures rather than one universally best mixture.
2. H2: low-cement and high-strength alternatives occupy different parts of the frontier, demonstrating a genuine engineering trade-off.

## Operationalization and method
Parse all 103 experiments, define three explicit objectives (minimize cement; maximize slump; maximize 28-day strength), and identify an observation as Pareto-efficient only when no other observed mixture is at least as good on all three objectives and strictly better on at least one.

## Primary empirical result
Twenty-three of 103 observed experiments (22.3%) are non-dominated under the stated three-objective rule. The frontier contains both low-cement and high-strength alternatives, so reporting a single “best” mix would hide decision-relevant trade-offs.

## Validity and claim boundary
This is an empirical trade-space demonstration, not a concrete design recommendation. Maximizing slump is an analytical objective here, not a universal engineering requirement; application-specific constraints, durability, cost, safety, and uncertainty are not modeled.

## Reproducibility status
The repository packages derived results, study-specific analysis functions, deterministic or seeded procedures where relevant, an internet-enabled source rebuild script, and tests for both computations and critical scientific invariants. The released analysis was documented after dataset selection and should not be represented as preregistered.
