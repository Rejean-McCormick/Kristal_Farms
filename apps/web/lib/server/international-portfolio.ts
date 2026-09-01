import "server-only";

import { readFile } from "node:fs/promises";
import path from "node:path";
import type { InternationalPortfolio } from "../international-types";

const workingDirectory = process.cwd();
const repoRoot = process.env.KRISTAL_REPO_ROOT
  ? path.resolve(process.env.KRISTAL_REPO_ROOT)
  : workingDirectory.endsWith(path.join("apps", "web"))
    ? path.resolve(workingDirectory, "../..")
    : workingDirectory;

const portfolioPath = path.join(
  repoRoot,
  "data",
  "publish",
  "current",
  "international_portfolio_public.json",
);

export async function getInternationalPortfolio(): Promise<InternationalPortfolio> {
  const payload = JSON.parse(await readFile(portfolioPath, "utf8")) as InternationalPortfolio;
  if (payload.schema !== "kristal-international-portfolio/v1" || payload.planning_slots !== 12) {
    throw new Error("Invalid international portfolio publication");
  }
  return payload;
}
