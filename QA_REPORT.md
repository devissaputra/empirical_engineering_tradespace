# Final QA Report

**Release status: PASS after correction.**

## Checks completed
- provenance and source identity reviewed;
- licensing/reuse note recorded;
- derived CSV structure checked against the stated sample and estimand;
- `results/empirical_summary.json` reconciled with packaged evidence;
- README/report language reconciled with the numerical results;
- study-specific methods moved into `research/model.py`;
- tests exercise scientific logic and invariants;
- internet rebuild script has no synthetic fallback;
- four SVG assets regenerated as study-specific figures and XML-validated;
- local Markdown links checked;
- citation metadata points to the final repository slug;
- no preregistration claim is made.

## Final empirical finding
Twenty-three of 103 observed experiments (22.3%) are non-dominated under the stated three-objective rule. The frontier contains both low-cement and high-strength alternatives, so reporting a single “best” mix would hide decision-relevant trade-offs.

## Required interpretation boundary
This is an empirical trade-space demonstration, not a concrete design recommendation. Maximizing slump is an analytical objective here, not a universal engineering requirement; application-specific constraints, durability, cost, safety, and uncertainty are not modeled.
