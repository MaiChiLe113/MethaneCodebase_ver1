"""src/methanewatch/verification/stage3_plausibility.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Stage 3: plume shape and orientation against wind and nearby sources
                 (supporting, not proof).
Why it exists  : A physical sanity check that can raise or lower confidence.
Requirements   : FR7
Stage          : Alpha
Proposed owner : Lam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; numpy
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : check_plausibility(candidate, wind, facilities) -> StageResult
"""
