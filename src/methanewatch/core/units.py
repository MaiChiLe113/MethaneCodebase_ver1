"""src/methanewatch/core/units.py

STATUS: PLACEHOLDER. No implementation yet; this file fixes the name, place and contract.

Purpose        : Unit conversions with explicit names: kg/h, ppb, mol/m2, m/s, km, pixels at 20
                 m.
Why it exists  : The IME rate is a product of many unit conversions; one tested module prevents
                 silent factor errors.
Requirements   : FR3, NFR2
Stage          : Alpha
Proposed owner : Chi (confirm at sprint planning)
Backlog / Jira : assign at sprint planning (report Table 6.1); commits and PR titles carry
                 MWPMWP-<n>
May import     : standard library, pydantic, pyyaml
Must not import: any other methanewatch package
To implement   : kg_per_h, ppb_to_mol_m2, pixels_to_m(pixels, gsd=20)
"""
