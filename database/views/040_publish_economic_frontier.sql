CREATE OR REPLACE VIEW publish.economic_benchmarks_v1 AS
SELECT b.benchmark_key,b.category,b.value_numeric,b.unit,b.basis_label,b.benchmark_role,b.usable_as_site_estimate,e.status AS evidence_status,e.confidence
FROM research.economic_benchmark b JOIN research.evidence e ON e.id=b.source_evidence_id;

CREATE OR REPLACE VIEW publish.economic_scenario_results_v1 AS
SELECT r.id,c.name AS comparison_name,r.metric,r.value_numeric,r.value_text,r.unit,r.completeness_status,r.metadata
FROM scenario.result r LEFT JOIN scenario.comparison c ON c.id=r.comparison_id;

CREATE OR REPLACE VIEW publish.economic_sensitivity_cases_v1 AS
SELECT case_key,overrides,results,status,metadata
FROM scenario.sensitivity_case;
