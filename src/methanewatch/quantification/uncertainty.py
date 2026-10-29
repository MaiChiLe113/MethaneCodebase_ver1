"""src/methanewatch/quantification/uncertainty.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Rate range from wind, mask and plume-length uncertainty; mark preliminary until
                 final ERA5.
Why it exists  : A rate without its uncertainty is not reportable.
Requirements   : FR3
Stage          : Alpha
Proposed owner : Chau (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; numpy
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : rate_range(inputs) -> (low, high)
"""
