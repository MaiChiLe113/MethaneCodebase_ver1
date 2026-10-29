# ADR 0007: FastAPI with a generated TypeScript client

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

The portal and the API are built by different people at the same time.

## Decision

FastAPI with Pydantic schemas is the API contract. scripts/export_openapi.py writes the OpenAPI JSON; scripts/gen_ts_client.sh generates web/src/api/client.ts. The portal develops against a mock of that contract.

## Consequences

Front and back can proceed in parallel and cannot drift apart silently. Cost: regenerate the client after each contract change.

## Related

diagrams/02-components/api-service, diagrams/02-components/web-portal
