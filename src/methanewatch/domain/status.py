"""src/methanewatch/domain/status.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : The four statuses (Supported, Rejected, Uncertain, Unreviewable) and the rule
                 that an emission is confirmed only when an analyst sets Supported and evidence
                 is complete.
Why it exists  : This rule is the report's central safety property; it must live in one tested
                 place, not in a router or a React component.
Requirements   : FR7
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : core
Must not import: ports, adapters, services, api; boto3, fastapi, pystac, cdsapi; any file or
                 network I/O
To implement   : Status, is_confirmed(review, dossier_state), allowed_transitions()
"""
