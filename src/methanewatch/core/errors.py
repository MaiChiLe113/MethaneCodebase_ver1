"""src/methanewatch/core/errors.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : The small set of typed errors every layer raises: NotFound, PermissionDenied,
                 Invalid, Unavailable, Conflict.
Why it exists  : The API maps these to HTTP codes in one place; capabilities never raise HTTP
                 errors.
Requirements   : NFR3, NFR5
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : standard library, pydantic, pyyaml
Must not import: any other methanewatch package
To implement   : NotFound, PermissionDenied, Invalid, Unavailable, Conflict
"""
