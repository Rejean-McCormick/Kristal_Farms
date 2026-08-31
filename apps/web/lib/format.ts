export function humanizeToken(value: string | null | undefined): string {
  if (!value) return "Unknown";
  return value
    .replaceAll("_", " ")
    .replace(/\b\w/g, (letter) => letter.toUpperCase())
    .replace("14 Port", "14-port");
}

export function formatCoordinate(value: number, positive: string, negative: string): string {
  const suffix = value >= 0 ? positive : negative;
  return `${Math.abs(value).toFixed(5)}° ${suffix}`;
}

export function formatNumber(value: number | null | undefined): string {
  if (value === null || value === undefined) return "Unknown";
  return new Intl.NumberFormat("en-CA", { maximumFractionDigits: 1 }).format(value);
}
