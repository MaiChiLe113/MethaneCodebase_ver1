"""src/methanewatch/verification/status.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Combine stage results into a proposed status with evidence references.
Why it exists  : The system only proposes; the analyst decides (see state-candidate-status).
Requirements   : FR7
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; numpy
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : propose_status(results) -> Proposal
"""
