"use client";

import { useMemo, useState } from "react";
import type { RelationItem } from "../../lib/explorer-types";

export function RelationConstellation({
  title,
  relations,
}: {
  title: string;
  relations: RelationItem[];
}) {
  const [activeId, setActiveId] = useState(relations[0]?.id ?? null);
  const active = relations.find((relation) => relation.id === activeId) ?? relations[0] ?? null;

  const nodes = useMemo(() => relations.slice(0, 4), [relations]);

  if (nodes.length === 0) {
    return <p className="empty-state">No published non-geographic relations for this entity.</p>;
  }

  return (
    <div className="constellation">
      <div className="constellation__plot" aria-label={`Relations for ${title}`}>
        <svg className="constellation__lines" viewBox="0 0 320 250" aria-hidden="true">
          {nodes.map((node, index) => {
            const [x, y] = nodePosition(index);
            return <line key={node.id} x1="160" y1="125" x2={x} y2={y} />;
          })}
        </svg>
        <div className="constellation__center" title={title}>
          <span>◎</span>
          <strong>{shortTitle(title)}</strong>
        </div>
        {nodes.map((node, index) => {
          const [x, y] = nodePosition(index);
          return (
            <button
              type="button"
              key={node.id}
              className={`constellation__node ${active?.id === node.id ? "is-active" : ""}`}
              style={{ left: `${(x / 320) * 100}%`, top: `${(y / 250) * 100}%` }}
              onClick={() => setActiveId(node.id)}
              aria-pressed={active?.id === node.id}
            >
              <span aria-hidden="true">○</span>
              {node.label}
            </button>
          );
        })}
      </div>

      {active && (
        <div className="constellation__detail">
          <span>{active.label}</span>
          <strong>{active.value}</strong>
          <small>{active.kind === "entity" ? "Entity relation" : "Context relation · not geometry"}</small>
        </div>
      )}
    </div>
  );
}

function nodePosition(index: number): [number, number] {
  const positions: Array<[number, number]> = [
    [160, 26],
    [282, 125],
    [160, 224],
    [38, 125],
  ];
  return positions[index] ?? [160, 26];
}

function shortTitle(title: string): string {
  if (title.length <= 16) return title;
  return `${title.slice(0, 14)}…`;
}
