"""src/methanewatch/verification/stage1_quality.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Stage 1: observation quality (cloud, invalid pixels, alignment, suitability of
                 references).
Why it exists  : Poor observations must be screened first and returned as Unreviewable, not
                 guessed at.
Requirements   : FR7
Stage          : Alpha
Proposed owner : Chau (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; numpy
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : check_quality(stack, candidate) -> StageResult
"""
