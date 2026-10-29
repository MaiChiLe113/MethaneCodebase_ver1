"""src/methanewatch/inference/predictor.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Load an approved model and predict logits for a scene stack, tile by tile.
Why it exists  : One predictor for the worker, the CLI and the benchmark.
Requirements   : FR2, NFR1
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : models, data, domain, ports, core; torch
Must not import: boto3, fastapi, pystac, cdsapi; services, api
To implement   : Predictor(model).predict(stack) -> Raster
"""
