"""src/methanewatch/adapters/stac/stac_scene_source.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : SceneSource for Sentinel-2 L1C through STAC (pystac-client).
Why it exists  : The only module that knows the STAC API.
Requirements   : FR1
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : ports, domain, core; boto3, fastapi, pystac, cdsapi, mlflow, argon2, jwt
Must not import: services, api, workers, cli
To implement   : StacSceneSource
"""
