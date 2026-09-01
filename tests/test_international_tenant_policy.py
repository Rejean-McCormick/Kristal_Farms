from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "contracts/policy/international-tenant-governance.yaml"
MAIN_POLICY = ROOT / "contracts/policy/kristal-farms-policy.yaml"
SCHEDULE = ROOT / "contracts/policy/jurisdiction-eligibility.yaml"
PORTFOLIO = ROOT / "research/commercial/international_portfolio_12.yaml"


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_international_policy_is_machine_readable_and_categorical():
    policy = load(POLICY)
    assert policy["eligibility"]["numeric_ethics_score_allowed"] is False
    assert policy["eligibility"]["states"] == [
        "ELIGIBLE",
        "ENHANCED_DUE_DILIGENCE",
        "SUSPENDED",
        "INELIGIBLE",
    ]


def test_proposed_jurisdiction_schedule_contains_expected_hard_exclusions_and_holds():
    schedule = load(SCHEDULE)
    by_code = {row["code"]: row for row in schedule["jurisdictions"]}
    assert schedule["default_nonlisted_state"] == "ENHANCED_DUE_DILIGENCE"
    assert {c for c, r in by_code.items() if r["state"] == "INELIGIBLE"} == {
        "US", "RU", "BY", "CN", "IR", "KP", "SY", "MM"
    }
    assert {c for c, r in by_code.items() if r["state"] == "SUSPENDED"} == {
        "AF", "LY", "NI", "SO", "SD", "SS", "VE", "YE", "ZW"
    }
    assert all(r["technology_origin_embargo_implied"] is False for r in by_code.values())


def test_downstream_resale_inherits_eligibility_boundary_without_content_inspection():
    policy = load(POLICY)
    downstream = policy["downstream_tenancy"]
    assert downstream["eligibility_boundary_inherited_by_resellers_and_subtenants"] is True
    assert downstream["unverified_global_resale_pool_allowed"] is False
    assert downstream["dedicated_capacity_pool_required_when_global_pool_can_serve_ineligible_counterparties"] is True
    assert downstream["commercial_allocation_records_auditable"] is True
    assert downstream["private_workload_content_auditable"] is False


def test_black_box_policy_forbids_routine_private_content_inspection():
    policy = load(POLICY)
    black_box = policy["black_box_tenancy"]
    assert black_box["content_blind_by_design"] is True
    assert black_box["routine_plaintext_application_access_allowed"] is False
    assert black_box["routine_private_model_inspection_allowed"] is False
    assert black_box["routine_private_dataset_inspection_allowed"] is False
    assert black_box["operator_key_escrow_required"] is False
    assert black_box["standing_decryption_backdoor_allowed"] is False


def test_main_policy_points_to_international_policy_contract():
    policy = load(MAIN_POLICY)
    assert policy["international_tenancy"]["policy_contract"] == "international-tenant-governance.yaml"
    assert policy["international_tenancy"]["jurisdiction_schedule_enforced"] is True
    assert policy["international_tenancy"]["downstream_counterparties_inherit_eligibility"] is True
    assert policy["international_tenancy"]["unverified_global_resale_pool_allowed"] is False
    assert policy["tenant_confidentiality"]["content_blind_by_design"] is True


def test_portfolio_has_12_unique_research_slots_and_no_commitment_claim():
    portfolio = load(PORTFOLIO)
    candidates = portfolio["candidates"]
    assert portfolio["planning_slots"] == 12
    assert portfolio["commitments_claimed"] is False
    assert len(candidates) == 12
    assert {c["slot"] for c in candidates} == set(range(1, 13))
    assert len({c["organization"] for c in candidates}) == 12
    assert all(c["home_jurisdiction"] != "US" for c in candidates)


def test_conditional_nebius_slot_requires_ring_fencing():
    portfolio = load(PORTFOLIO)
    nebius = next(c for c in portfolio["candidates"] if c["organization"] == "Nebius")
    assert nebius["engagement_tier"] == "CONDITIONAL_ONLY"
    assert nebius["ring_fencing_required"] is True


def test_tenant_eligibility_record_is_restricted_and_has_categorical_state():
    schema = json.loads((ROOT / "contracts/schemas/tenant-eligibility-record.schema.json").read_text(encoding="utf-8"))
    assert schema["properties"]["classification"]["const"] == "RESTRICTED"
    assert schema["properties"]["eligibility_state"]["enum"] == [
        "ELIGIBLE",
        "ENHANCED_DUE_DILIGENCE",
        "SUSPENDED",
        "INELIGIBLE",
    ]
