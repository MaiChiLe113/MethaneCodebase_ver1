"""src/methanewatch/adapters/aws/s3_evidence_store.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : EvidenceStore on S3 Object Lock (write once).
Why it exists  : WORM storage is a Beta requirement.
Requirements   : NFR2
Stage          : Beta scaffold
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : ports, domain, core; boto3, fastapi, pystac, cdsapi, mlflow, argon2, jwt
Must not import: services, api, workers, cli
To implement   : S3EvidenceStore
"""
