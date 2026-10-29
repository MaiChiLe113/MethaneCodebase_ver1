# MethaneWatch

Satellite methane plume segmentation, verification and evidence for COS40005 Project A. A target Sentinel-2 scene and up to six references go in; ranked, reviewable candidates with a verification status, an emission estimate (or an explicit reason there is none) and an attribution come out, sealed in a signed evidence dossier.

## State of this repository

This is the planned codebase, ready to divide among the team. The `diagrams/` folder and the documents under `docs/` are complete. Every source file under `src/`, `web/`, `tests/`, `infra/`, `docker/` and `scripts/` is a **placeholder**: it exists at its final path and carries a header with its purpose, the reason it exists, the requirements it covers, a proposed owner, what it may and may not import, and the names it must provide. There is no implementation yet, on purpose.

## How to start (for each member)

1. Open `docs/assignments.md` (who owns which folders and files) and `docs/work-breakdown.md` (file by file) and find yours.
2. Read the header of each file, then the diagram it points to (start with `diagrams/README.md`).
3. Create a branch, take the Jira key from the backlog, and put `MWPMWP-<n>` in every commit and in the pull request title (a pre-commit hook checks this).
4. Replace the placeholder text with code and tests, keeping to the "May import" line in the header. `make lint contracts test` must pass.

## Layout

```
diagrams/   34 LaTeX/TikZ diagrams, abstract to detailed; sources by level, rendered PDF and SVG in diagrams/output/
docs/       ADRs, requirements, assignments, work breakdown, model and dataset cards, runbook
configs/    experiments, release gates and permission matrix as data
src/methanewatch/
  core domain ports                       kernel, rules, interfaces (no I/O)
  data models training evaluation inference
  verification quantification attribution evidence
  services                                use cases
  adapters                                the only code that touches AWS, STAC, ERA5, disk
  api workers cli                         delivery
web/        React portal (talks to the API only)
tests/      unit, integration, ml, fixtures
infra/      Terraform modules (Beta scaffold)      docker/  images
scripts/    helpers          notebooks/  tutor demo only
```

## Stack in one line each

Python 3.11 with uv; PyTorch (hand-written trainer); rasterio, shapely, xarray; DVC and MLflow; Pydantic v2 config; FastAPI with a generated TypeScript client; DynamoDB and S3 (LocalStack first); SHA-256, hash-chained audit, Ed25519 signatures; React, Vite and MapLibre; pytest, hypothesis, Playwright; ruff, mypy, import-linter, pre-commit; GitHub Actions; Docker; Terraform for Beta. Reasons are in `docs/adr/`.

## Rules that must not be broken

A rate is an Estimate or an explicit Unavailable, never a bare number. Only an analyst confirms an emission, and only with complete evidence. Reviews are appended, never edited. Access is denied unless the permission matrix allows it, and refusals are audited. Synthetic data never enters the benchmark. Alpha targets are reported; the Beta gate decides promotion. See `CLAUDE.md` for the full list and the commands.
