"""src/methanewatch/evaluation/error_analysis.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Errors by site, cloud level and emission rate.
Why it exists  : False alarms are the report's main risk; this shows where they come from.
Requirements   : FR2, NFR2
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, domain, core; numpy
Must not import: models internals, boto3, fastapi, pystac, cdsapi; services, api
To implement   : by_site(result), by_cloud(result), by_rate(result)
"""
