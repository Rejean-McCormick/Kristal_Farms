export type MapPointFeatureKind = "community" | "hydrometric_station";
export type EntityKind = MapPointFeatureKind | "river";

export type PointGeometry = {
  type: "Point";
  coordinates: [number, number];
};

export type PublicFeatureProperties = {
  entity_id: string;
  name: string;
  region: string | null;
  feature_kind: MapPointFeatureKind;
  ranking_allowed: false;
  geometry_role?: string;
  geometry_precision?: string;
  not_facility_coordinate?: boolean;
  station_number?: string;
  river_name?: string;
  river_entity_id?: string;
  status?: string;
  evidence_status?: string;
  gross_drainage_area_km2?: number | null;
  marine_context?: string | null;
  telecom_context?: string | null;
  road_context?: string | null;
  energy_context?: string | null;
  population?: number | null;
};

export type PublicMapFeature = {
  type: "Feature";
  id: string;
  geometry: PointGeometry;
  properties: PublicFeatureProperties;
};

export type PublicFeatureCollection = {
  type: "FeatureCollection";
  release: string;
  features: PublicMapFeature[];
};

export type RiverScreeningDimension = {
  status: string;
  evidence_completeness: string;
  open_questions: string[];
  last_reviewed: string | null;
};

export type PublicRiverReference = {
  entity_id: string;
  canonical_key: string;
  name: string;
  region: string | null;
  status: string;
  ranking_allowed: false;
  aliases: string[];
  anchor: PointGeometry | null;
  anchor_station_entity_id: string | null;
  anchor_station_number: string | null;
  gross_drainage_area_km2: number | null;
  geometry_status: "authoritative_flowline_not_ingested";
  hydrology: RiverScreeningDimension | null;
  engineering: RiverScreeningDimension | null;
};

export type LayerCatalogEntry = {
  id: string;
  title: string;
  layer_group: string;
  display_config: {
    renderer: string;
    layer_type?: string;
    min_zoom?: number;
    max_zoom?: number;
  };
  evidence_config?: { enabled?: boolean };
  permissions?: { public?: boolean };
  semantics?: Record<string, unknown>;
};


export type PublicHydroScreeningSite = {
  id: string;
  entry_id: string;
  name: string;
  river_name: string | null;
  capacity_or_potential: string | null;
  current_status: string | null;
  geometry_confidence: string | null;
  geometry_class: string;
  geometry_role: "screening_reference_not_engineered_dam_site";
  coordinates: [number, number];
  nearest_active_community: string | null;
  distance_to_active_community_km: number | null;
  distance_to_mouth_or_coast_proxy_km: number | null;
  mouth_or_coast_proxy: [number, number] | null;
  mapping_note: string | null;
  source_notes: string | null;
  screening_scope: "coastal_core" | "coastal_extended_review";
  ranking_allowed: false;
};

export type PublicSourceReference = {
  name: string | null;
  url: string | null;
  reference_date: string | null;
};

export type PublicCommunityInfrastructure = {
  entity_id: string;
  name: string;
  region: string | null;
  ranking_allowed: false;
  population: {
    value: number | null;
    year: number | null;
    geography: string | null;
    source: PublicSourceReference | null;
    note: string | null;
  };
  airport: {
    access_known: boolean;
    code: string | null;
    name: string | null;
    runway_length_m: number | null;
    runway_surface: string | null;
    dimension_status: "published_reference" | "runtime_basemap_or_unknown";
    presence_source: PublicSourceReference | null;
    dimension_source: PublicSourceReference | null;
    note: string | null;
  };
  marine: {
    access_known: boolean;
    context: string | null;
    facility_name: string | null;
    dock_length_m: number | null;
    max_draft_m: number | null;
    heavy_lift_status: "confirmed" | "not_verified" | "unknown" | string;
    size_status: "published_reference" | "runtime_basemap_or_unknown" | "unknown" | string;
    source: PublicSourceReference | null;
    note: string | null;
  };
  runtime_enrichment: {
    basemap_facility_geometry_allowed: boolean;
    basemap_population_fallback_allowed: boolean;
    note: string | null;
  };
};

export type ExplorerBootstrap = {
  release: string;
  generatedAt: string;
  screeningMode: "unranked";
  rankingAllowed: false;
  communities: PublicFeatureCollection;
  stations: PublicFeatureCollection;
  rivers: PublicRiverReference[];
  hydroSites: PublicHydroScreeningSite[];
  communityInfrastructure: PublicCommunityInfrastructure[];
  layers: LayerCatalogEntry[];
};

export type EvidenceSummary = {
  entity_id: string;
  name: string;
  facts: number;
  supported: number;
  conflicting: number;
  unverified_or_unknown: number;
  evidence_ids: string[];
  ranking_allowed: false;
};

export type EvidenceSource = {
  id: string;
  title: string;
  publisher: string | null;
  source_type: string;
  url: string | null;
  role: string;
};

export type EvidenceRecord = {
  id: string;
  evidence_type: string;
  claim: string;
  status: string;
  confidence: string | null;
  retrieved_at: string | null;
  sources: EvidenceSource[];
};

export type RelationItem = {
  id: string;
  label: string;
  value: string;
  kind: "context" | "entity";
  entityId?: string;
};

export type EntityScreeningDimension = {
  id: string;
  label: string;
  status: string;
  evidenceCompleteness: string;
  openQuestions: string[];
  lastReviewed: string | null;
  appliesTo: string | null;
};

