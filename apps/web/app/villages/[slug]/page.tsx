import { notFound } from "next/navigation";
import { VillageDossier } from "../../../components/villages/VillageDossier";
import { getTargetVillage } from "../../../lib/server/villages";

export const dynamic = "force-dynamic";

export default async function VillagePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const village = await getTargetVillage(slug);
  if (!village) return notFound();
  return <VillageDossier village={village} />;
}
