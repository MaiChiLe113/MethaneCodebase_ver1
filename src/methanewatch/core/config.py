"""src/methanewatch/core/config.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Typed configuration (Pydantic v2) loaded from configs/*.yaml and environment.
Why it exists  : Every experiment and release gate must be reproducible from a file; one loader
                 means no scattered os.environ reads.
Requirements   : NFR5
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : standard library, pydantic, pyyaml
Must not import: any other methanewatch package
To implement   : Settings, load_settings(path), ExperimentConfig
"""
