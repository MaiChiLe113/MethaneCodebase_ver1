"""src/methanewatch/models/mamba/scan_fallback.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Pure PyTorch selective scan used when mamba-ssm or CUDA is missing.
Why it exists  : The laptop has no CUDA; without a fallback nobody could run or unit-test the
                 Mamba models there.
Requirements   : FR2, NFR5
Stage          : Alpha
Proposed owner : Hai (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, core; torch (mamba-ssm optional)
Must not import: data, training, evaluation; boto3, fastapi, pystac, cdsapi
To implement   : selective_scan(u, delta, A, B, C, D)
"""
