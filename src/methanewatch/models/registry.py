"""src/methanewatch/models/registry.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Name-to-class registry and build_model(cfg).
Why it exists  : Adding a model is one file, one registry line and one YAML.
Requirements   : FR2
Stage          : Alpha
Proposed owner : Hai (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, core; torch (mamba-ssm optional)
Must not import: data, training, evaluation; boto3, fastapi, pystac, cdsapi
To implement   : register(name), build_model(cfg)
"""
