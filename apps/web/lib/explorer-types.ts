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

export type ExplorerBootstrap = {
  release: string;
  generatedAt: string;
  screeningMode: "unranked";
  rankingAllowed: false;
  communities: PublicFeatureCollection;
  stations: PublicFeatureCollection;
  rivers: PublicRiverReference[];
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
};

export type ObservatoryVisibleLayers = {
  communities: boolean;
  hydrometric_stations: boolean;
  contextual_hydrography: boolean;
  satellite: boolean;
  labels: boolean;
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

export type MapCameraState = {
  lng: number;
  lat: number;
  zoom: number;
  bearing: number;
  pitch: number;
};
