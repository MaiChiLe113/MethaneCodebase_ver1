"""src/methanewatch/api/auth.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Token to user and role; reject unknown tokens.
Why it exists  : Authentication before authorisation; see seq-login-rbac.
Requirements   : FR5, NFR3
Stage          : Alpha
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : services, domain, core; fastapi; adapters only in deps.py
Must not import: capability packages directly
To implement   : current_user(request) -> User
"""
