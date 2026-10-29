"""src/methanewatch/ports/auth_provider.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : AuthProvider Protocol.
Why it exists  : Defines what services need from the outside world, so the science and ML code
                 can be tested with an in-memory fake. See diagrams/03-code/ports-adapters.
Requirements   : FR5, NFR3
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, core
Must not import: adapters, services, api; boto3, fastapi, pystac, cdsapi
To implement   : authenticate(credentials) -> Session; user_from_token(token) -> User
"""
