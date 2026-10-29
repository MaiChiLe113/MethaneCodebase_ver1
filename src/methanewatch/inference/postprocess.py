"""src/methanewatch/inference/postprocess.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Threshold, clean small blobs, find connected components.
Why it exists  : Turns probabilities into objects an analyst can review.
Requirements   : FR2
Stage          : Alpha
Proposed owner : Chau (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : models, data, domain, ports, core; torch
Must not import: boto3, fastapi, pystac, cdsapi; services, api
To implement   : to_components(prob, threshold, min_pixels)
"""
