"""src/methanewatch/quantification/estimate.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Return Estimate, Unavailable or Uncertain; never a bare number.
Why it exists  : The report's rule that unsupported inputs produce an explicit reason.
Requirements   : FR3, FR7
Stage          : Alpha
Proposed owner : Chau (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; numpy
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : estimate(candidate, wind_provider) -> EmissionEstimate
"""
