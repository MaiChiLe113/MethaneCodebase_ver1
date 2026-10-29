"""src/methanewatch/adapters/aws/dynamodb_audit_sink.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : AuditSink with conditional writes (refuse overwrite).
Why it exists  : Immutable audit log.
Requirements   : NFR3
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : ports, domain, core; boto3, fastapi, pystac, cdsapi, mlflow, argon2, jwt
Must not import: services, api, workers, cli
To implement   : DynamoAuditSink
"""
