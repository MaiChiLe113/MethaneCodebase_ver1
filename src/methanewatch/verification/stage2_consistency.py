"""src/methanewatch/verification/stage2_consistency.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Stage 2: compare the mask with the MBMP product and with history to find
                 persistent surface features.
Why it exists  : Checks that rely on related satellite data strengthen consistency but are not
                 independent confirmation.
Requirements   : FR7
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; numpy
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : check_consistency(candidate, mbmp, history) -> StageResult
"""
