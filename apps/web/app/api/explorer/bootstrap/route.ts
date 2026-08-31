import { NextResponse } from "next/server";
import { getExplorerBootstrap } from "../../../../lib/server/public-data";

export const dynamic = "force-dynamic";

export async function GET() {
  const payload = await getExplorerBootstrap();
  return NextResponse.json(payload, {
    headers: { "Cache-Control": "public, max-age=60, stale-while-revalidate=300" },
  });
}
