"use client";

import { useCallback, useEffect, useState } from "react";
import { ObservatoryExplorer } from "../explorer/ObservatoryExplorer";
import { InternationalPortfolioExplorer } from "../international/InternationalPortfolioExplorer";

type WorkspaceSection = "atlas" | "international";

function readSection(): WorkspaceSection {
  if (typeof window === "undefined") return "atlas";
  return new URLSearchParams(window.location.search).get("section") === "international"
    ? "international"
    : "atlas";
}

export function KristalObservatoryShell() {
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
    if (next === "international") url.searchParams.set("section", "international");
    else url.searchParams.delete("section");
    window.history.pushState({}, "", url);
  }, []);

  return (
    <div className="kristal-app-shell">
      <header className="kristal-app-shell__bar">
        <button
          type="button"
          className="kristal-app-shell__brand"
          onClick={() => navigate("atlas")}
          aria-label="Open Northern Atlas"
        >
          <span>KRISTAL FARMS</span>
          <strong>OBSERVATORY</strong>
        </button>

        <nav className="kristal-app-shell__nav" aria-label="Kristal Observatory workspaces">
          <button
            type="button"
            className={section === "atlas" ? "is-active" : ""}
            onClick={() => navigate("atlas")}
            aria-pressed={section === "atlas"}
          >
            <span className="kristal-app-shell__nav-index">01</span>
            Northern Atlas
          </button>
          <button
            type="button"
            className={section === "international" ? "is-active" : ""}
            onClick={() => navigate("international")}
            aria-pressed={section === "international"}
          >
            <span className="kristal-app-shell__nav-index">02</span>
            International 12
          </button>
        </nav>

        <div className="kristal-app-shell__context">
          <span>GOVERNED WORKSPACE</span>
          <strong>{section === "atlas" ? "GEOGRAPHY / EVIDENCE" : "COUNTERPARTY / PORTFOLIO"}</strong>
        </div>
      </header>

      <div className="kristal-app-shell__workspace">
        {section === "atlas"
          ? <ObservatoryExplorer embedded />
          : <InternationalPortfolioExplorer embedded />}
      </div>
    </div>
  );
}
