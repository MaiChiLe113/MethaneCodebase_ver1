# ADR 0002: Python 3.11, uv, extras

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

tacoreader supports Python 3.10 to 3.13. Some members work on a Mac without CUDA, one on a Windows PC with a GPU.

## Decision

Python 3.11 (range 3.11 to 3.13 allowed). uv manages the environment. Optional extras: ml, api, dev, mamba, so the API image does not carry PyTorch.

## Consequences

Small images and fast CI for the web tier. Cost: members must remember to pass --extra flags; the Makefile does it.

## Related

diagrams/01-containers/deployment-local
