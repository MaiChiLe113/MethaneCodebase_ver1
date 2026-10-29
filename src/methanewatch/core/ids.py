"""src/methanewatch/core/ids.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Typed identifiers (DetectionId, SceneId, RegionId, UserId) and their string
                 forms.
Why it exists  : Prevents mixing a scene id with a detection id; ids appear in DynamoDB keys.
Requirements   : NFR2
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : standard library, pydantic, pyyaml
Must not import: any other methanewatch package
To implement   : DetectionId, SceneId, RegionId, UserId, new_id()
"""
