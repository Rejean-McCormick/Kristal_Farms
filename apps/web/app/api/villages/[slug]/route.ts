import { NextResponse } from "next/server";
import { getTargetVillage } from "../../../../lib/server/villages";

export const dynamic = "force-dynamic";

export async function GET(
  _request: Request,
  context: { params: Promise<{ slug: string }> },
) {
  const { slug } = await context.params;
  const village = await getTargetVillage(slug);
  if (!village) return NextResponse.json({ error: "Village not found" }, { status: 404 });
  return NextResponse.json(village, {
    headers: { "Cache-Control": "public, max-age=60, stale-while-revalidate=300" },
  });
}
