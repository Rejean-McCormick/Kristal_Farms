# Kristal Farms - local PMTiles imagery server
$ErrorActionPreference = "Stop"

$Store = "C:\KristalData\imagery\pmtiles"
$Port = 8765
$Origin = "http://localhost:3000"
$Bundled = "C:\KristalData\bin\pmtiles.exe"

New-Item -ItemType Directory -Force -Path $Store | Out-Null

if (Test-Path $Bundled) {
    $Pmtiles = $Bundled
} else {
    $cmd = Get-Command pmtiles -ErrorAction SilentlyContinue
    if (-not $cmd) {
        Write-Host "ERROR: pmtiles CLI not found."
        Write-Host "Put pmtiles.exe at C:\KristalData\bin\pmtiles.exe or add it to PATH."
        exit 1
    }
    $Pmtiles = $cmd.Source
}

$Archives = Get-ChildItem $Store -Filter *.pmtiles -File -ErrorAction SilentlyContinue
if (-not $Archives) {
    Write-Host "No .pmtiles archives found in $Store"
    Write-Host "Create one first, then rerun this script."
    exit 1
}

Write-Host ""
Write-Host "Kristal local imagery server"
Write-Host "Store : $Store"
Write-Host "URL   : http://127.0.0.1:$Port"
Write-Host "CORS  : $Origin"
Write-Host ""
Write-Host "Available archives:"
$Archives | ForEach-Object { Write-Host " - $($_.BaseName)" }
Write-Host ""
Write-Host "Keep this window open while Observatory uses satellite imagery."
Write-Host "Ctrl+C stops the imagery server."
Write-Host ""

& $Pmtiles serve $Store --port=$Port --cors=$Origin --public-url="http://127.0.0.1:$Port"
