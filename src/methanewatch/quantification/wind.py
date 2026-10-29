"""src/methanewatch/quantification/wind.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Effective wind from ERA5 wind at the source location and time.
Why it exists  : ERA5 is about 31 km and ERA5T lags about five days, so source and version must
                 be recorded.
Requirements   : FR3
Stage          : Alpha
Proposed owner : Chau (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : domain, ports, core; numpy
Must not import: sibling capabilities, boto3, fastapi, pystac, cdsapi; services, api
To implement   : effective_wind(wind) -> EffectiveWind
"""
