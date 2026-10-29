"""src/methanewatch/domain/estimate.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : EmissionEstimate as a sum type: Estimate(rate, low, high, wind_source,
                 wind_version, preliminary) | Unavailable(reason) | Uncertain(reason).
Why it exists  : Makes it impossible to return a bare number; the type system carries the
                 report's rule.
Requirements   : FR3, FR7
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : core
Must not import: ports, adapters, services, api; boto3, fastapi, pystac, cdsapi; any file or
                 network I/O
To implement   : Estimate, Unavailable, Uncertain
"""
