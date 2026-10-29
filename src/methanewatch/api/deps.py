"""src/methanewatch/api/deps.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Composition root: builds adapters from settings and injects them into services.
Why it exists  : The only place that knows which adapter is used, so LocalStack to AWS is a
                 setting.
Requirements   : NFR5
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : services, domain, core; fastapi; adapters only in deps.py
Must not import: capability packages directly
To implement   : build_services(settings) -> Services
"""
