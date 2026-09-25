# Paper Blueprint

## Working title

**Objective Definition Changes the Observed Engineering Trade Space: A Reproducible Analysis of Concrete Slump Experiments**

Alternative title:

**Operationalization Sensitivity in an Observed Concrete Design Trade Space**

## Paper identity

This should be written as a compact empirical systems engineering and decision analysis paper. The strongest contribution is not a new optimization algorithm. It is the transparent demonstration that the efficient set changes materially when one engineering attribute changes role from objective to constraint or is removed from the decision model.

The manuscript should stay disciplined about scope. It analyzes observed alternatives in one public dataset. It does not claim to discover an optimal concrete formula.

## One sentence contribution

Using 103 observed laboratory mixtures, the study quantifies how Pareto frontier membership changes when workability is represented as an objective, omitted, or converted into an eligibility threshold.

## Draft abstract

Engineering trade spaces are conditional on the objectives and constraints used to define them, yet sensitivity to that formulation is often hidden once an efficient set has been computed. This study examines 103 laboratory observations from the UCI Concrete Slump Test dataset as a finite engineering trade space. The baseline analysis minimizes cement content while maximizing slump and 28 day compressive strength, producing 23 Pareto efficient observations. Three sensitivity specifications then change only the treatment of slump. Omitting slump as an objective reduces the frontier to 10 observations. Applying slump eligibility thresholds of at least 10 cm and at least 20 cm produces frontiers of 10 and 8 observations. These alternatives retain 43.5%, 43.5%, and 34.8% of the baseline frontier respectively. The results show that frontier membership is materially dependent on operationalization even when the underlying observations are unchanged. The study argues for explicit objective definition, constraint documentation, and sensitivity analysis before efficient alternatives are interpreted as decision relevant. The analysis is descriptive and does not prescribe a field concrete mixture.

## Introduction logic

### Paragraph 1: decision problem

Engineering design rarely has one objective. Material use, performance, workability, cost, environmental impact, durability, and risk can conflict. Multiobjective methods preserve those conflicts rather than hiding them inside a single score.

### Paragraph 2: specific context

Concrete mixture design is a useful setting because workability and compressive performance interact with material quantities and because prior research has used multiobjective optimization to balance competing concrete properties.

### Paragraph 3: gap

Most optimization papers emphasize how to search for good solutions. A smaller but important systems engineering question is what happens when the decision model itself changes. An observed alternative can be efficient under one formulation and dominated or ineligible under another.

### Paragraph 4: study contribution

This study isolates that issue using a small public dataset and an exact observed Pareto analysis. No surrogate model or synthetic design points are required. The analysis holds the dataset fixed and varies only the treatment of slump.

## Research questions

**RQ1.** Which observed mixtures are non dominated when cement is minimized while slump and 28 day compressive strength are maximized?

**RQ2.** How stable is that frontier when slump is removed as an objective or treated as an eligibility threshold?

## Data section

Report:

- UCI Concrete Slump Test;
- 103 laboratory experiments;
- DOI 10.24432/C5FG7D;
- CC BY 4.0;
- no synthetic augmentation;
- unit of analysis as one laboratory experiment;
- the exact variables used in the decision model;
- complete source and derived data provenance in the repository.

Explain that cement is a material intensity variable in this analysis. Do not equate it with lifecycle carbon or cost.

## Method section

### Baseline formulation

For each observation i, use three objectives:

- minimize cement;
- maximize slump;
- maximize 28 day compressive strength.

Define Pareto dominance formally. State that weak improvement is required on every objective and strict improvement on at least one.

### Sensitivity specifications

Recompute the frontier under:

1. cement and strength only;
2. cement and strength after requiring slump ≥ 10 cm;
3. cement and strength after requiring slump ≥ 20 cm.

State explicitly that the thresholds are analytical stress tests, not standards.

### Stability metrics

Report frontier size, intersection with the baseline, baseline retention, Jaccard similarity, and exact frontier IDs.

