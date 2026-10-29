"""src/methanewatch/domain/entities.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Dataclasses for the entities in diagrams/03-code/domain-model: Region, Scene,
                 Detection, Review, VerificationResult, FacilityMatch, EvidenceDossier, User,
                 AuditEntry, ModelVersion.
Why it exists  : One definition of every entity, shared by services, adapters and the API
                 schema.
Requirements   : FR2, FR3, FR5, FR7
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : core
Must not import: ports, adapters, services, api; boto3, fastapi, pystac, cdsapi; any file or
                 network I/O
To implement   : Region, Scene, Detection, Review, VerificationResult, FacilityMatch, Facility,
                 EvidenceDossier, User, AuditEntry, ModelVersion
"""
