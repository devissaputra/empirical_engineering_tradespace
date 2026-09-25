# Paper Blueprint

## Working title
Operationalization-Sensitive Trade-Space Analysis of Concrete Slump Experiments

## Motivation
Engineering trade spaces do not exist independently of the objectives used to define them. A design can appear non-dominated under one preference structure and disappear from the frontier under another. The UCI Concrete Slump Test dataset provides 103 observed laboratory alternatives that allow this dependence to be examined transparently without generating synthetic design points.

## Research questions
1. Which observed mixtures are non-dominated when cement is minimized while slump and 28-day strength are maximized?
2. How stable is that frontier when slump is omitted as an objective or treated as an eligibility threshold?

## Data
UCI Concrete Slump Test, 103 experiments. Dataset DOI: 10.24432/C5FG7D.

## Method
The primary analysis computes the exact observed Pareto frontier for three objectives. Sensitivity analyses recompute frontiers under three alternative specifications and compare frontier membership using overlap, retention, and Jaccard similarity.

## Results to report
- baseline frontier: 23 of 103 observations (22.3%);
- cement + strength only: 10 frontier points, 43.5% baseline retention;
- cement + strength with slump >= 10 cm: 10 frontier points, 43.5% retention;
- cement + strength with slump >= 20 cm: 8 frontier points, 34.8% retention.

## Interpretation
The main methodological result is not that one concrete mixture is best. It is that the observed efficient set depends materially on how workability is represented in the decision model. This supports an engineering-management argument for explicit objective elicitation and sensitivity analysis before design alternatives are ranked or selected.

## Limitations
The analysis is descriptive and secondary. It does not model cost, embodied carbon, durability, uncertainty, curing conditions, field constructability, or stakeholder utility. The slump thresholds are analytical probes rather than standards.

## Publication integrity
Do not describe this repository as peer reviewed, preregistered, externally validated, or based on original data collection unless those events actually occur.
