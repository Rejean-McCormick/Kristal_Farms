CREATE TABLE IF NOT EXISTS research.economic_benchmark (
  id uuid PRIMARY KEY,
  benchmark_key text NOT NULL UNIQUE,
  category text NOT NULL,
  value_numeric numeric NOT NULL,
  unit text NOT NULL,
  basis_label text NOT NULL,
  source_evidence_id uuid NOT NULL REFERENCES research.evidence(id) ON DELETE RESTRICT,
  benchmark_role text NOT NULL CHECK (benchmark_role IN ('reference_only','proxy_only','context_only')),
  usable_as_site_estimate boolean NOT NULL DEFAULT false,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS scenario.comparison (
  id uuid PRIMARY KEY,
  name text NOT NULL,
  conventional_scenario_id uuid NOT NULL REFERENCES scenario.scenario(id) ON DELETE RESTRICT,
  kristal_scenario_id uuid NOT NULL REFERENCES scenario.scenario(id) ON DELETE RESTRICT,
  comparison_class text NOT NULL,
  status text NOT NULL,
  algorithm_key text NOT NULL,
  algorithm_version text NOT NULL,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS scenario.result (
  id uuid PRIMARY KEY,
  comparison_id uuid REFERENCES scenario.comparison(id) ON DELETE CASCADE,
  scenario_id uuid REFERENCES scenario.scenario(id) ON DELETE CASCADE,
  metric text NOT NULL,
  value_numeric numeric,
  value_text text,
  unit text,
  algorithm_key text NOT NULL,
  algorithm_version text NOT NULL,
  completeness_status text NOT NULL,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  CHECK (value_numeric IS NOT NULL OR value_text IS NOT NULL)
);

CREATE TABLE IF NOT EXISTS scenario.sensitivity_case (
  id uuid PRIMARY KEY,
  comparison_id uuid NOT NULL REFERENCES scenario.comparison(id) ON DELETE CASCADE,
  case_key text NOT NULL,
  overrides jsonb NOT NULL,
  results jsonb NOT NULL,
  status text NOT NULL,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  UNIQUE(comparison_id,case_key)
);

INSERT INTO system.algorithm_registry(algorithm_key,version,semantic_class,description,parameters_schema,prohibited_outputs)
VALUES (
 'economics.enabling_infrastructure_frontier','1.0.0','derived_economic_frontier',
 'Compares evidence-backed project/funding ratios across distance stress cases and solves remaining budget headroom for unpriced Kristal-specific enabling infrastructure. It is not project NPV or savings.',
 '{"hv_distance_km":{"type":"array"},"road_distance_km":{"type":"array"},"fibre_distance_km":{"type":"array"}}'::jsonb,
 ARRAY['project_irr','bankable_npv','site_score','priority_rank','net_savings_claim']
) ON CONFLICT DO NOTHING;
