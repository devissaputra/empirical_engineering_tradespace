# Research Design

## Research questions
1. Which observed alternatives remain non-dominated when cement is minimized while slump and 28-day compressive strength are maximized?
2. How sensitive is that observed decision set to alternative treatment of slump?

## Design
Secondary multi-objective analysis of 103 laboratory mixture experiments from the UCI Concrete Slump Test dataset.

## Unit of analysis
One laboratory mixture experiment.

## Baseline objectives
- minimize cement;
- maximize slump;
- maximize 28-day compressive strength.

## Sensitivity logic
Because higher slump is not universally preferable, the study evaluates whether the baseline frontier is robust to three alternative operationalizations:
- omit slump and optimize only cement and strength;
- require slump >= 10 cm, then optimize cement and strength;
- require slump >= 20 cm, then optimize cement and strength.

These thresholds are analytical stress tests, not universal engineering standards.

## Robustness metrics
Each alternative specification reports:
- eligible sample size;
- Pareto-frontier size;
- overlap count with the baseline frontier;
- baseline retention fraction;
- Jaccard similarity with the baseline frontier.

## Validity boundary
The results describe this dataset under declared objectives and constraints. They do not establish a field-ready concrete mix, causal effects, or universal preference ordering. Durability, cost, safety, uncertainty, curing conditions, and project-specific acceptance criteria are outside the model.
