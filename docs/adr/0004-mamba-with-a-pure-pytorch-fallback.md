# ADR 0004: Mamba with a pure PyTorch fallback

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

mamba-ssm needs CUDA; the laptop has none, yet three Mamba models and ST-CM-UNet are in the benchmark.

## Decision

models/mamba/scan_fallback.py implements the selective scan in PyTorch. mamba-ssm is an optional extra used when CUDA is available. A test checks that both give close results on a small input.

## Consequences

Everyone can run and unit-test the Mamba models. Cost: the fallback is slow and must never be used for the reported benchmark.

## Related

diagrams/03-code/model-zoo
