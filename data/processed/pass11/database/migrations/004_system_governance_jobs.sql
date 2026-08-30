CREATE TABLE IF NOT EXISTS system.governance_state (
  singleton boolean PRIMARY KEY DEFAULT true CHECK (singleton),
  screening_mode text NOT NULL DEFAULT 'unranked', ranking_allowed boolean NOT NULL DEFAULT false,
  effective_from date NOT NULL, metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
INSERT INTO system.governance_state(singleton,screening_mode,ranking_allowed,effective_from,metadata)
VALUES (true,'unranked',false,DATE '2026-08-30','{"source":"Kristal platform architecture v0.1"}'::jsonb)
ON CONFLICT(singleton) DO UPDATE SET screening_mode=EXCLUDED.screening_mode, ranking_allowed=EXCLUDED.ranking_allowed, effective_from=EXCLUDED.effective_from, metadata=EXCLUDED.metadata;

CREATE TABLE IF NOT EXISTS system.metric_registry (
  metric text PRIMARY KEY, unit text, semantic_class text NOT NULL, display_label text NOT NULL,
  can_drive_compute_capacity boolean NOT NULL DEFAULT false, notes text
);

CREATE TABLE IF NOT EXISTS system.ingestion_job (
  id uuid PRIMARY KEY, job_type text NOT NULL, subject_entity_id uuid REFERENCES core.entity(id) ON DELETE CASCADE,
  status text NOT NULL, source_id uuid REFERENCES research.source(id) ON DELETE RESTRICT, endpoint_or_resource text,
  request_geometry geometry(Geometry,4326), metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(), updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS system_ingestion_job_geom_gix ON system.ingestion_job USING gist(request_geometry);

CREATE TABLE IF NOT EXISTS system.dataset_schema (
  id uuid PRIMARY KEY, schema_key text NOT NULL UNIQUE, name text NOT NULL, geometry_type text, verification_status text,
  source_ids uuid[] NOT NULL DEFAULT '{}'::uuid[], schema_definition jsonb NOT NULL DEFAULT '{}'::jsonb,
  last_verified date, metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
