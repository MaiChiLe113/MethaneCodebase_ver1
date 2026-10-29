"""src/methanewatch/training/losses.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Segmentation losses chosen by config (for example BCE with Dice).
Why it exists  : Class imbalance is severe (plumes are few pixels); the loss choice is a main
                 experiment variable.
Requirements   : FR2
Stage          : Alpha
Proposed owner : Hai (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : models, data, evaluation, domain, ports, core; torch, mlflow through a port
Must not import: boto3, fastapi, pystac, cdsapi; services, api
To implement   : build_loss(cfg)
"""
