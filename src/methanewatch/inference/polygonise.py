"""src/methanewatch/inference/polygonise.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Raster components to georeferenced polygons.
Why it exists  : The map shows polygons, not rasters; simplification is needed for the 1.5 s
                 tile target.
Requirements   : FR2, FR6
Stage          : Alpha
Proposed owner : Chau (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : models, data, domain, ports, core; torch
Must not import: boto3, fastapi, pystac, cdsapi; services, api
To implement   : polygonise(component, transform) -> Polygon
"""
