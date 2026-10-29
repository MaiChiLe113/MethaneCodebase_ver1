"""src/methanewatch/evaluation/benchmark.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Run every model on the sealed real test and write one results table; also score
                 the zero-shot pretrained model.
Why it exists  : The benchmark is the research deliverable; it must be one command.
Requirements   : FR2
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, domain, core; numpy
Must not import: models internals, boto3, fastapi, pystac, cdsapi; services, api
To implement   : run_benchmark(models, test_split) -> BenchmarkResult
"""
