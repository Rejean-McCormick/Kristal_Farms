"use client";

import { useEffect, useState } from "react";
import type { EntityDetail, EvidenceRecord } from "../../lib/explorer-types";
import { humanizeToken } from "../../lib/format";
import { RelationConstellation } from "./RelationConstellation";

type InspectorTab = "overview" | "hydrology" | "relations" | "evidence";

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

  const tabs: InspectorTab[] = detail?.screeningDimensions.length
    ? ["overview", "hydrology", "relations", "evidence"]
    : ["overview", "relations", "evidence"];

  return (
    <aside className="inspector" aria-label="Entity inspector">
      <div className="inspector__chrome">
        <span>ENTITY INSPECTOR</span>
        <button type="button" onClick={onClose} aria-label="Close inspector">×</button>
      </div>

      {loading && !detail ? (
        <div className="inspector__loading">
          <span className="scan-line" />
          Loading governed record…
        </div>
      ) : detail ? (
        <>
          <header className="inspector__header">
            <div className="inspector__eyebrow">{kindLabel(detail.featureKind)}</div>
            <h1>{detail.title}</h1>
            {detail.subtitle && <p>{detail.subtitle}</p>}
            <div className="status-row">
              <span className={`status-pill is-${detail.mapGeometryStatus}`}>
                <span aria-hidden="true">{geometryGlyph(detail.mapGeometryStatus)}</span>
                {geometryLabel(detail.mapGeometryStatus)}
              </span>
              {detail.status && <span className="status-pill is-muted">{detail.status}</span>}
            </div>
          </header>

          <nav
            className={`inspector__tabs ${tabs.length === 4 ? "has-four" : ""}`}
            aria-label="Inspector sections"
          >
            {tabs.map((item) => (
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

                <div className={`precision-note is-${detail.mapGeometryStatus}`}>
                  <span className="precision-note__mark" aria-hidden="true">
                    {geometryGlyph(detail.mapGeometryStatus)}
                  </span>
                  <div>
                    <strong>{geometryLabel(detail.mapGeometryStatus)}</strong>
                    <p>{detail.mapNote ?? humanizeToken(detail.geometryRole)}</p>
                  </div>
                </div>

                {detail.featureKind !== "river" && (
                  <button
                    className={`compare-action ${compared ? "is-active" : ""}`}
                    type="button"
                    onClick={() => onAddCompare(detail.entityId)}
                    aria-pressed={compared}
                  >
                    {compared ? "Pinned for comparison" : "Pin for comparison"}
                  </button>
                )}
              </section>
            )}

            {tab === "hydrology" && (
              <section>
                <div className="section-heading">
                  <span>HYDROLOGY / ENGINEERING GATES</span>
                  <small>Evidence state · no site ranking or design inference</small>
                </div>
                {detail.screeningDimensions.length ? (
                  <div className="screening-dimensions">
                    {detail.screeningDimensions.map((dimension) => (
                      <article className="screening-card" key={dimension.id}>
                        <div className="screening-card__header">
                          <span>{dimension.label}</span>
                          <strong className={`screening-state is-${dimension.status}`}>
                            {humanizeToken(dimension.status)}
                          </strong>
                        </div>
                        {dimension.appliesTo && (
                          <div className="screening-card__applies">Applies to {dimension.appliesTo}</div>
                        )}
                        <p>{humanizeToken(dimension.evidenceCompleteness)}</p>
                        {dimension.openQuestions.length > 0 && (
                          <div className="open-questions">
                            <span>OPEN QUESTIONS</span>
                            <ul>
                              {dimension.openQuestions.map((question) => (
                                <li key={question}>{question}</li>
                              ))}
                            </ul>
                          </div>
                        )}
                        {dimension.lastReviewed && (
                          <small>Last reviewed {dimension.lastReviewed}</small>
                        )}
                      </article>
                    ))}
                  </div>
                ) : (
                  <p className="empty-state">No public hydrology screening state is attached.</p>
                )}
              </section>
            )}

            {tab === "relations" && (
              <section>
                <div className="section-heading">
                  <span>RELATION MODEL</span>
                  <small>Screen-space only · no route geometry asserted</small>
                </div>
                {detail.relations.length ? (
                  <RelationConstellation title={detail.title} relations={detail.relations} />
                ) : (
                  <p className="empty-state">No public relation is attached to this entity.</p>
                )}
              </section>
            )}

            {tab === "evidence" && (
              <section>
                <div className="section-heading">
                  <span>EVIDENCE</span>
                  <small>Release {detail.release} · human-readable public records</small>
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
                    {detail.evidenceRecords.length ? (
                      <div className="evidence-records">
                        {detail.evidenceRecords.map((record) => (
                          <EvidenceRecordCard key={record.id} record={record} />
                        ))}
                      </div>
                    ) : (
                      <p className="empty-state evidence-fallback">
                        Evidence summary exists, but human-readable public evidence records are unavailable in this release.
                      </p>
                    )}
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

function EvidenceRecordCard({ record }: { record: EvidenceRecord }) {
  return (
    <article className="evidence-record">
      <div className="evidence-record__header">
        <span>{humanizeToken(record.evidence_type)}</span>
        <strong className={`evidence-status is-${record.status}`}>{humanizeToken(record.status)}</strong>
      </div>
      <p>{record.claim}</p>
      <div className="evidence-record__meta">
        {record.confidence && <span>Confidence · {humanizeToken(record.confidence)}</span>}
        {record.retrieved_at && <span>Retrieved · {record.retrieved_at}</span>}
      </div>
      {record.sources.length > 0 && (
        <div className="evidence-sources">
          {record.sources.map((source) =>
            source.url ? (
              <a key={`${record.id}:${source.id}`} href={source.url} target="_blank" rel="noreferrer">
                <span>{source.publisher ?? humanizeToken(source.source_type)}</span>
                <strong>{source.title}</strong>
                <small>{humanizeToken(source.role)} ↗</small>
              </a>
            ) : (
              <div key={`${record.id}:${source.id}`}>
                <span>{source.publisher ?? humanizeToken(source.source_type)}</span>
                <strong>{source.title}</strong>
              </div>
            ),
          )}
        </div>
      )}
      <code className="evidence-record__id">{record.id}</code>
    </article>
  );
}

function kindLabel(kind: EntityDetail["featureKind"]) {
  if (kind === "community") return "Community";
  if (kind === "river") return "River research reference";
  return "Hydrometric station";
}

function geometryGlyph(status: EntityDetail["mapGeometryStatus"]) {
  if (status === "official") return "●";
  if (status === "approximate") return "◌";
  return "∅";
}

function geometryLabel(status: EntityDetail["mapGeometryStatus"]) {
  if (status === "official") return "Official geometry";
  if (status === "approximate") return "Approximate geometry";
  return "Governed geometry unavailable";
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
