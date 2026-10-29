"""src/methanewatch/evidence/signing.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Ed25519 detached signature over the manifest through the Signer port.
Why it exists  : The signature protects the manifest, the manifest protects the files; the
                 private key never enters the repo.
Requirements   : NFR2, NFR3
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; hashlib, reportlab
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : sign_manifest(manifest, signer)
"""
