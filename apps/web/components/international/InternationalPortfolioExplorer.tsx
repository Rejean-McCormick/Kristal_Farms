"use client";

import { useEffect, useMemo, useState } from "react";
import type {
  InternationalCandidate,
  InternationalPortfolio,
  InternationalSourceReference,
} from "../../lib/international-types";
import styles from "./InternationalPortfolioExplorer.module.css";

const ROLE_LABELS: Record<string, string> = {
  ANCHOR_AI_CAMPUS: "Anchor AI campus",
  FLEXIBLE_TRAINING_NODE: "Flexible training node",
  AIDC_DEVELOPMENT_PARTNERSHIP: "AIDC development",
  SELECTIVE_SOVEREIGN_NODE: "Sovereign / private node",
};

const TIER_LABELS: Record<string, string> = {
  CORE_OUTREACH: "Core outreach",
  SECONDARY_OUTREACH: "Secondary",
  STRATEGIC_EXPLORATION: "Strategic exploration",
  SELECTIVE_OUTREACH: "Selective",
  CONDITIONAL_ONLY: "Conditional only",
};

const OUTREACH_LABELS: Record<string, string> = {
  RESEARCH_READY: "Research ready",
  DILIGENCE_REQUIRED: "EDD required",
  CONDITIONAL_RING_FENCE: "Ring-fence required",
  BLOCKED: "Blocked",
};

