# Pass 9–10 → Kristal Platform migration map

| Existing artifact | App-native destination | Rule |
|---|---|---|
| 34 watershed polygons | `core.natural_feature(type=watershed)` **only when official geometry is ingested** | current null state remains evidence/status |
| 35 authoritative river reaches | `core.natural_feature(type=river_reach)` after connectivity review | no auto-promotion from nearby lines |
| 36 DEM terrain profiles | `research.observation` with `derivation_type=derived` | terrain drop != project head |
| 37 hydrology observation profiles | WSC point -> `core.asset`; drainage area -> `research.observation`; metadata -> `research.evidence` | gauge != project site |
| 38 hydro research reaches | canonical river -> `core.natural_feature`; research readiness -> screening state | unranked |
| 39 reach logistics context | evidence + screening dimension state | proximity != access |
| 40 evidence matrix | `research.screening_dimension_state` | no score |
| 41 WSC basin availability | `research.evidence` + ingestion job | no fake polygon |
| 42 hydrography extraction jobs | `system.ingestion_job` | not a public map layer |
| 43 analysis windows | `system.ingestion_job.request_geometry` | request window != basin/reach |
| 44 attribute schema registry | `system.dataset_schema` / catalog metadata | system metadata |
| 45 HRDEM jobs | `system.ingestion_job` | raster outputs -> COG/raw/staging |
| 46 execution status | `system.ingestion_job.status` | operational state |
| 47 reach terrain gate | `research.screening_dimension_state(engineering/hydrology)` | gate != ranking |

## Pass 8 contract

The app architecture explicitly requires Pass 8 `status_record_no_geometry` objects to migrate primarily as evidence/observations/reference records rather than fictitious map points. Planning margins become time-series observations, and the screening override becomes governance state. The pass-8 data package is not present in the current Pass-10 worktree, so Pass 11 implements the target schema/contract but does not fabricate missing Pass-8 rows.
