export type VillageSourceReference = {
  id: string;
  title: string;
  publisher: string;
  url: string;
  role: string;
};


export type VillageEnergyProject = {
  entity_id: string;
  canonical_key: string | null;
  name: string;
  project_type: string | null;
  status: string | null;
  technology: string | null;
  capacity_mw: number | null;
  developer: string | null;
  metadata: Record<string, unknown>;
  sources: Array<{
    id: string;
    source_key: string;
    title: string;
    publisher: string;
    source_type: string;
    url: string;
    publication_date: string | null;
  }>;
};

export type TargetVillage = {
  order: number;
  slug: string;
  entity_id: string;
  name: string;
  region: string;
  kf_status: "TARGET_SCREENING" | "REFERENCE_ONLY" | "PAUSED" | string;
  screening_role: string;
  ranking_allowed: false;
  reviewed_at: string;
  development_thesis: string;
  coordinates: {
    longitude: number;
    latitude: number;
    geometry_status: string;
    not_facility_coordinate: boolean;
  };
  population: {
    value: number | null;
    year: number | null;
    geography: string | null;
    source: { name: string; url: string; reference_date: string | null } | null;
    note: string | null;
  };
  air: {
    access_known: boolean;
    code: string | null;
    name: string | null;
    runway_length_m: number | null;
    runway_surface: string | null;
    dimension_status: string;
    access_pattern: string;
    load_status: string;
    pavement_strength: string | null;
    max_aircraft_mass_kg: number | null;
    operational_constraints: string[];
    presence_source: { name: string; url: string; reference_date: string | null } | null;
    dimension_source: { name: string; url: string; reference_date: string | null } | null;
    note: string | null;
  };
  marine: {
    access_known: boolean;
    access_mode: string;
    commercial_access: string;
    facilities: Array<{ type: string; label: string; length_m: number | null }>;
    approach_depth_m: number | null;
    anchorage_depth_m: number | null;
    berth_depth_range_m: [number, number] | null;
    depth_status: string;
    ro_ro: boolean | null;
    laydown_available: boolean | null;
    load_limits: {
      status: string;
      deck_load_t_m2: number | null;
      axle_load_t: number | null;
      max_unit_mass_t: number | null;
      crane_swl_t: number | null;
    };
    seasonality: {
      service_type: string;
      start_month: number | null;
      end_month: number | null;
      status: string;
    };
    constraints: string[];
    source_ids: string[];
    baseline_context: string | null;
    baseline_source: { name: string; url: string; reference_date: string | null } | null;
    baseline_note: string | null;
  };
  logistics_envelope: {
    marine_delivery: string;
    air_delivery: string;
    heavy_module_status: "favourable" | "constrained" | "diligence_required" | "unknown" | string;
    assessment_status: "partial" | "research_ready" | "diligence_required" | string;
  };
  system_context: {
    marine: string | null;
    telecom: string | null;
    road: string | null;
    energy: string | null;
  };
  energy_projects: VillageEnergyProject[];
  open_gates: string[];
  sources: VillageSourceReference[];
};

export type TargetVillagePortfolio = {
  schema: "kristal-target-villages/v1";
  generated_at: string;
  portfolio_version: string;
  status: string;
  ranking_allowed: false;
  target_count: number;
  selection_note: string;
  semantics: Record<string, string>;
  items: TargetVillage[];
};
