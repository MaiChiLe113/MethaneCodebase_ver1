"""src/methanewatch/adapters/aws/s3_object_store.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : ObjectStore on S3, with LocalStack for development.
Why it exists  : Same code, different endpoint.
Requirements   : NFR2
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : ports, domain, core; boto3, fastapi, pystac, cdsapi, mlflow, argon2, jwt
Must not import: services, api, workers, cli
To implement   : S3ObjectStore
"""
