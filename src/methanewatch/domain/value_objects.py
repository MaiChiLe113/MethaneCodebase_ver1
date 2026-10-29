"""src/methanewatch/domain/value_objects.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Small immutable types: Point, Polygon, DateRange, Tile, Sha256, Confidence.
Why it exists  : Keeps geometry and digests validated at the edge, not at every use.
Requirements   : FR1, FR2
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : core
Must not import: ports, adapters, services, api; boto3, fastapi, pystac, cdsapi; any file or
                 network I/O
To implement   : Point, Polygon, DateRange, Tile, Sha256, Confidence
"""
