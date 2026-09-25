# Contributing

Changes should preserve the evidence chain of the study.

## Scientific changes

If a contribution changes an objective, threshold, source variable, exclusion rule, dominance definition, or interpretation, update the relevant analysis documentation and add or revise tests.

Do not silently change the released estimand.

## Data changes

Document provenance and licensing. Do not introduce synthetic fallback data into the empirical rebuild. Update integrity hashes only when the corresponding evidence file intentionally changes.

## Code changes

Add tests for behavior that affects frontier membership, sensitivity results, source validation, or release consistency.

## Documentation changes

Keep numerical claims synchronized with machine readable outputs. Distinguish observed results from interpretation and recommendation.

## Claim discipline

Do not describe the repository as peer reviewed, preregistered, externally validated, or field validated unless that status is independently true.
