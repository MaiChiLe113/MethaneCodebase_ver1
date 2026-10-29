"""src/methanewatch/domain/events.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Domain events (DetectionCreated, ReviewRecorded, DossierExported,
                 ModelPromoted).
Why it exists  : Services publish events; the audit sink subscribes, so no use case forgets to
                 audit.
Requirements   : NFR3
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : core
Must not import: ports, adapters, services, api; boto3, fastapi, pystac, cdsapi; any file or
                 network I/O
To implement   : DetectionCreated, ReviewRecorded, DossierExported, ModelPromoted
"""
