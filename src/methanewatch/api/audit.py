"""src/methanewatch/api/audit.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Audit middleware: state changes, exports and denied requests.
Why it exists  : Guarantees refusals are recorded even if a router forgets.
Requirements   : NFR3
Stage          : Alpha
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : services, domain, core; fastapi; adapters only in deps.py
Must not import: capability packages directly
To implement   : AuditMiddleware
"""
