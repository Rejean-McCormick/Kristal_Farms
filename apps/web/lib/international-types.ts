export type InternationalEligibilityState =
  | "ELIGIBLE"
  | "ENHANCED_DUE_DILIGENCE"
  | "SUSPENDED"
  | "INELIGIBLE";

export type InternationalOutreachState =
  | "RESEARCH_READY"
  | "DILIGENCE_REQUIRED"
  | "CONDITIONAL_RING_FENCE"
  | "BLOCKED";

export type InternationalSourceReference = {
  id: string;
  title: string;
  publisher: string;
  source_class?: string;
  url: string;
  published_on?: string;
  retrieved_on?: string;
  supports?: string;
  use?: string;
};

export type InternationalCandidate = {
  slot: number;
  slug: string;
  organization: string;
  home_jurisdiction: string;
  home_country: string;
  jurisdiction_state: InternationalEligibilityState;
  outreach_state: InternationalOutreachState;
  engagement_tier: string;
  target_role: string;
  rationale: string;
  hard_gate: string;
  ring_fencing_required: boolean;
  verification_status: string;
  sources: InternationalSourceReference[];
};

export type InternationalServiceOffer = {
  id: string;
  purpose: string;
  indicative_envelope?: string;
};

export type InternationalPortfolio = {
  schema: "kristal-international-portfolio/v1";
  generated_at: string;
  portfolio_version: string;
  status: "RESEARCH_ONLY";
  planning_slots: 12;
  commitments_claimed: false;
  policy_status: string;
  default_nonlisted_state: InternationalEligibilityState;
  service_offers: InternationalServiceOffer[];
  source_methodology: {
    validated_on: string;
    minimum_candidate_source_rule: string;
    interpretation: string;
  };
  policy_summary: {
    ineligible_jurisdictions: Array<{ code: string; name: string }>;
    suspended_jurisdictions: Array<{ code: string; name: string }>;
    counterparty_screening_before_access: boolean;
    technology_origin_embargo_implied: boolean;
    legal_reference_sources: InternationalSourceReference[];
  };
  candidates: InternationalCandidate[];
  disclaimer: string;
};
