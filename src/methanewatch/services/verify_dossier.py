"""src/methanewatch/services/verify_dossier.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Use case: verify a stored dossier.
Why it exists  : Regulators and inspectors check integrity without touching the science.
Requirements   : NFR2
Stage          : Alpha
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, models, training, evaluation, inference, verification, quantification,
                 attribution, evidence, domain, ports, core
Must not import: adapters, api, workers, cli; boto3, fastapi, pystac, cdsapi
To implement   : VerifyDossier.execute(dossier_id)
"""
