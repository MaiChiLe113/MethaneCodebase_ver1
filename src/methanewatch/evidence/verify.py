"""src/methanewatch/evidence/verify.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Recompute digests and check the signature; return Intact or Tampered with the
                 changed artefact.
Why it exists  : The required tamper test calls this.
Requirements   : NFR2
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; hashlib, reportlab
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : verify_dossier(dossier_id, store, signer) -> VerifyResult
"""
