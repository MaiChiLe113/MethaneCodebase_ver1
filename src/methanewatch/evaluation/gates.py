"""src/methanewatch/evaluation/gates.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Release gate function: Beta needs F1 >= 0.80 and FPR < 0.03 percent; Alpha
                 targets are reported only.
Why it exists  : A promotion rule must be a tested function, not a sentence in a document; see
                 diagrams/06-mlops/release-gate.
Requirements   : NFR2, NFR5
Stage          : Alpha
Proposed owner : Ha (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : data, domain, core; numpy
Must not import: models internals, boto3, fastapi, pystac, cdsapi; services, api
To implement   : check_beta_gate(metrics, gates) -> GateResult
"""
