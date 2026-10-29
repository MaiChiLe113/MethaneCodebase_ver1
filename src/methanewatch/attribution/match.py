"""src/methanewatch/attribution/match.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Rank plausible sources; return Match or Unresolved.
Why it exists  : Several candidates or none stay unresolved for the analyst; a plume near a
                 facility is not that facility's plume.
Requirements   : FR3
Stage          : Alpha
Proposed owner : Chau (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; shapely, pyproj
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : attribute(candidate, wind, index) -> FacilityMatch
"""
