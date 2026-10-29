# ADR 0014: Diagrams as LaTeX and TikZ

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

The team wants diagrams reviewed in pull requests, in the same toolchain as the report.

## Decision

Each diagram is a standalone .tex file using diagrams/_common/mwstyle.tex; a Makefile builds PDF and SVG into the single folder diagrams/output/. Rendered files are committed so people without TeX can read them.

## Consequences

Diffable, consistent style. Cost: a TeX Live installation is needed to change a diagram.

## Related

diagrams/README.md
