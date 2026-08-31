export type FeatureKind = "community" | "hydrometric_station";

export type PointGeometry = {
  type: "Point";
  coordinates: [number, number];
};

export type PublicFeatureProperties = {
  entity_id: string;
  name: string;
  region: string | null;
  feature_kind: FeatureKind;
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

export type RelationItem = {
  id: string;
  label: string;
  value: string;
  kind: "context" | "entity";
  entityId?: string;
};

export type EntityDetail = {
  entityId: string;
  featureKind: FeatureKind;
  title: string;
  subtitle: string | null;
  status: string | null;
  geometry: PointGeometry;
  geometryRole: string | null;
  geometryPrecision: string | null;
  notFacilityCoordinate: boolean;
  facts: Array<{ label: string; value: string }>;
  relations: RelationItem[];
  evidence: EvidenceSummary | null;
  release: string;
  rankingAllowed: false;
};

export type MapCameraState = {
  lng: number;
  lat: number;
  zoom: number;
  bearing: number;
  pitch: number;
};
