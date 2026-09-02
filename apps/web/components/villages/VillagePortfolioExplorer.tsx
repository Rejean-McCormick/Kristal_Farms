"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import type { TargetVillage, TargetVillagePortfolio } from "../../lib/village-types";
import { humanizeToken } from "../../lib/format";
import styles from "./VillagePortfolio.module.css";

export function VillagePortfolioExplorer({ embedded = false }: { embedded?: boolean } = {}) {
  const [portfolio, setPortfolio] = useState<TargetVillagePortfolio | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [query, setQuery] = useState("");
  const [region, setRegion] = useState("ALL");
  const [marineMode, setMarineMode] = useState("ALL");

  useEffect(() => {
    const controller = new AbortController();
    fetch("/api/villages", { signal: controller.signal })
      .then(async (response) => {
        if (!response.ok) throw new Error(`Village portfolio failed (${response.status})`);
        return (await response.json()) as TargetVillagePortfolio;
      })
      .then(setPortfolio)
      .catch((caught: unknown) => {
        if ((caught as Error).name !== "AbortError") setError((caught as Error).message);
      });
    return () => controller.abort();
  }, []);

  const filtered = useMemo(() => {
    if (!portfolio) return [];
    const needle = query.trim().toLowerCase();
    return portfolio.items.filter((village) => {
      const regionMatch = region === "ALL"
        || (region === "NUNAVIK" && village.region.includes("Nunavik"))
        || (region === "NUNATSIAVUT" && village.region.includes("Nunatsiavut"));
      const marineMatch = marineMode === "ALL" || village.marine.access_mode === marineMode;
      const queryMatch = !needle || [
        village.name,
        village.region,
        village.air.code,
        village.marine.access_mode,
        village.screening_role,
      ].filter(Boolean).join(" ").toLowerCase().includes(needle);
      return regionMatch && marineMatch && queryMatch;
    });
  }, [portfolio, query, region, marineMode]);

  if (error) {
    return (
      <main className={`${styles.state} ${embedded ? styles.embeddedState : ""}`}>
        <span>VILLAGE PORTFOLIO</span>
        <h1>Publication unavailable</h1>
        <p>{error}</p>
      </main>
    );
  }

  if (!portfolio) {
    return (
      <main className={`${styles.state} ${embedded ? styles.embeddedState : ""}`}>
        <span>VILLAGE PORTFOLIO</span>
        <strong>Loading governed village dossiers…</strong>
      </main>
    );
  }

  const nunavikCount = portfolio.items.filter((item) => item.region.includes("Nunavik")).length;
  const nunatsiavutCount = portfolio.items.filter((item) => item.region.includes("Nunatsiavut")).length;
  const depthReferenced = portfolio.items.filter((item) => item.marine.depth_status !== "not_verified").length;

  return (
    <main className={`${styles.shell} ${embedded ? styles.embeddedShell : ""}`}>
      <section className={styles.hero}>
        <div>
          <span className={styles.eyebrow}>TARGET VILLAGES / COMMUNITY DOSSIERS</span>
          <h1>One diligence surface for every KF target village.</h1>
          <p>
            Air, marine, seasonality, logistics gates and community-system context are published as evidence-deepening dossiers.
            Inclusion remains unranked and does not imply project selection or cargo certification.
          </p>
        </div>
        <div className={styles.metrics}>
          <Metric value={String(portfolio.target_count)} label="target villages" />
          <Metric value={String(nunavikCount)} label="Nunavik" />
          <Metric value={String(nunatsiavutCount)} label="Nunatsiavut" />
          <Metric value={String(depthReferenced)} label="depth references" />
        </div>
      </section>

      <section className={styles.policyStrip}>
        <div>
          <span>SCREENING MODE</span>
          <strong>UNRANKED · EVIDENCE DEEPENING</strong>
        </div>
        <p>{portfolio.selection_note}</p>
        <span className={styles.policyNote}>Unknown capacity stays unknown.</span>
      </section>

      <section className={styles.catalog}>
        <div className={styles.filters}>
          <label className={styles.searchBox}>
            <span>Search</span>
            <input
              type="search"
              value={query}
              placeholder="Village, airport, region, marine mode…"
              onChange={(event) => setQuery(event.target.value)}
            />
          </label>
          <Filter label="Region" value={region} onChange={setRegion} options={[
            ["ALL", "All regions"],
            ["NUNAVIK", "Nunavik"],
            ["NUNATSIAVUT", "Nunatsiavut"],
          ]} />
          <Filter label="Marine access" value={marineMode} onChange={setMarineMode} options={[
            ["ALL", "All access modes"],
            ["lighterage_beach_ramp", "Lighterage / landing"],
            ["ferry_ro_ro_terminal", "Ferry / Ro-Ro"],
            ["ferry_and_local_ramp", "Ferry / local ramp"],
          ]} />
        </div>

        <div className={styles.catalogHeader}>
          <span>{filtered.length} / {portfolio.target_count} VISIBLE</span>
          <button type="button" onClick={() => { setQuery(""); setRegion("ALL"); setMarineMode("ALL"); }}>
            Reset filters
          </button>
        </div>

        <div className={styles.cards}>
          {filtered.map((village) => <VillageCard key={village.slug} village={village} />)}
          {!filtered.length && <div className={styles.empty}>No village matches the active filters.</div>}
        </div>
      </section>

      <footer className={styles.footer}>
        <span>{portfolio.portfolio_version}</span>
        <span>Ranking disabled · load limits remain unverified unless explicitly published.</span>
        <span>Published {portfolio.generated_at}</span>
      </footer>
    </main>
  );
}

