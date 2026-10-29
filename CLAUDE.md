# CLAUDE.md

Guidance for Claude Code and for new team members working in this repository.

## What this is

MethaneWatch (COS40005 Project A). Hexagonal Python monorepo plus a React portal. Read `README.md`, then `diagrams/README.md`, then `docs/work-breakdown.md`.

## Current state

Source files are placeholders: a header, no implementation. When asked to implement a file, read its header first, keep to its "May import" and "Must not import" lines, implement only the names under "To implement", and add the test named in `docs/requirements.md`. Do not move files or add packages without an ADR.

## Architecture rules (checked by `make contracts`)

Layers, high to low: api/workers/cli, services, training, inference and evaluation, capabilities (models, verification, quantification, attribution, evidence), data, ports, domain, core. A layer may import only layers below it. domain, ports and all capabilities must not import boto3, fastapi, pystac or cdsapi. adapters must not import services, api, workers or cli. Adapters are chosen only in `api/deps.py` (the composition root). web/ talks to the API over HTTP only.

## Hard constraints from the report

1. An emission rate is an Estimate (with range, wind source and version) or Unavailable or Uncertain with a reason. Never return a bare number.
2. The system proposes a status; only an analyst sets it. An emission is confirmed only when the analyst sets Supported and the evidence is complete. Uncertain must never be shown as Confirmed.
3. Reviews are appended, never edited. Every review, status change, export and denied request creates an audit entry.
4. Access is deny by default from `configs/permissions.yaml`; the portal only hides what the API would refuse.
5. Synthetic data never enters the benchmark. Final scores come from the real test split only.
6. Alpha targets (IoU 0.70, F1 0.75) are reported. The Beta gate (F1 0.80, FPR below 0.03 percent) controls promotion. Do not merge them.
7. Integrity (hashes, signatures) is not scientific correctness. Keep evidence/ separate from verification/.
8. Commits and pull request titles carry `MWPMWP-<n>`. Pull requests follow the Definition of Done in report Section 7.4 and need a peer review.

## Commands

`make setup` (environment and hooks), `make lint`, `make contracts`, `make test` (no cloud, no GPU), `make test-ml` (model shapes on CPU), `make api`, `make web-dev`, `make up` (local stack), `make diagrams`.

## Where things are decided

Design in `docs/adr/` (Proposed until the team agrees), requirements in `docs/requirements.md`, who owns what in `docs/assignments.md` (by person) and `docs/work-breakdown.md` (by file), numeric gates in `configs/release_gates.yaml`, permissions in `configs/permissions.yaml`.
