# Data Provenance and Derived Evidence

## Public source

This repository uses the UCI Concrete Slump Test dataset.

- Creator: I Cheng Yeh
- Instances: 103
- Dataset DOI: 10.24432/C5FG7D
- License reported by UCI: CC BY 4.0
- Retrieval used for this release: 25 September 2026

The repository does not silently republish the complete raw UCI file as if it were original data.

## Packaged analysis evidence

### `derived/objective_observations.csv`

Complete 103 row table containing the exact variables used to recompute every released frontier offline.

### `derived/primary_results.csv`

Complete 23 observation baseline frontier. This table keeps the source mixture variables so that frontier points can be inspected rather than reduced to IDs only.

### `derived/sensitivity_results.csv`

Complete summary of the four decision formulations, including eligible sample size, frontier size, overlap, retention, Jaccard similarity, and exact frontier IDs.

## Integrity

`source_manifest.json` records:

- source identity;
- dataset DOI;
- source page and direct data endpoint;
- license note;
- release retrieval date;
- whether raw data are redistributed;
- SHA 256 hashes for the packaged objective and sensitivity tables;
- the claim boundary.

The public source rebuild also computes and prints the SHA 256 digest of the downloaded source bytes.

## Evidence policy

No synthetic fallback is used. If the public source cannot be fetched, the online rebuild should fail rather than silently substitute generated data.

The offline package remains independently verifiable from the committed derived evidence.
