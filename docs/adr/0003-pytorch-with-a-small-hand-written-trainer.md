# ADR 0003: PyTorch with a small hand-written trainer

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

Eight models share one interface and the team needs to understand every line of training for the report and the tutor demo.

## Decision

Plain PyTorch and a short training/trainer.py (epochs, mixed precision, resume) instead of a training framework. Experiment tracking through MLflow callbacks.

## Consequences

Easy to audit and to run on CPU for tests. Cost: we maintain a few features a framework would give for free.

## Related

diagrams/03-code/model-zoo, diagrams/02-components/ml-pipeline
