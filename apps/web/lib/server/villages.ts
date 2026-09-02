import "server-only";

import { readFile } from "node:fs/promises";
import path from "node:path";
import type { TargetVillage, TargetVillagePortfolio } from "../village-types";

const workingDirectory = process.cwd();
const repoRoot = process.env.KRISTAL_REPO_ROOT
  ? path.resolve(process.env.KRISTAL_REPO_ROOT)
  : workingDirectory.endsWith(path.join("apps", "web"))
    ? path.resolve(workingDirectory, "../..")
    : workingDirectory;

const villagesPath = path.join(
  repoRoot,
  "data",
  "publish",
  "current",
  "target_villages_public.json",
);

export async function getTargetVillagePortfolio(): Promise<TargetVillagePortfolio> {
  const payload = JSON.parse(await readFile(villagesPath, "utf8")) as TargetVillagePortfolio;
  if (
    payload.schema !== "kristal-target-villages/v1"
    || payload.ranking_allowed !== false
    || payload.target_count !== payload.items.length
  ) {
    throw new Error("Invalid target village publication");
  }
  return payload;
}

export async function getTargetVillage(slug: string): Promise<TargetVillage | null> {
  const portfolio = await getTargetVillagePortfolio();
  return portfolio.items.find((item) => item.slug === slug) ?? null;
}
