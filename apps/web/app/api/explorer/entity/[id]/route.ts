import { NextResponse } from "next/server";
import { getEntityDetail } from "../../../../../lib/server/public-data";

export const dynamic = "force-dynamic";

export async function GET(
  _request: Request,
  context: { params: Promise<{ id: string }> },
) {
  const { id } = await context.params;
  const entity = await getEntityDetail(id);

  if (!entity) {
    return NextResponse.json({ error: "Entity not found" }, { status: 404 });
  }

  return NextResponse.json(entity, {
    headers: { "Cache-Control": "public, max-age=60, stale-while-revalidate=300" },
  });
}
