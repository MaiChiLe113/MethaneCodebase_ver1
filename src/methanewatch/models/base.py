"""src/methanewatch/models/base.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : SegmentationModel Protocol: forward(x, ref_valid) -> logits (B,1,100,100).
Why it exists  : One interface for eight candidates so the comparison is fair; see
                 diagrams/03-code/model-zoo.
Requirements   : FR2
Stage          : Alpha
Proposed owner : Hai (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, core; torch (mamba-ssm optional)
Must not import: data, training, evaluation; boto3, fastapi, pystac, cdsapi
To implement   : SegmentationModel
"""
