import Link from "next/link";
import type { ReactNode } from "react";
import type { TargetVillage } from "../../lib/village-types";
import { humanizeToken } from "../../lib/format";
import styles from "./VillagePortfolio.module.css";

export function VillageDossier({ village }: { village: TargetVillage }) {
  const atlasView = `/?view=${village.coordinates.longitude},${village.coordinates.latitude},7,0,0`;
  return (
    <main className={`${styles.shell} ${styles.dossierShell}`}>
      <header className={styles.dossierHeader}>
        <Link href="/?section=villages" className={styles.backLink}>← Villages</Link>
        <div className={styles.dossierHeaderTitle}>
          <span>KRISTAL FARMS · TARGET VILLAGE DOSSIER</span>
          <strong>{village.name}</strong>
        </div>
        <Link href={atlasView} className={styles.atlasLink}>Open in Northern Atlas</Link>
      </header>

      <section className={styles.dossierHero}>
        <div>
          <span className={styles.eyebrow}>{village.screening_role}</span>
          <h1>{village.name}</h1>
          <p>{village.region}</p>
          <div className={styles.heroBadges}>
            <Badge>{humanizeToken(village.kf_status)}</Badge>
            <Badge>UNRANKED</Badge>
            <Badge>{humanizeToken(village.logistics_envelope.assessment_status)}</Badge>
          </div>
        </div>
        <div className={styles.heroSnapshot}>
          <Snapshot label="Population" value={village.population.value != null ? village.population.value.toLocaleString("en-CA") : "Not verified"} note={village.population.year ? String(village.population.year) : undefined} />
          <Snapshot label="Airport" value={village.air.code ?? "—"} note={village.air.runway_length_m != null ? `${Math.round(village.air.runway_length_m).toLocaleString("en-CA")} m · ${village.air.runway_surface ?? "surface ?"}` : "runway not verified"} />
          <Snapshot label="Marine" value={humanizeToken(village.marine.access_mode)} note={seasonText(village)} />
          <Snapshot label="Open gates" value={String(village.open_gates.length)} note={`reviewed ${village.reviewed_at}`} />
        </div>
      </section>

      <section className={styles.thesisStrip}>
        <span>KF DEVELOPMENT THESIS</span>
        <p>{village.development_thesis}</p>
      </section>

      <div className={styles.dossierGrid}>
        <section className={styles.dossierSection}>
          <SectionHeading index="01" title="Air logistics" subtitle="Runway dimensions are context, not aircraft certification." />
          <div className={styles.factMatrix}>
            <Fact label="Airport" value={[village.air.name, village.air.code].filter(Boolean).join(" · ") || "Not verified"} />
            <Fact label="Runway" value={village.air.runway_length_m != null ? `${Math.round(village.air.runway_length_m).toLocaleString("en-CA")} m` : "Not verified"} />
            <Fact label="Surface" value={village.air.runway_surface ? humanizeToken(village.air.runway_surface) : "Not verified"} />
            <Fact label="Access pattern" value={humanizeToken(village.air.access_pattern)} />
            <Fact label="Pavement strength" value={village.air.pavement_strength ?? "NOT VERIFIED"} state={village.air.pavement_strength ? "known" : "unknown"} />
            <Fact label="Aircraft mass limit" value={village.air.max_aircraft_mass_kg != null ? `${village.air.max_aircraft_mass_kg.toLocaleString("en-CA")} kg` : "NOT VERIFIED"} state={village.air.max_aircraft_mass_kg != null ? "known" : "unknown"} />
          </div>
          <TokenList title="Operational constraints" items={village.air.operational_constraints} />
          {village.air.note && <p className={styles.sectionNote}>{village.air.note}</p>}
        </section>

        <section className={styles.dossierSection}>
          <SectionHeading index="02" title="Marine logistics" subtitle="Approach, anchorage and berth depths are kept separate." />
          <div className={styles.factMatrix}>
            <Fact label="Access model" value={humanizeToken(village.marine.access_mode)} />
            <Fact label="Commercial access" value={humanizeToken(village.marine.commercial_access)} />
            <Fact label="Approach depth" value={depth(village.marine.approach_depth_m)} state={village.marine.approach_depth_m != null ? "known" : "unknown"} />
            <Fact label="Anchorage depth" value={depth(village.marine.anchorage_depth_m)} state={village.marine.anchorage_depth_m != null ? "known" : "unknown"} />
            <Fact label="Berth depth" value={rangeDepth(village.marine.berth_depth_range_m)} state={village.marine.berth_depth_range_m ? "known" : "unknown"} />
            <Fact label="Depth evidence" value={humanizeToken(village.marine.depth_status)} />
            <Fact label="Ro-Ro" value={boolText(village.marine.ro_ro)} state={village.marine.ro_ro == null ? "unknown" : "known"} />
            <Fact label="Laydown" value={boolText(village.marine.laydown_available)} state={village.marine.laydown_available == null ? "unknown" : "known"} />
          </div>

          <div className={styles.facilities}>
            {village.marine.facilities.map((facility, index) => (
              <article key={`${facility.type}-${index}`}>
                <span>{humanizeToken(facility.type)}</span>
                <strong>{facility.label}</strong>
                <em>{facility.length_m != null ? `${facility.length_m.toLocaleString("en-CA")} m` : "dimension not verified"}</em>
              </article>
            ))}
          </div>

          <div className={styles.loadBox}>
            <div className={styles.loadBoxHeading}>
              <span>MARINE LOAD LIMITS</span>
              <strong>{humanizeToken(village.marine.load_limits.status)}</strong>
            </div>
            <div className={styles.loadGrid}>
              <Fact label="Deck load" value={tonnage(village.marine.load_limits.deck_load_t_m2, "t/m²")} state="unknown" />
              <Fact label="Axle load" value={tonnage(village.marine.load_limits.axle_load_t, "t")} state="unknown" />
              <Fact label="Max unit mass" value={tonnage(village.marine.load_limits.max_unit_mass_t, "t")} state="unknown" />
              <Fact label="Crane SWL" value={tonnage(village.marine.load_limits.crane_swl_t, "t")} state="unknown" />
            </div>
          </div>

          <TokenList title="Marine constraints" items={village.marine.constraints} />
        </section>

        <section className={styles.dossierSection}>
          <SectionHeading index="03" title="Logistics envelope" subtitle="Planning envelope only; no heavy-cargo certification is inferred." />
          <div className={styles.envelopeGrid}>
            <Envelope label="Marine delivery" value={humanizeToken(village.logistics_envelope.marine_delivery)} />
            <Envelope label="Air delivery" value={humanizeToken(village.logistics_envelope.air_delivery)} />
            <Envelope label="Heavy module" value={humanizeToken(village.logistics_envelope.heavy_module_status)} />
            <Envelope label="Assessment" value={humanizeToken(village.logistics_envelope.assessment_status)} />
          </div>
          <div className={styles.gates}>
            <span>OPEN LOGISTICS GATES</span>
            {village.open_gates.map((gate) => (
              <div key={gate}><i aria-hidden="true">○</i><strong>{humanizeToken(gate)}</strong><em>Not verified</em></div>
            ))}
          </div>
        </section>

        <section className={styles.dossierSection}>
          <SectionHeading index="04" title="Community-system context" subtitle="Contextual records for the next diligence layers." />
          <div className={styles.factMatrix}>
            <Fact label="Telecom" value={humanizeToken(village.system_context.telecom)} state={village.system_context.telecom ? "known" : "unknown"} />
            <Fact label="Energy" value={humanizeToken(village.system_context.energy)} state={village.system_context.energy ? "known" : "unknown"} />
            <Fact label="Road" value={humanizeToken(village.system_context.road)} state={village.system_context.road ? "known" : "unknown"} />
            <Fact label="Marine baseline" value={humanizeToken(village.system_context.marine)} state={village.system_context.marine ? "known" : "unknown"} />
            <Fact label="Longitude" value={`${Math.abs(village.coordinates.longitude).toFixed(4)}° W`} />
            <Fact label="Latitude" value={`${Math.abs(village.coordinates.latitude).toFixed(4)}° N`} />
          </div>
          <p className={styles.sectionNote}>Village coordinates are approximate community references and are not facility coordinates.</p>
        </section>

        <section className={styles.dossierSection}>
          <SectionHeading index="05" title="Electrical system & projects" subtitle="External references stay separate from the existing-grid layer; status is never promoted by the interface." />
          <div className={styles.factMatrix}>
            <Fact label="Baseline" value={humanizeToken(village.system_context.energy)} state={village.system_context.energy ? "known" : "unknown"} />
            <Fact label="Documented projects" value={String(village.energy_projects.length)} state={village.energy_projects.length ? "known" : "unknown"} />
          </div>
          {village.energy_projects.length ? (
            <>
              <div className={styles.facilities}>
                {village.energy_projects.map((project) => (
                  <article key={project.entity_id}>
                    <span>{humanizeToken(project.status)}</span>
                    <strong>{project.name}</strong>
                    <em>{energyProjectSummary(project)}</em>
                  </article>
                ))}
              </div>
              <div className={styles.sources}>
                {uniqueEnergySources(village).map((source) => (
                  <a key={source.id} href={source.url} target="_blank" rel="noreferrer">
                    <span>{humanizeToken(source.source_type)}</span>
                    <strong>{source.title}</strong>
                    <em>{source.publisher}{source.publication_date ? ` · ${source.publication_date}` : ""}</em>
                  </a>
                ))}
              </div>
            </>
          ) : (
            <p className={styles.sectionNote}>No additional governed external energy project is linked to this target village in the current public release.</p>
          )}
          <p className={styles.sectionNote}>Study, funded, rejected and active projects are context only. Null geometry does not imply a route, and no project here is a Kristal Farms candidate.</p>
        </section>

        <section className={`${styles.dossierSection} ${styles.sourcesSection}`}>
          <SectionHeading index="06" title="Evidence & sources" subtitle="Research references used for logistics deepening." />
          <div className={styles.sources}>
            {village.sources.map((source) => (
              <a key={source.id} href={source.url} target="_blank" rel="noreferrer">
                <span>{humanizeToken(source.role)}</span>
                <strong>{source.title}</strong>
                <em>{source.publisher}</em>
              </a>
            ))}
            {village.air.dimension_source && (
              <a href={village.air.dimension_source.url} target="_blank" rel="noreferrer">
                <span>AIRPORT DIMENSION SOURCE</span>
                <strong>{village.air.dimension_source.name}</strong>
                <em>{village.air.dimension_source.reference_date ?? "current reference"}</em>
              </a>
            )}
          </div>
        </section>
      </div>

      <footer className={styles.dossierFooter}>
        <span>{village.entity_id}</span>
        <p>Target-village research dossier · ranking disabled · null means not verified, not zero.</p>
      </footer>
    </main>
  );
}

