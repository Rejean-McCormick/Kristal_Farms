@echo off
setlocal EnableExtensions
cd /d "%~dp0"
title Kristal Farms Observatory - Quick Start

echo.
echo ================================================
echo   Kristal Farms Observatory - QUICK START
echo ================================================
echo.
echo This shortcut does NOT rebuild or validate the repo.
echo After files change, use REBUILD_OBSERVATORY.pyw instead.
echo.

if not exist "apps\web\package.json" (
  echo ERROR: apps\web\package.json not found.
  pause
  exit /b 1
)

where node >nul 2>&1
if errorlevel 1 (
  echo ERROR: Node.js is not available in PATH.
  pause
  exit /b 1
)
where npm >nul 2>&1
if errorlevel 1 (
  echo ERROR: npm is not available in PATH.
  pause
  exit /b 1
)

pushd "apps\web"
if not exist "node_modules\maplibre-gl\package.json" (
  echo Frontend dependencies missing - running npm ci...
  call npm ci
  if errorlevel 1 (
    popd
    pause
    exit /b 1
  )
)

start "" powershell -NoProfile -WindowStyle Hidden -Command "Start-Sleep -Seconds 3; Start-Process 'http://localhost:3000'"
call npm run dev
set "EXITCODE=%ERRORLEVEL%"
popd

echo.
echo Observatory stopped with exit code %EXITCODE%.
pause
exit /b %EXITCODE%
