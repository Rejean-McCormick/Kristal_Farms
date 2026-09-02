import { NextResponse } from "next/server";
import { getTargetVillagePortfolio } from "../../../lib/server/villages";

export const dynamic = "force-dynamic";

export async function GET() {
  const payload = await getTargetVillagePortfolio();
  return NextResponse.json(payload, {
    headers: { "Cache-Control": "public, max-age=60, stale-while-revalidate=300" },
  });
}
