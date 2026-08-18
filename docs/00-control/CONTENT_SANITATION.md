# Content and Source Hygiene

## Promotion blockers, not automatic visibility blockers

Working research can remain public while still being unsuitable as authoritative evidence.

The following files contain non-portable assistant/UI-style citation artifacts and require source cleanup before their claims are promoted into formal engineering, regulatory, investor or partner material:

- `docs/30-site-screening/nunavik/Rivieres_littoral_ouest_Nord_quebecois_nord_La_Grande.md`
- `docs/50-research/Partners_inventory_deep-research-report.md`

## Scan before formal promotion

Check for:

- `turn...search` tokens;
- `filecite` tokens;
- private-use Unicode citation symbols;
- unsupported precise numeric claims;
- obsolete as-of dates;
- source links that no longer identify the referenced evidence;
- language that converts a working assumption into an operational result.

## Public repository exclusions

Credentials, private tenant data, PII, legally restricted material, confidential rights-holder information and credible operational-security details should remain outside Git. See `PUBLICATION_POLICY.md`.
