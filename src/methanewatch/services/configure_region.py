"""src/methanewatch/services/configure_region.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Use case: create or change a monitored region and alert cadence.
Why it exists  : Regions drive what the pipeline monitors.
Requirements   : FR1, FR4
Stage          : Beta scaffold
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, models, training, evaluation, inference, verification, quantification,
                 attribution, evidence, domain, ports, core
Must not import: adapters, api, workers, cli; boto3, fastapi, pystac, cdsapi
To implement   : ConfigureRegion.execute(user, region)
"""
