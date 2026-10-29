"""src/methanewatch/models/sam4ch4/model.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Zero-shot SAM-based reference wrapper (inference only).
Why it exists  : Reports what a general segmentation model does without methane training.
Requirements   : FR2
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, core; torch (mamba-ssm optional)
Must not import: data, training, evaluation; boto3, fastapi, pystac, cdsapi
To implement   : Sam4Ch4Model
"""
