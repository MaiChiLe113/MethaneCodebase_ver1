# ADR 0013: Alpha targets and the Beta gate are different things

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

The report gives IoU 0.70 and F1 0.75 as Alpha targets, and F1 0.80 with FPR below 0.03 percent as the Beta promotion gate.

## Decision

Both live in configs/release_gates.yaml under separate keys. evaluation/gates.py implements the Beta gate as a tested function; Alpha targets are reported only. The registry refuses to approve a model that fails the gate.

## Consequences

No confusion between a research result and permission to serve users.

## Related

diagrams/06-mlops/release-gate
