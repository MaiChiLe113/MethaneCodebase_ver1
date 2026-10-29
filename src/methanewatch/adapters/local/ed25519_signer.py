"""src/methanewatch/adapters/local/ed25519_signer.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Signer using an Ed25519 key from an untracked file.
Why it exists  : Real signatures in Alpha; key custody for Beta is an ADR.
Requirements   : NFR2, NFR3
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : ports, domain, core; boto3, fastapi, pystac, cdsapi, mlflow, argon2, jwt
Must not import: services, api, workers, cli
To implement   : Ed25519Signer(key_path)
"""
