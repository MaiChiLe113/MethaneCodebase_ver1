"""src/methanewatch/evaluation/metrics.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : IoU, F1, precision, recall, false-positive rate at pixel and object level.
Why it exists  : The Alpha targets and the Beta gate are defined on these; one tested
                 implementation.
Requirements   : FR2, NFR2
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, domain, core; numpy
Must not import: models internals, boto3, fastapi, pystac, cdsapi; services, api
To implement   : iou, f1, precision, recall, fpr
"""
