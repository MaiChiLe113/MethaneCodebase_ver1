"""src/methanewatch/training/optim.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Optimiser and scheduler factories.
Why it exists  : Keeps hyper-parameters in YAML.
Requirements   : FR2
Stage          : Alpha
Proposed owner : Hai (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : models, data, evaluation, domain, ports, core; torch, mlflow through a port
Must not import: boto3, fastapi, pystac, cdsapi; services, api
To implement   : build_optimizer(model, cfg), build_scheduler(opt, cfg)
"""
