# ADR 0001: Hexagonal monorepo with import contracts

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

The report asks for separate ingestion, AI detection, scientific verification, quantification, evidence and user services. Six people will edit the same code, and the science must be testable without a cloud account or a GPU.

## Decision

One repository. Layers: delivery, services, capabilities, rules and interfaces, kernel. Capabilities receive the outside world through Protocols in ports/; adapters implement them and are chosen only in the composition root (api/deps.py). import-linter enforces the layer order and bans boto3, fastapi, pystac and cdsapi below the adapters.

## Consequences

Members can work on their own package against fakes. A wrong import fails CI instead of a review. Cost: a little indirection (a port per outside system) and one more file to learn.

## Related

diagrams/01-containers/layers-and-dependencies, diagrams/03-code/package-dependencies
