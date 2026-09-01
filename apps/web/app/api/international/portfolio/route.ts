import { NextResponse } from "next/server";
import { getInternationalPortfolio } from "../../../../lib/server/international-portfolio";

export const dynamic = "force-dynamic";

export async function GET() {
  const payload = await getInternationalPortfolio();
  return NextResponse.json(payload, {
    headers: { "Cache-Control": "public, max-age=60, stale-while-revalidate=300" },
  });
}
