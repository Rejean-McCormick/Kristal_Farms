from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "contracts/policy/international-tenant-governance.yaml"
MAIN_POLICY = ROOT / "contracts/policy/kristal-farms-policy.yaml"


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


def test_current_us_counterparty_exclusion_does_not_imply_technology_embargo():
    policy = load(POLICY)
    exclusion = policy["owner_directed_exclusions"]["counterparty_jurisdictions"][0]
    assert exclusion["jurisdiction"] == "US"
    assert exclusion["status"] == "INELIGIBLE"
    assert exclusion["technology_origin_embargo_implied"] is False


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
    assert policy["tenant_confidentiality"]["content_blind_by_design"] is True


def test_nonlisted_jurisdictions_default_to_enhanced_due_diligence():
    schedule = load(ROOT / "contracts/policy/jurisdiction-eligibility.yaml")
    assert schedule["default_nonlisted_state"] == "ENHANCED_DUE_DILIGENCE"
    assert schedule["jurisdictions"][0]["code"] == "US"
    assert schedule["jurisdictions"][0]["legal_prohibition_claimed"] is False


def test_tenant_eligibility_record_is_restricted_and_has_categorical_state():
    import json

    schema = json.loads((ROOT / "contracts/schemas/tenant-eligibility-record.schema.json").read_text(encoding="utf-8"))
    assert schema["properties"]["classification"]["const"] == "RESTRICTED"
    assert schema["properties"]["eligibility_state"]["enum"] == [
        "ELIGIBLE",
        "ENHANCED_DUE_DILIGENCE",
        "SUSPENDED",
        "INELIGIBLE",
    ]
