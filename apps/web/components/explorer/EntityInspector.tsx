"use client";

import { useEffect, useState } from "react";
import type { EntityDetail } from "../../lib/explorer-types";
import { humanizeToken } from "../../lib/format";
import { RelationConstellation } from "./RelationConstellation";

type InspectorTab = "overview" | "relations" | "evidence";

type Props = {
  entityId: string | null;
  onClose: () => void;
  onAddCompare: (entityId: string) => void;
  compared: boolean;
};

export function EntityInspector({ entityId, onClose, onAddCompare, compared }: Props) {
  const [detail, setDetail] = useState<EntityDetail | null>(null);
  const [loading, setLoading] = useState(false);
  const [tab, setTab] = useState<InspectorTab>("overview");

  useEffect(() => {
    if (!entityId) {
      setDetail(null);
      return;
    }

    const controller = new AbortController();
    setLoading(true);
    setTab("overview");

    fetch(`/api/explorer/entity/${encodeURIComponent(entityId)}`, { signal: controller.signal })
      .then(async (response) => {
        if (!response.ok) throw new Error(`Entity request failed (${response.status})`);
        return (await response.json()) as EntityDetail;
      })
      .then(setDetail)
      .catch((error: unknown) => {
        if ((error as Error).name !== "AbortError") console.error(error);
      })
      .finally(() => setLoading(false));

    return () => controller.abort();
  }, [entityId]);

  if (!entityId) return null;

  return (
    <aside className="inspector" aria-label="Entity inspector">
      <div className="inspector__chrome">
        <span>ENTITY INSPECTOR</span>
        <button type="button" onClick={onClose} aria-label="Close inspector">
          ×
        </button>
      </div>

      {loading && !detail ? (
        <div className="inspector__loading">
          <span className="scan-line" />
          Loading governed record…
        </div>
      ) : detail ? (
        <>
          <header className="inspector__header">
            <div className="inspector__eyebrow">
              {detail.featureKind === "community" ? "Community" : "Hydrometric station"}
            </div>
            <h1>{detail.title}</h1>
            {detail.subtitle && <p>{detail.subtitle}</p>}
            <div className="status-row">
              <span className="status-pill">
                <span aria-hidden="true">{detail.geometryPrecision === "official" ? "●" : "◌"}</span>
                {detail.geometryPrecision === "official" ? "Official geometry" : "Approximate geometry"}
              </span>
              {detail.status && <span className="status-pill is-muted">{detail.status}</span>}
            </div>
          </header>

          <nav className="inspector__tabs" aria-label="Inspector sections">
            {(["overview", "relations", "evidence"] as const).map((item) => (
              <button
                type="button"
                key={item}
                className={tab === item ? "is-active" : ""}
                onClick={() => setTab(item)}
              >
                {item}
              </button>
            ))}
          </nav>

          <div className="inspector__body">
            {tab === "overview" && (
              <section>
                <div className="fact-grid">
                  {detail.facts.map((item) => (
                    <div className="fact" key={item.label}>
                      <span>{item.label}</span>
                      <strong>{item.value}</strong>
                    </div>
                  ))}
                </div>

                <div className="precision-note">
                  <span className="precision-note__mark" aria-hidden="true">
                    {detail.notFacilityCoordinate ? "◌" : "+"}
                  </span>
                  <div>
                    <strong>{detail.notFacilityCoordinate ? "Reference geometry" : "Published geometry"}</strong>
                    <p>
                      {detail.notFacilityCoordinate
                        ? "This coordinate is an approximate community reference and must not be interpreted as a facility location."
                        : humanizeToken(detail.geometryRole)}
                    </p>
                  </div>
                </div>

                <button
                  className={`compare-action ${compared ? "is-active" : ""}`}
                  type="button"
                  onClick={() => onAddCompare(detail.entityId)}
                  aria-pressed={compared}
                >
                  {compared ? "Pinned for comparison" : "Pin for comparison"}
                </button>
              </section>
            )}

            {tab === "relations" && (
              <section>
                <div className="section-heading">
                  <span>RELATION MODEL</span>
                  <small>Screen-space only · no route geometry asserted</small>
                </div>
                <RelationConstellation title={detail.title} relations={detail.relations} />
              </section>
            )}

            {tab === "evidence" && (
              <section>
                <div className="section-heading">
                  <span>EVIDENCE SUMMARY</span>
                  <small>Release {detail.release}</small>
                </div>
                {detail.evidence ? (
                  <>
                    <div className="evidence-metrics">
                      <EvidenceMetric label="Facts" value={detail.evidence.facts} glyph="●" />
                      <EvidenceMetric label="Supported" value={detail.evidence.supported} glyph="◉" />
                      <EvidenceMetric label="Conflicting" value={detail.evidence.conflicting} glyph="◐" />
                      <EvidenceMetric
                        label="Unknown"
                        value={detail.evidence.unverified_or_unknown}
                        glyph="?"
                      />
                    </div>
                    <div className="evidence-ids">
                      <span>Evidence records</span>
                      {detail.evidence.evidence_ids.map((id) => (
                        <code key={id}>{id}</code>
                      ))}
                    </div>
                  </>
                ) : (
                  <p className="empty-state">
                    No public evidence summary is attached to this entity in the current release.
                  </p>
                )}
              </section>
            )}
          </div>

          <footer className="inspector__footer">
            <span>Release {detail.release}</span>
            <span>Ranking disabled</span>
          </footer>
        </>
      ) : (
        <div className="empty-state">The entity could not be loaded.</div>
      )}
    </aside>
  );
}

function EvidenceMetric({ label, value, glyph }: { label: string; value: number; glyph: string }) {
  return (
    <div className="evidence-metric">
      <span aria-hidden="true">{glyph}</span>
      <strong>{value}</strong>
      <small>{label}</small>
    </div>
  );
}