### Reproducibility

Describe the offline packaged evidence, public source rebuild, hashes, tests, and deterministic figure generation.

## Results section structure

### 1. Descriptive sample

Report n = 103, mean cement 229.89 kg/m³, mean slump 18.05 cm, mean strength 36.04 MPa, minimum cement 137.0 kg/m³, and maximum strength 58.53 MPa.

### 2. Baseline frontier

Report 23 efficient observations, 22.3% of the sample.

Use a trade space figure rather than claiming one best observation. Mention several contrasting frontier profiles to make the tradeoff concrete.

### 3. Operationalization sensitivity

Use the following table:

| Specification | Eligible n | Frontier n | Baseline retention | Jaccard |
|---|---:|---:|---:|---:|
| Three objective baseline | 103 | 23 | 1.000 | 1.000 |
| Cement and strength only | 103 | 10 | 0.435 | 0.435 |
| Slump ≥ 10 cm, then cement and strength | 84 | 10 | 0.435 | 0.435 |
| Slump ≥ 20 cm, then cement and strength | 63 | 8 | 0.348 | 0.348 |

State that each alternative frontier is a subset of the baseline frontier in this release. This explains why retention and Jaccard are numerically identical for the alternatives.

## Discussion

### Main interpretation

The efficient set is not invariant. More than half of the baseline frontier disappears when slump is no longer maximized.

### Systems engineering implication

Objective elicitation is part of model construction. A frontier should be interpreted together with the objectives, constraints, and preference assumptions that produced it.

### Decision support implication

A Pareto frontier narrows the candidate set but does not select a final design. Selection still requires application specific requirements or stakeholder preferences.

### Concrete engineering implication

The study should not be used as a mix design prescription. Real projects require additional variables such as durability, cost, embodied carbon, safety, curing regime, constituent availability, and project specific workability.

## Limitations section

Cover at least these points:

1. finite public dataset with 103 observations;
2. deterministic treatment of measured values;
3. no uncertainty model or repeated laboratory measurements;
4. cement is not a complete environmental or economic metric;
5. slump is context dependent;
6. no causal claims;
7. no generation of new candidate mixtures;
8. external validity is limited to the observed dataset and declared decision rules.

## Figures

**Figure 1. Observed engineering trade space.** Cement on the horizontal axis, 28 day strength on the vertical axis, slump encoded by bubble size, and baseline frontier members visually distinguished.

**Figure 2. Reproducible analysis pipeline.** Public source, validation, objective table, baseline frontier, sensitivity specifications, stability metrics, and bounded interpretation.

**Figure 3. Sensitivity of frontier size and baseline retention.**

## Tables

**Table 1.** Dataset and variable definitions.

**Table 2.** Baseline and sensitivity decision formulations.

**Table 3.** Headline results and stability metrics.

**Optional appendix table.** Exact frontier experiment IDs for every specification.

## Literature positioning

Use the cited literature for two limited purposes:

- establish that concrete mixture design is naturally multiobjective;
- distinguish search based optimization of generated candidate solutions from this repository's observed alternative sensitivity analysis.

Do not claim novelty simply because a method has not been seen in a small literature search. Phrase the contribution as the specific transparent empirical framing implemented here.

## Writing rules

- Use “observed Pareto efficient alternatives,” not “optimal concrete designs.”
- Use “sensitivity threshold,” not “required slump.”
- Use “secondary analysis,” not “experiment conducted by the author.”
- Distinguish dataset facts from interpretation.
- Keep all numerical claims synchronized with machine readable outputs.
- Do not describe the work as preregistered, peer reviewed, or externally validated unless that later becomes true.

## Completion checklist

A manuscript draft is ready for external feedback when:

- every number can be traced to a released table or JSON file;
- the method section reproduces the exact code logic;
- figures are regenerated from the packaged data;
- references are verified against DOI or publisher records;
- limitations are explicit;
- the abstract does not overstate the contribution;
- repository commit or release tag is cited in the manuscript.
