"""src/methanewatch/services/export_dossier.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Use case: seal, sign and store a dossier, then audit the export.
Why it exists  : Refuses unless the latest review is Supported and evidence is complete.
Requirements   : FR6, NFR2, NFR3
Stage          : Alpha
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, models, training, evaluation, inference, verification, quantification,
                 attribution, evidence, domain, ports, core
Must not import: adapters, api, workers, cli; boto3, fastapi, pystac, cdsapi
To implement   : ExportDossier.execute(user, detection_id)
"""
