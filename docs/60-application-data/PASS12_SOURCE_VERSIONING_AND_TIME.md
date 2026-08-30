# Pass 12 — Source versioning and time

Hydrology needs two separate clocks.

## Measurement time

`valid_from`, `valid_to`, and the source date identify when the hydrologic value applies.

## Knowledge time

`retrieved_at`, `source_release`, evidence publication date and raw artifact hash identify what Kristal knew and from which release.

This matters because official station metadata can change. Pass 12 demonstrates this explicitly for Natashquan 02WB003: the existing WSC source record uses **15,400 km² gross drainage area**, while the current CEHQ station page publishes **15,693 km² basin at station**. Both are retained under separate metrics/evidence. No value is silently overwritten.

HYDAT target release for this pass: `HYDAT_20260717`.
