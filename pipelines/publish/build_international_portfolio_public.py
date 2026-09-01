#!/usr/bin/env python3
"""Publish the governed International 12 research portfolio for read-only product use.

The web application must not read research/ or policy YAML at runtime. This helper
performs the explicit promotion step and writes only the public fields needed by
the International Portfolio interface.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

import yaml

COUNTRY_NAMES = {
    "FR": "France", "KR": "South Korea", "JP": "Japan", "FI": "Finland",
    "GB": "United Kingdom", "DE": "Germany", "AU": "Australia", "NL": "Netherlands",
}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def outreach_state(jurisdiction_state: str, ring_fencing_required: bool) -> str:
    if jurisdiction_state in {"INELIGIBLE", "SUSPENDED"}:
        return "BLOCKED"
    if ring_fencing_required:
        return "CONDITIONAL_RING_FENCE"
    if jurisdiction_state == "ENHANCED_DUE_DILIGENCE":
        return "DILIGENCE_REQUIRED"
    return "RESEARCH_READY"


def build(repo_root: Path) -> dict:
    portfolio = yaml.safe_load((repo_root / "research/commercial/international_portfolio_12.yaml").read_text(encoding="utf-8"))
    policy = yaml.safe_load((repo_root / "contracts/policy/jurisdiction-eligibility.yaml").read_text(encoding="utf-8"))

    candidates = portfolio["candidates"]
    slots = [item["slot"] for item in candidates]
    if portfolio["planning_slots"] != 12 or sorted(slots) != list(range(1, 13)):
        raise SystemExit("International portfolio must contain exactly slots 1..12")
    if len({item["organization"] for item in candidates}) != 12:
        raise SystemExit("International portfolio organizations must be unique")

    state_by_code = {item["code"]: item["state"] for item in policy["jurisdictions"]}
    public_candidates = []
    for item in candidates:
        code = item["home_jurisdiction"]
        jurisdiction_state = state_by_code.get(code, policy["default_nonlisted_state"])
        ring_fencing_required = bool(item.get("ring_fencing_required", False))
        public_candidates.append({
            "slot": item["slot"],
            "slug": slugify(item["organization"]),
            "organization": item["organization"],
            "home_jurisdiction": code,
            "home_country": COUNTRY_NAMES.get(code, code),
            "jurisdiction_state": jurisdiction_state,
            "outreach_state": outreach_state(jurisdiction_state, ring_fencing_required),
            "engagement_tier": item["engagement_tier"],
            "target_role": item["target_role"],
            "rationale": item["rationale"],
            "hard_gate": item["hard_gate"],
            "ring_fencing_required": ring_fencing_required,
        })

    return {
        "schema": "kristal-international-portfolio/v1",
        "generated_at": "2026-08-31",
        "portfolio_version": portfolio["portfolio_version"],
        "status": portfolio["status"],
        "planning_slots": portfolio["planning_slots"],
        "commitments_claimed": portfolio["commitments_claimed"],
        "policy_status": policy.get("policy_status", "CURRENT"),
        "default_nonlisted_state": policy["default_nonlisted_state"],
        "service_offers": [{"id": key, **value} for key, value in portfolio["service_offers"].items()],
        "policy_summary": {
            "ineligible_jurisdictions": [
                {"code": row["code"], "name": row["name"]}
                for row in policy["jurisdictions"] if row["state"] == "INELIGIBLE"
            ],
            "suspended_jurisdictions": [
                {"code": row["code"], "name": row["name"]}
                for row in policy["jurisdictions"] if row["state"] == "SUSPENDED"
            ],
            "counterparty_screening_before_access": True,
            "technology_origin_embargo_implied": False,
        },
        "candidates": public_candidates,
        "disclaimer": "Research portfolio only. Inclusion does not mean interest, commitment, eligibility clearance, or contract.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()
    output = args.output or repo_root / "data/publish/current/international_portfolio_public.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(build(repo_root), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
