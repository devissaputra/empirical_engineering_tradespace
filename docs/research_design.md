# Research Design

## Research question
What engineering alternatives remain non-dominated when cement is minimized while slump and 28-day compressive strength are maximized?

## Design
Secondary multi-objective analysis of 103 laboratory mixture experiments.

## Source and unit of analysis
Source: UCI Concrete Slump Test. The operational unit follows the public dataset and is documented in `data/source_manifest.json` and `docs/data_dictionary.md`.

## Hypotheses
1. H1: the observed design space contains multiple non-dominated mixtures rather than one universally best mixture.
2. H2: low-cement and high-strength alternatives occupy different parts of the frontier, demonstrating a genuine engineering trade-off.

## Method
Parse all 103 experiments, define three explicit objectives (minimize cement; maximize slump; maximize 28-day strength), and identify an observation as Pareto-efficient only when no other observed mixture is at least as good on all three objectives and strictly better on at least one.

## Validity boundary
This is an empirical trade-space demonstration, not a concrete design recommendation. Maximizing slump is an analytical objective here, not a universal engineering requirement; application-specific constraints, durability, cost, safety, and uncertainty are not modeled.
