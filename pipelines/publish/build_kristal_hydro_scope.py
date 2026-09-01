#!/usr/bin/env python3
"""Publish the Kristal coastal hydro screening scope.

Raw evidence stays untouched. This publisher creates a conservative, auditable
product-facing scope for the current Kristal Farms model.

Core map scope:
- coastal/community-scale
- no operating/committed/retired/altered hydro
- no named large-grid hydro context
- close to an active Labrador community
- close to the source mouth/coast proxy

Extended review references are retained in the audit/public payload but are not
shown by default in Observatory.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
PUBLISH = ROOT / "data" / "publish" / "current"
PROCESSED = ROOT / "data" / "processed" / "current"

HYDRO_POINTS = RAW / "labrador_hydro_google_mymaps_points_v1.csv"
VILLAGE_INVENTORY = RAW / "kristal_farms_village_inventory.csv"

CORE_MAX_COMMUNITY_KM = 50.0
CORE_MAX_COAST_PROXY_KM = 25.0
EXTENDED_MAX_COMMUNITY_KM = 75.0
EXTENDED_MAX_COAST_PROXY_KM = 30.0

STATUS_EXCLUDE_TOKENS = (
    "operating",
    "harnessed",
    "planned",
    "under agreement",
    "former",
    "retired",
    "partly altered",
    "partially altered",
    "partially harnessed",
    "current status needs confirmation",
    "interprovincial",
)

GRID_CONTEXT_NAME_TOKENS = (
    "churchill falls",
    "muskrat falls",
    "gull island",
    "lower churchill",
    "twin falls",
    "menihek",
)

ACTIVE_VILLAGE_CATEGORIES = (
    "A - Priority target",
    "D - Nunavik screening pool",
    "E - Nunatsiavut screening pool",
)


def haversine_km(a: tuple[float, float], b: tuple[float, float]) -> float:
    lon1, lat1 = a
    lon2, lat2 = b
    radius_km = 6371.0088
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    h = math.sin(dlat / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlon / 2) ** 2
    return 2 * radius_km * math.asin(math.sqrt(h))


def read_active_villages() -> list[dict]:
    villages: list[dict] = []
    with VILLAGE_INVENTORY.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("category") not in ACTIVE_VILLAGE_CATEGORIES:
                continue
            if "Labrador" not in (row.get("region") or ""):
                continue
            villages.append(row)
    return villages


def load_community_coordinates() -> dict[str, tuple[float, float]]:
    path = PUBLISH / "communities_public.geojson"
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    output: dict[str, tuple[float, float]] = {}
    for feature in payload.get("features", []):
        name = str(feature.get("properties", {}).get("name") or "").strip()
        coords = feature.get("geometry", {}).get("coordinates")
        if name and isinstance(coords, list) and len(coords) >= 2:
            output[name] = (float(coords[0]), float(coords[1]))
    return output


def parse_float(value: str | None) -> float | None:
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def lower(value: str | None) -> str:
    return (value or "").strip().lower()


def classify_geometry(confidence: str) -> str:
    text = confidence.lower()
    if "exact" in text or "strong proxy" in text:
        return "named_or_strong_proxy"
    if "gauge" in text:
        return "gauge_proxy"
    if "river-point" in text or "river point" in text:
        return "river_proxy"
    if "approximate" in text or "manual" in text:
        return "approximate_reference"
    return "reference_geometry"


def hard_exclusion_reasons(row: dict) -> list[str]:
    reasons: list[str] = []
    status = lower(row.get("Current_status"))
    combined_name = " ".join(
        [
            lower(row.get("Map_Name")),
            lower(row.get("Hydro_site_or_reference")),
            lower(row.get("River_or_watercourse")),
        ]
    )

    if lower(row.get("Point_Mappable")) != "yes":
        reasons.append("not_mappable")
    if any(token in status for token in STATUS_EXCLUDE_TOKENS):
        reasons.append("existing_committed_or_non_target_status")
    if any(token in combined_name for token in GRID_CONTEXT_NAME_TOKENS):
        reasons.append("known_large_grid_hydro_context")
    return reasons


def scope_class(
    *,
    hard_reasons: list[str],
    nearest_community_km: float | None,
    coast_proxy_km: float | None,
    core_community_km: float,
    core_coast_km: float,
    extended_community_km: float,
    extended_coast_km: float,
) -> tuple[str, list[str]]:
    reasons = list(hard_reasons)
    if reasons:
        return "excluded", reasons

    if nearest_community_km is None:
        return "excluded", ["no_active_community_distance"]
    if coast_proxy_km is None:
        return "excluded", ["no_coast_mouth_proxy"]

    if nearest_community_km <= core_community_km and coast_proxy_km <= core_coast_km:
        return "core", []

    if nearest_community_km <= extended_community_km and coast_proxy_km <= extended_coast_km:
        extended_reasons: list[str] = []
        if nearest_community_km > core_community_km:
            extended_reasons.append("outside_core_community_distance")
        if coast_proxy_km > core_coast_km:
            extended_reasons.append("outside_core_coast_distance")
        return "extended_review", extended_reasons

    if nearest_community_km > extended_community_km:
        reasons.append("too_far_from_active_community")
    if coast_proxy_km > extended_coast_km:
        reasons.append("too_far_inland_from_coast_proxy")
    return "excluded", reasons


def public_site(
    row: dict,
    *,
    entry_id: str,
    lat: float,
    lon: float,
    nearest_name: str | None,
    nearest_km: float | None,
    coast_km: float | None,
    coast_point: tuple[float, float] | None,
    scope: str,
) -> dict:
    return {
        "id": row.get("Feature_ID") or entry_id,
        "entry_id": entry_id,
        "name": row.get("Map_Name") or row.get("Hydro_site_or_reference") or row.get("River_or_watercourse"),
        "river_name": row.get("River_or_watercourse"),
        "capacity_or_potential": row.get("Capacity_or_potential") or None,
        "current_status": row.get("Current_status") or None,
        "geometry_confidence": row.get("Dam_point_confidence") or None,
        "geometry_class": classify_geometry(row.get("Dam_point_confidence") or ""),
        "geometry_role": "screening_reference_not_engineered_dam_site",
        "coordinates": [lon, lat],
        "nearest_active_community": nearest_name,
        "distance_to_active_community_km": round(nearest_km, 2) if nearest_km is not None else None,
        "distance_to_mouth_or_coast_proxy_km": round(coast_km, 2) if coast_km is not None else None,
        "mouth_or_coast_proxy": list(coast_point) if coast_point else None,
        "mapping_note": row.get("Mapping_note") or None,
        "source_notes": row.get("Source_URLs_or_notes") or None,
        "screening_scope": scope,
        "ranking_allowed": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core-community-km", type=float, default=CORE_MAX_COMMUNITY_KM)
    parser.add_argument("--core-coast-km", type=float, default=CORE_MAX_COAST_PROXY_KM)
    parser.add_argument("--extended-community-km", type=float, default=EXTENDED_MAX_COMMUNITY_KM)
    parser.add_argument("--extended-coast-km", type=float, default=EXTENDED_MAX_COAST_PROXY_KM)
    args = parser.parse_args()

    active_villages = read_active_villages()
    community_coords = load_community_coordinates()
    active_points = [
        (row["village_community"], community_coords[row["village_community"]])
        for row in active_villages
        if row.get("village_community") in community_coords
    ]

    grouped: dict[str, dict[str, dict]] = {}
    with HYDRO_POINTS.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            grouped.setdefault(row["Entry_ID"], {})[row["Point_Role"]] = row

    audit_rows: list[dict] = []
    core_sites: list[dict] = []
    review_sites: list[dict] = []

    for entry_id, parts in grouped.items():
        row = parts.get("Dam_or_site")
        if not row:
            continue

        lat = parse_float(row.get("Latitude"))
        lon = parse_float(row.get("Longitude"))
        if lat is None or lon is None:
            continue
        site_point = (lon, lat)

        nearest_name: str | None = None
        nearest_km: float | None = None
        for name, point in active_points:
            distance = haversine_km(site_point, point)
            if nearest_km is None or distance < nearest_km:
                nearest_name = name
                nearest_km = distance

        coast_row = parts.get("Mouth_or_coast")
        coast_km: float | None = None
        coast_point: tuple[float, float] | None = None
        if coast_row:
            coast_lat = parse_float(coast_row.get("Latitude"))
            coast_lon = parse_float(coast_row.get("Longitude"))
            if coast_lat is not None and coast_lon is not None:
                coast_point = (coast_lon, coast_lat)
                coast_km = haversine_km(site_point, coast_point)

        decision, reasons = scope_class(
            hard_reasons=hard_exclusion_reasons(row),
            nearest_community_km=nearest_km,
            coast_proxy_km=coast_km,
            core_community_km=args.core_community_km,
            core_coast_km=args.core_coast_km,
            extended_community_km=args.extended_community_km,
            extended_coast_km=args.extended_coast_km,
        )

        audit_rows.append(
            {
                "entry_id": entry_id,
                "feature_id": row.get("Feature_ID"),
                "name": row.get("Map_Name"),
                "river": row.get("River_or_watercourse"),
                "capacity_or_potential": row.get("Capacity_or_potential"),
                "current_status": row.get("Current_status"),
                "geometry_confidence": row.get("Dam_point_confidence"),
                "geometry_class": classify_geometry(row.get("Dam_point_confidence") or ""),
                "latitude": lat,
                "longitude": lon,
                "nearest_active_community": nearest_name,
                "distance_to_active_community_km": round(nearest_km, 2) if nearest_km is not None else "",
                "distance_to_mouth_or_coast_proxy_km": round(coast_km, 2) if coast_km is not None else "",
                "scope_class": decision,
                "reason_codes": ";".join(reasons),
            }
        )

        if decision == "core":
            core_sites.append(
                public_site(
                    row,
                    entry_id=entry_id,
                    lat=lat,
                    lon=lon,
                    nearest_name=nearest_name,
                    nearest_km=nearest_km,
                    coast_km=coast_km,
                    coast_point=coast_point,
                    scope="coastal_core",
                )
            )
        elif decision == "extended_review":
            review_sites.append(
                public_site(
                    row,
                    entry_id=entry_id,
                    lat=lat,
                    lon=lon,
                    nearest_name=nearest_name,
                    nearest_km=nearest_km,
                    coast_km=coast_km,
                    coast_point=coast_point,
                    scope="coastal_extended_review",
                )
            )

    PUBLISH.mkdir(parents=True, exist_ok=True)
    PROCESSED.mkdir(parents=True, exist_ok=True)

    payload = {
        "schema": "kristal-hydro-screening-scope/v2",
        "screening_mode": "unranked",
        "ranking_allowed": False,
        "model_scope": {
            "description": "Coastal/community-scale hydro screening; existing/committed large-grid hydro is outside active scope.",
            "core": {
                "max_distance_to_active_community_km": args.core_community_km,
                "max_distance_to_mouth_or_coast_proxy_km": args.core_coast_km,
            },
            "extended_review": {
                "max_distance_to_active_community_km": args.extended_community_km,
                "max_distance_to_mouth_or_coast_proxy_km": args.extended_coast_km,
            },
            "active_labrador_communities": [name for name, _ in active_points],
            "grid_exclusion_method": "named/status-based until authoritative transmission geometry is ingested",
            "site_geometry_policy": "proxy/gauge/approximate points are screening references, not dam sites",
        },
        "sites": sorted(core_sites, key=lambda row: (row.get("nearest_active_community") or "", row["name"])),
        "review_sites": sorted(review_sites, key=lambda row: (row.get("nearest_active_community") or "", row["name"])),
    }

    public_path = PUBLISH / "kristal_hydro_screening_scope_public.json"
    public_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    audit_path = PROCESSED / "kristal_hydro_screening_scope_audit.csv"
    fieldnames = list(audit_rows[0].keys()) if audit_rows else []
    with audit_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(audit_rows)

    counts = {"core": 0, "extended_review": 0, "excluded": 0}
    for row in audit_rows:
        counts[row["scope_class"]] += 1
    print(
        f"Core {counts['core']} · extended review {counts['extended_review']} · "
        f"excluded {counts['excluded']} · total {len(audit_rows)}"
    )
    print(public_path.relative_to(ROOT))
    print(audit_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
