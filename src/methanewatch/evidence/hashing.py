"""src/methanewatch/evidence/hashing.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Streamed SHA-256 of every artefact and a manifest of digests.
Why it exists  : The base of tamper evidence.
Requirements   : NFR2, NFR3
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; hashlib, reportlab
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : sha256_file(path), build_manifest(artefacts)
"""
