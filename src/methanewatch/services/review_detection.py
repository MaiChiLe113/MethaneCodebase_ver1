"""src/methanewatch/services/review_detection.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Use case: record a review (append-only) and audit it.
Why it exists  : Enforces reason required, Supported needs complete evidence, reviewer is the
                 caller.
Requirements   : FR5, FR7, NFR3
Stage          : Alpha
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, models, training, evaluation, inference, verification, quantification,
                 attribution, evidence, domain, ports, core
Must not import: adapters, api, workers, cli; boto3, fastapi, pystac, cdsapi
To implement   : ReviewDetection.execute(user, detection_id, status, reason, refs)
"""
