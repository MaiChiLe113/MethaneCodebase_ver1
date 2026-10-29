"""src/methanewatch/training/trainer.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Small hand-written training loop: epochs, mixed precision, gradient clipping,
                 resume.
Why it exists  : A hand-written loop is shorter to audit than a framework and works on CPU and
                 CUDA.
Requirements   : FR2, NFR5
Stage          : Alpha
Proposed owner : Hai (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : models, data, evaluation, domain, ports, core; torch, mlflow through a port
Must not import: boto3, fastapi, pystac, cdsapi; services, api
To implement   : Trainer(model, loaders, cfg).fit()
"""
