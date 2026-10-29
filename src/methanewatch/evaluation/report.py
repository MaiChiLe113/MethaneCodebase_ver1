"""src/methanewatch/evaluation/report.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Tables and figures from a BenchmarkResult.
Why it exists  : Keeps plotting out of the metrics code.
Requirements   : FR2
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, domain, core; numpy
Must not import: models internals, boto3, fastapi, pystac, cdsapi; services, api
To implement   : to_table(result), plot_curves(result)
"""
