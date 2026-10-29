"""src/methanewatch/models/classical/threshold.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Classical band-ratio or threshold baseline on B11 and B12 (no training).
Why it exists  : A floor every learned model must beat; also the reference the report asks for.
Requirements   : FR2
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, core; torch (mamba-ssm optional)
Must not import: data, training, evaluation; boto3, fastapi, pystac, cdsapi
To implement   : ThresholdModel
"""
