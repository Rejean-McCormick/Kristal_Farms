from __future__ import annotations

def reference_frontier(hv_km, road_km, fibre_km, *, tx_low, tx_high, road_low, road_high, fibre_low_proxy, fibre_high_proxy):
    vals=[hv_km,road_km,fibre_km,tx_low,tx_high,road_low,road_high,fibre_low_proxy,fibre_high_proxy]
    if any(v is None for v in vals):
        return {"status":"insufficient","reason":"required reference input missing"}
    if any(v < 0 for v in vals):
        raise ValueError("distances and unit references must be non-negative")
    conventional_low=hv_km*tx_low + road_km*road_low
    conventional_high=hv_km*tx_high + road_km*road_high
    fibre_low=fibre_km*fibre_low_proxy
    fibre_high=fibre_km*fibre_high_proxy
    return {
      "status":"derived_reference_frontier",
      "conventional_export_reference_low_cad":conventional_low,
      "conventional_export_reference_high_cad":conventional_high,
      "fibre_funding_proxy_low_cad":fibre_low,
      "fibre_funding_proxy_high_cad":fibre_high,
      "remaining_unpriced_kristal_farms_budget_conservative_cad":conventional_low-fibre_high,
      "remaining_unpriced_kristal_farms_budget_optimistic_cad":conventional_high-fibre_low,
      "not_net_savings":True,
      "not_site_estimate":True,
      "unpriced_kristal_farms_items_remain_open":True,
    }

def complete_project_economics(*args, **kwargs):
    raise RuntimeError("economic architecture deliberately does not compute bankable project NPV/IRR without complete site-specific capex, opex, revenue, financing, tax, hydrology and engineering inputs.")
