# ADR 0005: Typed configuration from YAML

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

Experiments, release gates and the permission matrix must be reproducible and reviewable.

## Decision

Pydantic v2 models loaded from configs/*.yaml and environment variables. No other code reads os.environ.

## Consequences

A run is a file diff. Mistakes fail at load time. Cost: every new setting needs a field.

## Related

diagrams/00-context/repository-map
