"""src/methanewatch/evidence/audit_chain.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Hash-chained audit entries: each holds the hash of the previous one.
Why it exists  : Editing history breaks the chain, so tampering is detectable.
Requirements   : NFR3
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; hashlib, reportlab
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : next_entry(prev, action, user, target), verify_chain(entries)
"""
