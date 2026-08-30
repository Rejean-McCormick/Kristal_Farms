CREATE TABLE IF NOT EXISTS system.algorithm_registry (
  algorithm_key text NOT NULL,
  version text NOT NULL,
  semantic_class text NOT NULL,
  description text NOT NULL,
  parameters_schema jsonb NOT NULL DEFAULT '{}'::jsonb,
  prohibited_outputs text[] NOT NULL DEFAULT '{}'::text[],
  status text NOT NULL DEFAULT 'active',
  PRIMARY KEY(algorithm_key,version)
);
INSERT INTO system.algorithm_registry(algorithm_key,version,semantic_class,description,parameters_schema,prohibited_outputs)
VALUES (
 'hydrology.climatological_monthly_mean','1.0.0','derived_hydrology',
 'Computes climatological monthly means from daily mean discharge only after configurable completeness gates. This is a research statistic, not design flow.',
 '{"min_complete_years":{"type":"integer","default":10},"min_year_completeness_fraction":{"type":"number","default":0.90},"min_month_completeness_fraction":{"type":"number","default":0.80}}'::jsonb,
 ARRAY['design_flow_m3s','capacity_mw','project_gross_head_m']
) ON CONFLICT DO NOTHING;
