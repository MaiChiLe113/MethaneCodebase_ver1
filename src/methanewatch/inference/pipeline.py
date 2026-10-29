"""src/methanewatch/inference/pipeline.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Scene stack to ranked candidates; the unit that must finish within 15 minutes
                 per granule.
Why it exists  : Timing is measured here, see seq-detect-and-quantify.
Requirements   : FR2, NFR1
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : models, data, domain, ports, core; torch
Must not import: boto3, fastapi, pystac, cdsapi; services, api
To implement   : detect(stack, predictor) -> list[Candidate]
"""
