"""src/methanewatch/quantification/ime.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Integrated mass enhancement: Q = IME x U_eff / L.
Why it exists  : The standard point-source rate method; units checked at each step.
Requirements   : FR3
Stage          : Alpha
Proposed owner : Chau (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; numpy
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : ime_rate(enhancement, mask, pixel_m, u_eff, length_m)
"""
