# Hydrology source versioning and time

Hydrology uses two separate clocks.

## Measurement time

`valid_from`, `valid_to` and source date identify when a hydrologic value applies.

## Knowledge time

`retrieved_at`, `source_release`, evidence publication date and raw-artifact hash identify what the project knew and from which release.

This distinction matters because official metadata can change. Natashquan station 02WB003 currently retains both the WSC `gross_drainage_area_km2 = 15400` observation and the CEHQ `station_basin_area_km2 = 15693` observation under separate metrics/evidence; neither silently overwrites the other.

The current HYDAT source manifest records release `HYDAT_20260717`.
