"""src/methanewatch/adapters/memory/fakes.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : In-memory implementations of every port for unit tests.
Why it exists  : Lets the whole science chain run with no cloud and no GPU.
Requirements   : NFR5
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : ports, domain, core; boto3, fastapi, pystac, cdsapi, mlflow, argon2, jwt
Must not import: services, api, workers, cli
To implement   : InMemory<Port> for each port in ports/
"""
