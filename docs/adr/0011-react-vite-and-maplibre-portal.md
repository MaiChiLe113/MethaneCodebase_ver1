# ADR 0011: React, Vite and MapLibre portal

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

The portal is map-centred and must meet a p95 tile load of 1.5 s and a SUS of at least 75.

## Decision

React 18 and TypeScript with Vite; MapLibre GL for the map; TanStack Query for server state; Tailwind for styling. Token kept in memory.

## Consequences

Mature map library without a vendor key. Cost: bundle size and map performance need attention (lazy layers, simplified polygons).

## Related

diagrams/02-components/web-portal
