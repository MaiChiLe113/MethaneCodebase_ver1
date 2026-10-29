"""src/methanewatch/evidence/provenance.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : PROV-style lineage: data, code version, model, person.
Why it exists  : Lets a reviewer see exactly what produced a result.
Requirements   : NFR2
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; hashlib, reportlab
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : build_provenance(detection, review, versions)
"""
