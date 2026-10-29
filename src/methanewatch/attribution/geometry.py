"""src/methanewatch/attribution/geometry.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Distance and upwind tests between plume polygons and facility locations.
Why it exists  : Isolates the geometry so it can be tested on hand-made cases.
Requirements   : FR3
Stage          : Alpha
Proposed owner : Chau (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; shapely, pyproj
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : upwind_distance(plume, facility, wind)
"""
