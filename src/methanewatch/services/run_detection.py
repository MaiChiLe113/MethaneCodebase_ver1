"""src/methanewatch/services/run_detection.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Use case: scenes to a saved detection with proposal, estimate and match.
Why it exists  : The orchestration order is the product; see seq-detect-and-quantify.
Requirements   : FR1, FR2, FR3, FR7, NFR1
Stage          : Alpha
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, models, training, evaluation, inference, verification, quantification,
                 attribution, evidence, domain, ports, core
Must not import: adapters, api, workers, cli; boto3, fastapi, pystac, cdsapi
To implement   : RunDetection(ports...).execute(region, date)
"""