export function InternationalPortfolioExplorer({ embedded = false }: { embedded?: boolean } = {}) {
  const [portfolio, setPortfolio] = useState<InternationalPortfolio | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selectedSlug, setSelectedSlug] = useState<string | null>(null);
  const [query, setQuery] = useState("");
  const [role, setRole] = useState("ALL");
  const [tier, setTier] = useState("ALL");
  const [country, setCountry] = useState("ALL");

  useEffect(() => {
    const controller = new AbortController();
    fetch("/api/international/portfolio", { signal: controller.signal })
      .then(async (response) => {
        if (!response.ok) throw new Error(`Portfolio failed (${response.status})`);
        return (await response.json()) as InternationalPortfolio;
      })
      .then((payload) => {
        setPortfolio(payload);
        const slug = new URLSearchParams(window.location.search).get("project");
        const initial = payload.candidates.find((candidate) => candidate.slug === slug)?.slug
          ?? payload.candidates[0]?.slug
          ?? null;
        setSelectedSlug(initial);
      })
      .catch((caught: unknown) => {
        if ((caught as Error).name !== "AbortError") setError((caught as Error).message);
      });
    return () => controller.abort();
  }, []);

  const countries = useMemo(() => {
    if (!portfolio) return [];
    return [...new Map(
      portfolio.candidates.map((candidate) => [candidate.home_jurisdiction, candidate.home_country] as [string, string]),
    ).entries()].sort((a, b) => a[1].localeCompare(b[1]));
  }, [portfolio]);

  const filtered = useMemo(() => {
    if (!portfolio) return [];
    const normalized = query.trim().toLocaleLowerCase();
    return portfolio.candidates.filter((candidate) => {
      const matchesQuery = !normalized || [
        candidate.organization,
        candidate.home_country,
        candidate.home_jurisdiction,
        candidate.rationale,
        candidate.hard_gate,
        ROLE_LABELS[candidate.target_role] ?? candidate.target_role,
        ...candidate.sources.flatMap((source) => [source.title, source.publisher, source.supports ?? ""]),
      ].join(" ").toLocaleLowerCase().includes(normalized);
      return matchesQuery
        && (role === "ALL" || candidate.target_role === role)
        && (tier === "ALL" || candidate.engagement_tier === tier)
        && (country === "ALL" || candidate.home_jurisdiction === country);
    });
  }, [portfolio, query, role, tier, country]);

  const selected = useMemo(
    () => portfolio?.candidates.find((candidate) => candidate.slug === selectedSlug) ?? null,
    [portfolio, selectedSlug],
  );

  function selectProject(candidate: InternationalCandidate) {
    setSelectedSlug(candidate.slug);
    const url = new URL(window.location.href);
    url.searchParams.set("project", candidate.slug);
    window.history.replaceState({}, "", url);
  }

  if (error) {
    return (
      <main className={`${styles.fatal} ${embedded ? styles.embeddedState : ""}`}>
        <span>KRISTAL / INTERNATIONAL PORTFOLIO</span>
        <h1>Portfolio unavailable</h1>
        <p>{error}</p>
        <a href="/">Return to Northern Atlas</a>
      </main>
    );
  }

  if (!portfolio) {
    return (
      <main className={`${styles.boot} ${embedded ? styles.embeddedState : ""}`}>
        <span>KRISTAL / INTERNATIONAL PORTFOLIO</span>
        <strong>Loading governed portfolio</strong>
      </main>
    );
  }

  const ringFenceCount = portfolio.candidates.filter((candidate) => candidate.ring_fencing_required).length;
  const uniqueCountries = new Set(portfolio.candidates.map((candidate) => candidate.home_jurisdiction)).size;

  return (
    <main className={`${styles.shell} ${embedded ? styles.embeddedShell : ""}`}>
      {!embedded && (
        <header className={styles.header}>
          <div className={styles.brand}>
            <span>KRISTAL / INTERNATIONAL PORTFOLIO</span>
            <strong>PORTFOLIO OBSERVATORY · RESEARCH ONLY</strong>
          </div>
          <nav className={styles.nav} aria-label="Primary navigation">
            <a href="/">Northern Atlas</a>
            <a className={styles.activeNav} href="/international">International Portfolio</a>
          </nav>
        </header>
      )}

      <section className={styles.hero}>
        <div>
          <span className={styles.eyebrow}>12-POSITION INTERNATIONAL COMPUTE PORTFOLIO</span>
          <h1>Navigate the twelve research projects.</h1>
          <p>
            Different roles, one governed admission boundary: jurisdiction first, counterparty diligence second,
            contract third. No organization shown here is represented as interested, committed or contracted.
          </p>
        </div>
        <div className={styles.metrics} aria-label="Portfolio summary">
          <Metric value="12" label="portfolio slots" />
          <Metric value={String(uniqueCountries)} label="home jurisdictions" />
          <Metric value={String(portfolio.service_offers.length)} label="service offers" />
          <Metric value={String(ringFenceCount)} label="ring-fence flag" />
        </div>
      </section>

      <section className={styles.policyStrip}>
        <div>
          <span>POLICY GATE</span>
          <strong>{portfolio.policy_status.replaceAll("_", " ")}</strong>
        </div>
        <p>
          {portfolio.policy_summary.ineligible_jurisdictions.length} jurisdictions marked ineligible · {" "}
          {portfolio.policy_summary.suspended_jurisdictions.length} suspended · non-listed jurisdictions default to {" "}
          {portfolio.default_nonlisted_state.replaceAll("_", " ").toLowerCase()}.
        </p>
        <span className={styles.policyNote}>Technology origin remains a separate control.</span>
      </section>

      <section className={styles.workspace}>
        <div className={styles.catalog}>
          <div className={styles.filters}>
            <label className={styles.searchBox}>
              <span>Search</span>
              <input
                type="search"
                placeholder="Organization, country, role, hard gate…"
                value={query}
                onChange={(event) => setQuery(event.target.value)}
              />
            </label>
            <Filter label="Role" value={role} onChange={setRole} options={[
              ["ALL", "All roles"],
              ...portfolio.service_offers.map((offer) => [offer.id, ROLE_LABELS[offer.id] ?? offer.id] as [string, string]),
            ]} />
            <Filter label="Tier" value={tier} onChange={setTier} options={[
              ["ALL", "All tiers"],
              ...[...new Set(portfolio.candidates.map((candidate) => candidate.engagement_tier))]
                .map((value) => [value, TIER_LABELS[value] ?? value] as [string, string]),
            ]} />
            <Filter label="Country" value={country} onChange={setCountry} options={[
              ["ALL", "All countries"],
              ...countries.map(([code, name]) => [code, `${name} · ${code}`] as [string, string]),
            ]} />
          </div>

          <div className={styles.catalogHeader}>
            <span>{filtered.length} / 12 VISIBLE</span>
            <button type="button" onClick={() => { setQuery(""); setRole("ALL"); setTier("ALL"); setCountry("ALL"); }}>
              Reset filters
            </button>
          </div>

          <div className={styles.cards}>
            {filtered.map((candidate) => (
              <button
                key={candidate.slug}
                type="button"
                className={`${styles.card} ${selectedSlug === candidate.slug ? styles.selectedCard : ""}`}
                onClick={() => selectProject(candidate)}
                aria-pressed={selectedSlug === candidate.slug}
              >
                <div className={styles.cardTopline}>
                  <span className={styles.slot}>#{String(candidate.slot).padStart(2, "0")}</span>
                  <span>{candidate.home_country} · {candidate.home_jurisdiction}</span>
                </div>
                <strong>{candidate.organization}</strong>
                <span className={styles.role}>{ROLE_LABELS[candidate.target_role] ?? candidate.target_role}</span>
                <div className={styles.badges}>
                  <Badge value={candidate.engagement_tier} label={TIER_LABELS[candidate.engagement_tier] ?? candidate.engagement_tier} />
                  <Badge value={candidate.outreach_state} label={OUTREACH_LABELS[candidate.outreach_state] ?? candidate.outreach_state} />
                </div>
                <p>{candidate.rationale}</p>
                <div className={styles.cardGate}>
                  <span>HARD GATE</span>
                  <em>{candidate.hard_gate}</em>
                </div>
              </button>
            ))}
            {!filtered.length && <div className={styles.empty}>No project matches the active filters.</div>}
          </div>
        </div>

        <aside className={styles.inspector} aria-label="Selected international project">
          {selected ? (
            <ProjectInspector candidate={selected} portfolio={portfolio} />
          ) : (
            <div className={styles.inspectorEmpty}>Select a project.</div>
          )}
        </aside>
      </section>

      <footer className={styles.footer}>
        <span>{portfolio.portfolio_version}</span>
        <span>{portfolio.disclaimer}</span>
        <span>Published {portfolio.generated_at}</span>
      </footer>
    </main>
  );
}

