"use client";

import { useCallback, useEffect, useState } from "react";
import { ObservatoryExplorer } from "../explorer/ObservatoryExplorer";
import { InternationalPortfolioExplorer } from "../international/InternationalPortfolioExplorer";
import { VillagePortfolioExplorer } from "../villages/VillagePortfolioExplorer";
import styles from "./KristalFarmsObservatoryShell.module.css";

type WorkspaceSection = "atlas" | "villages" | "corridors" | "international" | "economics" | "evidence";

type WorkspaceGroup = "EXPLORE" | "EVALUATE" | "GOVERN";

type SectionDefinition = {
  id: WorkspaceSection;
  index: string;
  label: string;
  group: WorkspaceGroup;
  context: string;
};

const SECTIONS: SectionDefinition[] = [
  { id: "atlas", index: "01", label: "Northern Atlas", group: "EXPLORE", context: "GEOGRAPHY / EVIDENCE" },
  { id: "villages", index: "02", label: "Villages", group: "EXPLORE", context: "COMMUNITIES / DILIGENCE" },
  { id: "corridors", index: "03", label: "Corridors", group: "EXPLORE", context: "DOSSIERS / GATES" },
  { id: "economics", index: "04", label: "Economics", group: "EVALUATE", context: "SCENARIOS / SENSITIVITY" },
  { id: "evidence", index: "05", label: "Evidence", group: "GOVERN", context: "PROVENANCE / CONTROL" },
  { id: "international", index: "06", label: "International Portfolio", group: "GOVERN", context: "COUNTERPARTY / PORTFOLIO" },
];

const SECTION_IDS = new Set<WorkspaceSection>(SECTIONS.map((section) => section.id));

function readSection(): WorkspaceSection {
  if (typeof window === "undefined") return "atlas";
  const raw = new URLSearchParams(window.location.search).get("section");
  return raw && SECTION_IDS.has(raw as WorkspaceSection) ? (raw as WorkspaceSection) : "atlas";
}

export function KristalFarmsObservatoryShell() {
  const [section, setSection] = useState<WorkspaceSection>("atlas");

  useEffect(() => {
    setSection(readSection());
    const onPopState = () => setSection(readSection());
    window.addEventListener("popstate", onPopState);
    return () => window.removeEventListener("popstate", onPopState);
  }, []);

  const navigate = useCallback((next: WorkspaceSection) => {
    setSection(next);
    const url = new URL(window.location.href);
    if (next === "atlas") url.searchParams.delete("section");
    else url.searchParams.set("section", next);
    if (next !== "international") url.searchParams.delete("project");
    window.history.pushState({}, "", url);
  }, []);

  const current = SECTIONS.find((item) => item.id === section) ?? SECTIONS[0];

  return (
    <div className={styles.shell}>
      <header className={styles.bar}>
        <button
          type="button"
          className={styles.brand}
          onClick={() => navigate("atlas")}
          aria-label="Open Kristal Farms Observatory Northern Atlas"
        >
          <span>KRISTAL FARMS</span>
          <strong>OBSERVATORY</strong>
        </button>

        <nav className={styles.nav} aria-label="Kristal Farms Observatory workspaces">
          {SECTIONS.map((item) => (
            <button
              type="button"
              key={item.id}
              className={section === item.id ? styles.active : ""}
              onClick={() => navigate(item.id)}
              aria-pressed={section === item.id}
              title={`${item.group}: ${item.label}`}
            >
              <span className={styles.navMeta}>
                <span>{item.index}</span>
                {item.group}
              </span>
              <strong>{item.label}</strong>
            </button>
          ))}
        </nav>

        <div className={styles.context}>
          <span>{current.group} WORKSPACE</span>
          <strong>{current.context}</strong>
        </div>
      </header>

      <div className={styles.workspace}>
        {section === "atlas" && <ObservatoryExplorer embedded />}
        {section === "villages" && <VillagePortfolioExplorer embedded />}
        {section === "international" && <InternationalPortfolioExplorer embedded />}
        {section === "corridors" && (
          <WorkspaceBrief
            eyebrow="CORRIDOR DOSSIERS"
            title="Turn screening references into decision-grade dossiers."
            status="UNRANKED · EVIDENCE BUILD"
            description="Corridors are the next unit of project development. This workspace is intentionally non-ranking until geometry, hydrology, logistics, rights, community and telecom evidence support a controlled comparison."
            cards={[
              ["Selection", "No preferred corridor selected", "A dossier deepens evidence; it does not declare a winner."],
              ["Required gates", "Hydro · fibre · marine · community · rights", "Unknowns remain explicit until supported by attributable evidence."],
              ["Next product step", "Publish corridor dossier artifacts", "Wire controlled dossier summaries into this surface as they mature."],
            ]}
          />
        )}
        {section === "economics" && (
          <WorkspaceBrief
            eyebrow="ECONOMICS"
            title="Compare architectures without manufacturing bankability."
            status="NON-BANKABLE · SCENARIO ONLY"
            description="Economics remain a scenario and sensitivity workspace. Benchmark ratios, proxy hydrology and conceptual layouts must not be promoted into project CAPEX, NPV or IRR claims."
            cards={[
              ["Comparison", "Equal-scope architectures", "Compare local compute, electrical export and hybrid configurations on the same assumptions."],
              ["Sensitivity", "Power · fibre · cooling · utilization", "Expose assumption ranges instead of hiding uncertainty behind a single headline number."],
              ["Promotion gate", "Vendor + site evidence required", "Bankable economics require project geometry, quotations, service requirements and commercial terms."],
            ]}
          />
        )}
        {section === "evidence" && (
          <WorkspaceBrief
            eyebrow="EVIDENCE CONTROL"
            title="Make every material claim traceable."
            status="EVIDENCE BEFORE RANKING"
            description="The Evidence workspace is the control plane for provenance, conflicts, unknowns and publication status. It should expose what is supported without turning contextual data into authoritative project facts."
            cards={[
              ["Provenance", "Source → evidence → claim", "Keep attributable sources, retrieval dates and transformation lineage visible."],
              ["Uncertainty", "Unknown stays unknown", "Gauge points are not dam sites; terrain drop is not project head; benchmarks are not site costs."],
              ["Publication", "Controlled artifacts only", "Product surfaces consume governed releases rather than research files at runtime."],
            ]}
          />
        )}
      </div>
    </div>
  );
}

function WorkspaceBrief({
  eyebrow,
  title,
  status,
  description,
  cards,
}: {
  eyebrow: string;
  title: string;
  status: string;
  description: string;
  cards: Array<[string, string, string]>;
}) {
  return (
    <main className={styles.brief}>
      <section className={styles.briefHero}>
        <div>
          <span className={styles.eyebrow}>{eyebrow}</span>
          <h1>{title}</h1>
          <p>{description}</p>
        </div>
        <strong className={styles.status}>{status}</strong>
      </section>

      <section className={styles.briefGrid}>
        {cards.map(([label, value, note]) => (
          <article key={label} className={styles.briefCard}>
            <span>{label}</span>
            <strong>{value}</strong>
            <p>{note}</p>
          </article>
        ))}
      </section>

      <section className={styles.briefFooter}>
        <span>KRISTAL FARMS OBSERVATORY</span>
        <p>This surface is a governed workspace scaffold. It does not imply site selection, authorization, commitment or bankability.</p>
      </section>
    </main>
  );
}
