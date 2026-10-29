"""src/methanewatch/services/promote_model.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Use case: promote a model only if the Beta gate passes; roll back to the
                 previous version.
Why it exists  : The registry must refuse an unapproved model.
Requirements   : FR2, NFR5
Stage          : Alpha
Proposed owner : Nam (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, models, training, evaluation, inference, verification, quantification,
                 attribution, evidence, domain, ports, core
Must not import: adapters, api, workers, cli; boto3, fastapi, pystac, cdsapi
To implement   : PromoteModel.execute(user, version), rollback(user)
"""