function Metric({ value, label }: { value: string; label: string }) {
  return <div><strong>{value}</strong><span>{label}</span></div>;
}

function Filter({
  label,
  value,
  onChange,
  options,
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  options: Array<[string, string]>;
}) {
  return (
    <label className={styles.filter}>
      <span>{label}</span>
      <select value={value} onChange={(event) => onChange(event.target.value)}>
        {options.map(([optionValue, optionLabel]) => (
          <option key={optionValue} value={optionValue}>{optionLabel}</option>
        ))}
      </select>
    </label>
  );
}

function Badge({ value, label }: { value: string; label: string }) {
  return <span className={`${styles.badge} ${styles[`badge_${value}`] ?? ""}`}>{label}</span>;
}

function ProjectInspector({
  candidate,
  portfolio,
}: {
  candidate: InternationalCandidate;
  portfolio: InternationalPortfolio;
}) {
  const offer = portfolio.service_offers.find((item) => item.id === candidate.target_role);
  return (
    <div className={styles.inspectorInner}>
      <div className={styles.inspectorChrome}>
        <span>SLOT {String(candidate.slot).padStart(2, "0")} / 12</span>
        <span>{candidate.home_country} · {candidate.home_jurisdiction}</span>
      </div>
      <div className={styles.inspectorTitle}>
        <span>RESEARCH CANDIDATE</span>
        <h2>{candidate.organization}</h2>
        <p>{ROLE_LABELS[candidate.target_role] ?? candidate.target_role}</p>
      </div>

      <div className={styles.inspectorStatus}>
        <Badge value={candidate.engagement_tier} label={TIER_LABELS[candidate.engagement_tier] ?? candidate.engagement_tier} />
        <Badge value={candidate.outreach_state} label={OUTREACH_LABELS[candidate.outreach_state] ?? candidate.outreach_state} />
      </div>

      <section className={styles.detailSection}>
        <span>WHY IT IS IN THE 12</span>
        <p>{candidate.rationale}</p>
      </section>

      <section className={styles.detailSection}>
        <span>DECISION GATE</span>
        <strong>{candidate.hard_gate}</strong>
      </section>

      <section className={styles.detailSection}>
        <span>REFERENCES</span>
        <SourceList sources={candidate.sources} />
        <p className={styles.sourceCaution}>{portfolio.source_methodology.interpretation}</p>
      </section>

      <section className={styles.detailGrid}>
        <div><span>Jurisdiction state</span><strong>{candidate.jurisdiction_state.replaceAll("_", " ")}</strong></div>
        <div><span>Outreach state</span><strong>{OUTREACH_LABELS[candidate.outreach_state] ?? candidate.outreach_state}</strong></div>
        <div><span>Ring fencing</span><strong>{candidate.ring_fencing_required ? "REQUIRED" : "NOT FLAGGED"}</strong></div>
        <div><span>Commitment</span><strong>NONE CLAIMED</strong></div>
        <div><span>Evidence status</span><strong>{candidate.verification_status.replaceAll("_", " ")}</strong></div>
        <div><span>Validated</span><strong>{portfolio.source_methodology.validated_on}</strong></div>
      </section>

      {offer && (
        <section className={styles.offerBox}>
          <span>KRISTAL SERVICE OFFER</span>
          <strong>{ROLE_LABELS[offer.id] ?? offer.id}</strong>
          <p>{offer.purpose}</p>
          {offer.indicative_envelope && <em>{offer.indicative_envelope}</em>}
        </section>
      )}

      <section className={styles.boundaryBox}>
        <span>GOVERNANCE BOUNDARY</span>
        <ul>
          <li>Beneficial ownership and effective control must be verified before contracting.</li>
          <li>Downstream resale/subletting remains inside the same eligibility boundary.</li>
          <li>Eligibility audits concern counterparties and allocation records, not private workload content.</li>
          <li>U.S.-origin technology is not automatically prohibited by the counterparty policy.</li>
        </ul>
      </section>

      <section className={styles.detailSection}>
        <span>POLICY / LEGAL LOOKUP SOURCES</span>
        <SourceList sources={portfolio.policy_summary.legal_reference_sources} />
      </section>
    </div>
  );
}

function SourceList({ sources }: { sources: InternationalSourceReference[] }) {
  return (
    <ul className={styles.sourceList}>
      {sources.map((source) => (
        <li key={source.id}>
          <a href={source.url} target="_blank" rel="noreferrer noopener">{source.title}</a>
          <small>
            {source.publisher}
            {source.published_on ? ` · ${source.published_on}` : ""}
          </small>
          {source.supports && <p>{source.supports}</p>}
          {source.use && <p>{source.use}</p>}
        </li>
      ))}
    </ul>
  );
}
