"""src/methanewatch/training/finetune.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Entry point for fine-tuning on real data.
Why it exists  : Fine-tuning must start from a registered pretrained checkpoint and use the real
                 splits only.
Requirements   : FR2
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : models, data, evaluation, domain, ports, core; torch, mlflow through a port
Must not import: boto3, fastapi, pystac, cdsapi; services, api
To implement   : run_finetune(cfg, checkpoint)
"""
