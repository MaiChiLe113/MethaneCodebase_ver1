"""src/methanewatch/adapters/aws/dynamodb_repositories.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Detection, Review, Region, User and ModelVersion repositories on DynamoDB.
Why it exists  : Keys follow diagrams/05-data/er-model; decision D12.
Requirements   : FR2, FR5, FR6
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : ports, domain, core; boto3, fastapi, pystac, cdsapi, mlflow, argon2, jwt
Must not import: services, api, workers, cli
To implement   : Dynamo<Repository> classes
"""
