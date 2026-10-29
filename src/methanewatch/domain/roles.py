"""src/methanewatch/domain/roles.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Role and Action enumerations (analyst, inspector, regulator, ml_engineer,
                 admin).
Why it exists  : The permission matrix in configs/permissions.yaml refers to these names; a typo
                 must fail at load time.
Requirements   : FR5, NFR3
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : core
Must not import: ports, adapters, services, api; boto3, fastapi, pystac, cdsapi; any file or
                 network I/O
To implement   : Role, Action
"""