function VillageCard({ village }: { village: TargetVillage }) {
  return (
    <Link href={`/villages/${village.slug}`} className={styles.card}>
      <div className={styles.cardTopline}>
        <span className={styles.slot}>#{String(village.order).padStart(2, "0")}</span>
        <span>{village.region}</span>
      </div>
      <div className={styles.cardTitle}>
        <strong>{village.name}</strong>
        <span>{humanizeToken(village.kf_status)}</span>
      </div>
      <div className={styles.cardFacts}>
        <CardFact label="Population" value={village.population.value != null ? `${village.population.value.toLocaleString("en-CA")} · ${village.population.year ?? "year ?"}` : "Not verified"} />
        <CardFact label="Airport" value={village.air.runway_length_m != null ? `${village.air.code ?? "—"} · ${Math.round(village.air.runway_length_m).toLocaleString("en-CA")} m · ${village.air.runway_surface ?? "surface ?"}` : "Runway not verified"} />
        <CardFact label="Marine" value={humanizeToken(village.marine.access_mode)} />
        <CardFact label="Season" value={seasonLabel(village)} />
      </div>
      <div className={styles.cardGate}>
        <span>LOGISTICS</span>
        <strong>{humanizeToken(village.logistics_envelope.heavy_module_status)}</strong>
        <em>{village.open_gates.length} open gates · full dossier →</em>
      </div>
    </Link>
  );
}

function CardFact({ label, value }: { label: string; value: string }) {
  return <div><span>{label}</span><strong>{value}</strong></div>;
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
        {options.map(([optionValue, optionLabel]) => <option key={optionValue} value={optionValue}>{optionLabel}</option>)}
      </select>
    </label>
  );
}

function seasonLabel(village: TargetVillage): string {
  const { start_month: start, end_month: end } = village.marine.seasonality;
  if (start == null || end == null) return "Not verified";
  return `${monthName(start)}–${monthName(end)} · ${humanizeToken(village.marine.seasonality.service_type)}`;
}

function monthName(month: number): string {
  return new Intl.DateTimeFormat("en-CA", { month: "short", timeZone: "UTC" }).format(new Date(Date.UTC(2026, month - 1, 1)));
}
