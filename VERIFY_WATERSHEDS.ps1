$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$GeoJson = Join-Path $Root "apps\web\public\data\watersheds\nhn_workunit_limits.geojson"
$Manifest = Join-Path $Root "apps\web\public\data\watersheds\manifest.json"

Write-Host "Kristal watershed overlay verification" -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path $GeoJson)) { throw "Missing $GeoJson" }
if (-not (Test-Path $Manifest)) { throw "Missing $Manifest" }

$payload = Get-Content $GeoJson -Raw | ConvertFrom-Json
$manifestPayload = Get-Content $Manifest -Raw | ConvertFrom-Json
$count = @($payload.features).Count

Write-Host "Status:      $($manifestPayload.status)"
Write-Host "Features:    $count"
Write-Host "Coverage:    $($manifestPayload.coverage)"
Write-Host "Source:      $($manifestPayload.source)"
Write-Host "GeoJSON:     $GeoJson"
Write-Host ""

$Explorer = Join-Path $Root "apps\web\components\explorer\ObservatoryExplorer.tsx"
$Map = Join-Path $Root "apps\web\components\explorer\ObservatoryMap.tsx"
$Types = Join-Path $Root "apps\web\lib\explorer-types.ts"

$checks = @(
    @{ File = $Explorer; Text = "watershed_boundaries" },
    @{ File = $Map; Text = "WATERSHED_SOURCE" },
    @{ File = $Types; Text = "watershed_boundaries: boolean" }
)

foreach ($check in $checks) {
    if (-not (Test-Path $check.File)) { throw "Missing app file: $($check.File)" }
    if (-not (Select-String -Path $check.File -Pattern $check.Text -SimpleMatch -Quiet)) {
        throw "Patch marker '$($check.Text)' missing in $($check.File)"
    }
}

Write-Host "UI patch:    OK" -ForegroundColor Green
if ($count -gt 0) {
    Write-Host "Boundary data: READY" -ForegroundColor Green
} else {
    Write-Host "Boundary data: EMPTY — run FETCH_WATERSHEDS.pyw" -ForegroundColor Yellow
}
