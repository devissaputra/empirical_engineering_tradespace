# Paper Blueprint

## Working title
Empirical Engineering Design Trade Space: Concrete Slump Experiments

## Motivation
Engineering design decisions are often multi-objective: improving one performance dimension can consume more material or degrade another. The concrete slump experiments provide observed alternatives on which an explicit Pareto rule can be evaluated without inventing a weighted score.

## Research question
What engineering alternatives remain non-dominated when cement is minimized while slump and 28-day compressive strength are maximized?

## Data and method
Parse all 103 experiments, define three explicit objectives (minimize cement; maximize slump; maximize 28-day strength), and identify an observation as Pareto-efficient only when no other observed mixture is at least as good on all three objectives and strictly better on at least one.

## Results to report
Twenty-three of 103 observed experiments (22.3%) are non-dominated under the stated three-objective rule. The frontier contains both low-cement and high-strength alternatives, so reporting a single “best” mix would hide decision-relevant trade-offs. Report the packaged headline metrics and the full relevant derived table; do not cherry-pick only the strongest contrast.

## Robustness / sensitivity
The released frontier is computed from all 103 observed mixtures using one declared three-objective rule: minimize cement while maximizing slump and 28-day strength. Every reported frontier point is checked for pairwise non-domination. Adding flow, cost, durability, uncertainty, or application-specific constraint thresholds would define a different trade space and should be reported as a separate sensitivity analysis.

## Limitations
This is an empirical trade-space demonstration, not a concrete design recommendation. Maximizing slump is an analytical objective here, not a universal engineering requirement; application-specific constraints, durability, cost, safety, and uncertainty are not modeled.

## Publication integrity
Do not describe this repository as peer reviewed, preregistered, or externally validated unless those events actually occur. Distinguish analysis of public data from original data collection.
