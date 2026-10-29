# ADR 0008: Authentication behind a port

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

Alpha needs real sign-in without paying for a managed identity service; Beta may use Cognito.

## Decision

AuthProvider is a port. Alpha adapter: JWT with argon2 password hashes. Beta adapter: Amazon Cognito. Token lifetime and refresh are open and decided in sprint 1.

## Consequences

The API and RBAC do not change when the provider does. Cost: two adapters to test.

## Related

diagrams/04-behaviour/seq-login-rbac
