"""src/methanewatch/adapters/local/jwt_auth.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : AuthProvider with JWT tokens and argon2 password hashes.
Why it exists  : Gives real sign-in before Cognito exists.
Requirements   : FR5, NFR3
Stage          : Alpha
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : ports, domain, core; boto3, fastapi, pystac, cdsapi, mlflow, argon2, jwt
Must not import: services, api, workers, cli
To implement   : JwtAuthProvider
"""
