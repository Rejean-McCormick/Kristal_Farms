CREATE TABLE IF NOT EXISTS scenario.scenario (
  id uuid PRIMARY KEY, name text NOT NULL, description text, owner text, status text NOT NULL CHECK (status IN ('draft','working','shared','archived')),
  created_at timestamptz NOT NULL DEFAULT now(), updated_at timestamptz NOT NULL DEFAULT now(), base_dataset_version text NOT NULL,
  geometry geometry(Geometry,4326), metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
CREATE TABLE IF NOT EXISTS scenario.assumption (
  id uuid PRIMARY KEY, scenario_id uuid NOT NULL REFERENCES scenario.scenario(id) ON DELETE CASCADE, parameter text NOT NULL,
  value_numeric numeric, value_text text, unit text, source_type text NOT NULL CHECK (source_type IN ('user_input','engineering_assumption','derived','evidence','default')),
  evidence_id uuid REFERENCES research.evidence(id) ON DELETE RESTRICT, notes text, metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  CHECK (value_numeric IS NOT NULL OR value_text IS NOT NULL)
);