export type EntityDetail = {
  entityId: string;
  featureKind: EntityKind;
  title: string;
  subtitle: string | null;
  status: string | null;
  geometry: PointGeometry | null;
  geometryRole: string | null;
  geometryPrecision: string | null;
  mapGeometryStatus: "official" | "approximate" | "unavailable";
  mapNote: string | null;
  notFacilityCoordinate: boolean;
  facts: Array<{ label: string; value: string }>;
  relations: RelationItem[];
  evidence: EvidenceSummary | null;
  evidenceRecords: EvidenceRecord[];
  screeningDimensions: EntityScreeningDimension[];
  release: string;
  rankingAllowed: false;
  targetVillageSlug?: string | null;
};

export type ObservatoryVisibleLayers = {
  communities: boolean;
  hydrometric_stations: boolean;
  contextual_hydrography: boolean;
  contextual_buildings: boolean;
  contextual_transport: boolean;
  contextual_facilities: boolean;
  grid_reach: boolean;
  satellite: boolean;
  terrain_relief: boolean;
  terrain_basins: boolean;
  labels: boolean;
};


export type GridReachManifest = {
  type: "FeatureCollection";
  schema: "kristal-grid-reach/v1";
  version: string;
  status: "research_context" | string;
  ranking_allowed: false;
  default_visible: boolean;
  measurement_allowed: false;
  local_distribution_network_included: false;
  title: string;
  note: string;
  sources: Array<{
    id: string;
    publisher: string;
    title: string;
    url: string;
    reference_date: string | null;
  }>;
  features: Array<{
    type: "Feature";
    id?: string | number;
    geometry: { type: string; coordinates: unknown };
    properties: Record<string, unknown>;
  }>;
};

export type LocalImageryManifest = {
  schema: "kristal-local-imagery/v1";
  id: string;
  title: string;
  available: boolean;
  tile_template: string;
  tile_size: 256 | 512;
  minzoom: number;
  maxzoom: number;
  bounds: [number, number, number, number] | null;
  source: string | null;
  acquired: string | null;
  license: string | null;
  attribution: string | null;
  source_sha256?: string | null;
  generated_at?: string | null;
};

export type LocalTerrainRiseSummary = {
  rise_m: number;
  area_km2: number;
  volume_m3: number;
  max_depth_m: number;
};

export type LocalTerrainSiteProfile = {
  site_id: string;
  site_name: string;
  seed_elevation_m: number;
  min_rise_m: number;
  max_rise_m: number;
  default_rise_m: number;
  feature_count: number;
  rise_summaries: LocalTerrainRiseSummary[];
};

export type LocalTerrainManifest = {
  schema: "kristal-local-terrain/v1";
  id: string;
  title: string;
  available: boolean;
  geojson_url: string;
  minzoom: number;
  maxzoom: number;
  bounds: [number, number, number, number] | null;
  source: string | null;
  vertical_datum: string | null;
  cell_size_m: number | null;
  generated_at?: string | null;
  note?: string | null;
  site_profiles: LocalTerrainSiteProfile[];
};

export type ContextInfrastructureKind =
  | "airport"
  | "dock"
  | "dam"
  | "power"
  | "potential_hydro";

export type ScreeningConfidence = "low" | "medium" | "high";

export type ContextInfrastructure = {
  key: string;
  kind: ContextInfrastructureKind;
  name: string;
  coordinates: [number, number];
  source: string;
  sizeLabel: string | null;
  capacityMw: number | null;
  capacityBasis: "mapped" | "estimated_head_flow" | "screening_range" | "published_potential_label" | null;
  nearestPortName: string | null;
  nearestPortDistanceKm: number | null;
  nearestAirportName?: string | null;
  nearestAirportDistanceKm?: number | null;
  nearestCommunityName?: string | null;
  nearestCommunityDistanceKm?: number | null;
  populationServed?: number | null;
  screeningConfidence?: ScreeningConfidence | null;
  estimatedHeadM?: number | null;
  estimatedFlowM3s?: number | null;
  estimatedPowerMinMw?: number | null;
  estimatedPowerMaxMw?: number | null;
  riverName?: string | null;
  basinName?: string | null;
  evidenceLabel?: string | null;
  powerLabel?: string | null;
  statusLabel?: string | null;
  geometryConfidence?: string | null;
  coastProxyDistanceKm?: number | null;
  sourceNote?: string | null;
  notes?: string | null;
};

export type CommunityInfrastructureSummary = {
  population: number | null;
  populationYear: number | null;
  populationGeography: string | null;
  populationSource: string | null;
  populationSourceUrl: string | null;
  populationNote: string | null;
  airport: ContextInfrastructure | null;
  airportDistanceKm: number | null;
  airportCode: string | null;
  airportPublishedRunwayLengthM: number | null;
  airportPublishedSurface: string | null;
  airportPublishedSource: string | null;
  airportPublishedSourceUrl: string | null;
  airportPublishedNote: string | null;
  dock: ContextInfrastructure | null;
  dockDistanceKm: number | null;
  marinePublishedDockLengthM: number | null;
  marinePublishedMaxDraftM: number | null;
  marineHeavyLiftStatus: string | null;
  marinePublishedSource: string | null;
  marinePublishedSourceUrl: string | null;
  marinePublishedNote: string | null;
  hasPublishedMarineContext: boolean;
  associatedHydroSites: Array<{ facility: ContextInfrastructure; distanceKm: number }>;
};

export type MapCameraState = {
  lng: number;
  lat: number;
  zoom: number;
  bearing: number;
  pitch: number;
};
