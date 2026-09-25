# Research Design

## Design summary

This is a secondary empirical trade study over a finite set of observed laboratory alternatives. It combines exact Pareto dominance with operationalization sensitivity analysis.

## Unit of analysis

One UCI Concrete Slump Test laboratory experiment.

## Research questions

1. Which observed alternatives are non dominated under a three objective formulation of cement, slump, and 28 day strength?
2. How much does frontier membership change when the role of slump changes?

## Conceptual model

The study separates four layers:

1. **Evidence layer:** observed laboratory measurements.
2. **Decision model layer:** declared objectives and eligibility rules.
3. **Computation layer:** exact Pareto dominance over eligible observations.
4. **Interpretation layer:** bounded decision support conclusions.

This separation is important because the same evidence can produce a different frontier when the decision model changes.

## Baseline objectives

| Variable | Direction | Interpretation |
|---|---|---|
| Cement | Minimize | Lower material quantity on this dimension |
| Slump | Maximize | Baseline workability preference used for stress testing |
| 28 day strength | Maximize | Higher measured compressive performance |

## Sensitivity logic

Higher slump is not universally preferable. The study therefore tests three alternative formulations:

- omit slump from the objectives;
- require slump ≥ 10 cm and optimize cement plus strength;
- require slump ≥ 20 cm and optimize cement plus strength.

## Stability metrics

Each alternative is compared with the baseline using:

- frontier size;
- overlap count;
- baseline retention;
- Jaccard similarity;
- exact frontier membership.

## Inference scope

The analysis supports descriptive statements about the named dataset under the declared formulations.

It does not support:

- causal inference;
- prediction for unobserved mixtures;
- universal concrete design recommendations;
- a claim that cement alone measures cost or carbon;
- a claim that larger slump is always better.

## Threats to validity

**Construct validity:** objectives are simplified representations of engineering concerns.

**Measurement validity:** recorded laboratory values are treated as exact because replicate uncertainty is not modeled.

**External validity:** results may not transfer to other mixture families, constituent sources, environmental conditions, or project requirements.

**Decision validity:** additional constraints and stakeholder preferences are required before field selection.

## Research integrity

The source dataset, analysis rules, outputs, code, and limitations are version controlled. The analysis plan documents the released study after dataset selection and must not be described as preregistration.
