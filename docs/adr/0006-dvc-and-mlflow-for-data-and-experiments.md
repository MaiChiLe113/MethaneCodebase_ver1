# ADR 0006: DVC and MLflow for data and experiments

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

Every model must trace back to exact data, code and settings (report MLOps scope).

## Decision

DVC versions recipes, splits and manifests; MLflow records runs, metrics and the model registry (which version is approved).

## Consequences

Reproducibility and an auditable promotion. Cost: two more tools for the team to learn.

## Related

diagrams/06-mlops/lifecycle
