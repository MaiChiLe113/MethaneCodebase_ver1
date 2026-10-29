"""src/methanewatch/evidence/dossier.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Render the readable PDF and the manifest.json.
Why it exists  : People need a document; machines need exact digests.
Requirements   : NFR2, FR6
Stage          : Alpha
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; hashlib, reportlab
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : render_dossier(manifest, provenance) -> bytes
"""
