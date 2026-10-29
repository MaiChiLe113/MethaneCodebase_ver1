"""src/methanewatch/verification/mbmp.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Multi-band multi-pass enhancement product used for consistency checks.
Why it exists  : A physical product independent of the neural network.
Requirements   : FR7
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; numpy
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : mbmp(stack) -> Raster
"""
