INSERT INTO system.metric_registry(metric,unit,semantic_class,display_label,can_drive_compute_capacity,notes) VALUES
('remaining_unpriced_kristal_budget_conservative_cad','CAD','derived_economic_frontier','Remaining unpriced Kristal budget — conservative reference frontier',false,'Not savings/NPV. Uses lower export project ratios and higher fibre funding proxy.'),
('remaining_unpriced_kristal_budget_optimistic_cad','CAD','derived_economic_frontier','Remaining unpriced Kristal budget — optimistic reference frontier',false,'Not savings/NPV. Uses higher export project ratios and lower fibre funding proxy.'),
('conventional_export_reference_capex_cad','CAD','derived_economic_frontier','Conventional export reference envelope',false,'Reference project ratios only; not site estimate.'),
('fibre_funding_proxy_cad','CAD','derived_economic_frontier','Northern fibre funding proxy',false,'Public funding intensity, not total fibre project cost.')
ON CONFLICT(metric) DO UPDATE SET unit=EXCLUDED.unit,semantic_class=EXCLUDED.semantic_class,display_label=EXCLUDED.display_label,can_drive_compute_capacity=EXCLUDED.can_drive_compute_capacity,notes=EXCLUDED.notes;
