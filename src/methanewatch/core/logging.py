"""src/methanewatch/core/logging.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Structured logging with a request or run id on every line.
Why it exists  : Needed to trace one detection across worker, API and audit log without a
                 debugger.
Requirements   : NFR5
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : standard library, pydantic, pyyaml
Must not import: any other methanewatch package
To implement   : get_logger(name), bind(run_id=...)
"""
