"""src/methanewatch/adapters/era5/era5_wind.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : WindProvider reading ERA5 or ERA5T through the CDS API with a file cache.
Why it exists  : Records source and version; marks ERA5T results preliminary.
Requirements   : FR3
Stage          : Alpha
Proposed owner : Chau (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : ports, domain, core; boto3, fastapi, pystac, cdsapi, mlflow, argon2, jwt
Must not import: services, api, workers, cli
To implement   : Era5WindProvider
"""
