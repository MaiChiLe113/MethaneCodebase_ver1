"""src/methanewatch/api/rbac.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Role by action check from configs/permissions.yaml; deny by default.
Why it exists  : Access is decided only here; the portal merely hides what this would refuse.
Requirements   : FR5, NFR3
Stage          : Alpha
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : services, domain, core; fastapi; adapters only in deps.py
Must not import: capability packages directly
To implement   : require(action) -> Dependency
"""