function SectionHeading({ index, title, subtitle }: { index: string; title: string; subtitle: string }) {
  return <header className={styles.sectionHeading}><span>{index}</span><div><h2>{title}</h2><p>{subtitle}</p></div></header>;
}
function Snapshot({ label, value, note }: { label: string; value: string; note?: string }) {
  return <div><span>{label}</span><strong>{value}</strong>{note && <em>{note}</em>}</div>;
}
function Fact({ label, value, state = "known" }: { label: string; value: string; state?: "known" | "unknown" }) {
  return <div className={styles.fact}><span>{label}</span><strong className={state === "unknown" ? styles.unknown : ""}>{value}</strong></div>;
}
function Envelope({ label, value }: { label: string; value: string }) {
  return <div><span>{label}</span><strong>{value}</strong></div>;
}
function Badge({ children }: { children: ReactNode }) { return <span className={styles.badge}>{children}</span>; }
function TokenList({ title, items }: { title: string; items: string[] }) {
  return <div className={styles.tokenList}><span>{title}</span><div>{items.map((item) => <em key={item}>{humanizeToken(item)}</em>)}</div></div>;
}
function energyProjectSummary(project: TargetVillage["energy_projects"][number]) {
  const parts: string[] = [];
  if (project.technology) parts.push(humanizeToken(project.technology));
  if (project.capacity_mw != null) {
    const value = project.capacity_mw < 1 ? `${Math.round(project.capacity_mw * 1000)} kW` : `${project.capacity_mw.toLocaleString("en-CA")} MW`;
    parts.push(value);
  }
  const voltage = project.metadata?.voltage_kv;
  if (typeof voltage === "number") parts.push(`${voltage.toLocaleString("en-CA")} kV`);
  return parts.join(" · ") || humanizeToken(project.project_type);
}
function uniqueEnergySources(village: TargetVillage) {
  const seen = new Set<string>();
  return village.energy_projects.flatMap((project) => project.sources).filter((source) => {
    if (seen.has(source.id)) return false;
    seen.add(source.id);
    return true;
  });
}
function depth(value: number | null) { return value == null ? "NOT VERIFIED" : `${value.toLocaleString("en-CA")} m`; }
function rangeDepth(value: [number, number] | null) { return value ? `${value[0].toLocaleString("en-CA")}–${value[1].toLocaleString("en-CA")} m` : "NOT VERIFIED"; }
function tonnage(value: number | null, unit: string) { return value == null ? "NOT VERIFIED" : `${value.toLocaleString("en-CA")} ${unit}`; }
function boolText(value: boolean | null) { return value == null ? "NOT VERIFIED" : value ? "Yes" : "No"; }
function seasonText(village: TargetVillage) {
  const { start_month: start, end_month: end } = village.marine.seasonality;
  if (start == null || end == null) return "season not verified";
  const fmt = new Intl.DateTimeFormat("en-CA", { month: "short", timeZone: "UTC" });
  const m = (n: number) => fmt.format(new Date(Date.UTC(2026, n - 1, 1)));
  return `${m(start)}–${m(end)} · ${humanizeToken(village.marine.seasonality.service_type)}`;
}
