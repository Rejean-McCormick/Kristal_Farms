-- Canonical entity supertype: gives evidence/observations a real FK target.
CREATE TABLE IF NOT EXISTS core.entity (
  id uuid PRIMARY KEY,
  canonical_key text NOT NULL UNIQUE,
  entity_type text NOT NULL CHECK (entity_type IN ('place','asset','project','corridor','natural_feature')),
  name text NOT NULL,
  status text,
  visibility text NOT NULL DEFAULT 'PUBLIC' CHECK (visibility IN ('PUBLIC','PARTNER','INTERNAL','RESTRICTED')),
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS core.place (
  entity_id uuid PRIMARY KEY REFERENCES core.entity(id) ON DELETE CASCADE,
  place_type text NOT NULL, geometry geometry(Geometry,4326), jurisdiction text, metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
CREATE INDEX IF NOT EXISTS core_place_geom_gix ON core.place USING gist (geometry);

CREATE TABLE IF NOT EXISTS core.asset (
  entity_id uuid PRIMARY KEY REFERENCES core.entity(id) ON DELETE CASCADE,
  asset_type text NOT NULL, technology text, geometry geometry(Geometry,4326), operator text, operational_status text,
  commissioned_date date, capacity_value numeric, capacity_unit text, metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
CREATE INDEX IF NOT EXISTS core_asset_geom_gix ON core.asset USING gist (geometry);

CREATE TABLE IF NOT EXISTS core.project (
  entity_id uuid PRIMARY KEY REFERENCES core.entity(id) ON DELETE CASCADE,
  project_type text NOT NULL, role text NOT NULL CHECK (role IN ('external_reference','kristal_candidate','kristal_project')),
  project_status text, geometry geometry(Geometry,4326), developer text, operator text, technology text, capacity_mw numeric,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
CREATE INDEX IF NOT EXISTS core_project_geom_gix ON core.project USING gist (geometry);

CREATE TABLE IF NOT EXISTS core.corridor (
  entity_id uuid PRIMARY KEY REFERENCES core.entity(id) ON DELETE CASCADE,
  corridor_type text NOT NULL CHECK (corridor_type IN ('road','marine','transmission','distribution','fibre','conceptual')),
  corridor_status text, geometry geometry(Geometry,4326), operator text, metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
CREATE INDEX IF NOT EXISTS core_corridor_geom_gix ON core.corridor USING gist (geometry);

-- Pass 11 refinement required by Hydro Resource Atlas. Rivers, watersheds and reaches are natural features, not projects.
CREATE TABLE IF NOT EXISTS core.natural_feature (
  entity_id uuid PRIMARY KEY REFERENCES core.entity(id) ON DELETE CASCADE,
  feature_type text NOT NULL CHECK (feature_type IN ('river','watershed','river_reach','lake','coastline','other')),
  geometry geometry(Geometry,4326), jurisdiction text, feature_status text, metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
CREATE INDEX IF NOT EXISTS core_natural_feature_geom_gix ON core.natural_feature USING gist (geometry);

CREATE TABLE IF NOT EXISTS core.entity_relation (
  id uuid PRIMARY KEY, from_entity_id uuid NOT NULL REFERENCES core.entity(id) ON DELETE CASCADE,
  to_entity_id uuid NOT NULL REFERENCES core.entity(id) ON DELETE CASCADE, relation_type text NOT NULL,
  valid_from date, valid_to date, metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  UNIQUE(from_entity_id,to_entity_id,relation_type)
);
