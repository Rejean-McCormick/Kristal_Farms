# Kristal Farms - register one locally served PMTiles archive in Observatory
param(
    [Parameter(Mandatory=$true)][string]$Id,
    [string]$Title = "Local satellite imagery",
    [string]$Source = "Local static satellite snapshot",
    [string]$Acquired = "",
    [string]$License = "",
    [string]$Attribution = "Local imagery snapshot"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Target = Join-Path $Root "apps\web\public\imagery\local-satellite.json"
$TileJsonUrl = "http://127.0.0.1:8765/$Id.json"

Write-Host "Reading $TileJsonUrl ..."
$tilejson = Invoke-RestMethod -Uri $TileJsonUrl -TimeoutSec 10

if (-not $tilejson.tiles -or $tilejson.tiles.Count -lt 1) {
    throw "TileJSON did not contain a tiles URL."
}

$tileTemplate = [string]$tilejson.tiles[0]
$bounds = $null
if ($tilejson.bounds -and $tilejson.bounds.Count -eq 4) {
    $bounds = @([double]$tilejson.bounds[0], [double]$tilejson.bounds[1], [double]$tilejson.bounds[2], [double]$tilejson.bounds[3])
}

$manifest = [ordered]@{
    schema = "kristal-local-imagery/v1"
    id = $Id
    title = $Title
    available = $true
    tile_template = $tileTemplate
    tile_size = 512
    minzoom = [int]$tilejson.minzoom
    maxzoom = [int]$tilejson.maxzoom
    bounds = $bounds
    source = $Source
    acquired = $(if ($Acquired) { $Acquired } else { $null })
    license = $(if ($License) { $License } else { $null })
    attribution = $Attribution
    generated_at = (Get-Date).ToUniversalTime().ToString("o")
}

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Target) | Out-Null
$manifest | ConvertTo-Json -Depth 5 | Set-Content -Path $Target -Encoding UTF8

Write-Host ""
Write-Host "Registered $Id"
Write-Host "Manifest: $Target"
Write-Host "Tiles:    $tileTemplate"
Write-Host "Zoom:     $($manifest.minzoom)-$($manifest.maxzoom)"
Write-Host ""
Write-Host "Restart Observatory if it is already running."
