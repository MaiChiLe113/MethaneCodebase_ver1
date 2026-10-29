# ADR 0012: Synthetic data as recipes; never in the benchmark

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

One million synthetic samples would take about 310 GB; the advisor rule says synthetic data must not enter the benchmark.

## Decision

Store recipes (parquet) and rebuild samples on the fly (about 1.5 ms each); about 20 GB. A test asserts that no synthetic id appears in the benchmark split. Licence note: MethaneSET and the MARS-S2L weights are CC BY-NC-SA 4.0.

## Consequences

Cheap to store, deterministic, honest benchmark. Cost: determinism must be proven by a test.

## Related

diagrams/05-data/synthetic-recipe-flow, diagrams/05-data/split-policy
