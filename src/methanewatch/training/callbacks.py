"""src/methanewatch/training/callbacks.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Checkpointing, early stopping, MLflow logging.
Why it exists  : Experiment tracking is required for reproducibility.
Requirements   : FR2, NFR5
Stage          : Alpha
Proposed owner : Hai (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : models, data, evaluation, domain, ports, core; torch, mlflow through a port
Must not import: boto3, fastapi, pystac, cdsapi; services, api
To implement   : Checkpoint, EarlyStopping, MlflowLogger
"""
