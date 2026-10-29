"""src/methanewatch/ports/signer.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Signer Protocol.
Why it exists  : Defines what services need from the outside world, so the science and ML code
                 can be tested with an in-memory fake. See diagrams/03-code/ports-adapters.
Requirements   : NFR2, NFR3
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, core
Must not import: adapters, services, api; boto3, fastapi, pystac, cdsapi
To implement   : sign(manifest_bytes) -> bytes; verify(manifest_bytes, signature) -> bool
"""
