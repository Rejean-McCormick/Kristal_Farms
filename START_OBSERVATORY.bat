@echo off
setlocal EnableExtensions

title Kristal Farms - Observatory

rem Always run from the repository root (the folder containing this file)
cd /d "%~dp0"

echo.
echo ==========================================
echo   Kristal Farms - Observatory v0.3.6
echo ==========================================
echo.

if not exist "apps\web\package.json" (
    echo ERROR: apps\web\package.json was not found.
    echo Put this file at the root of the Kristal Farms repository.
    echo.
    pause
    exit /b 1
)

where node >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or is not available in PATH.
    echo Install Node.js 20 or 22 LTS, then try again.
    echo.
    pause
    exit /b 1
)

where npm >nul 2>&1
if errorlevel 1 (
    echo ERROR: npm is not installed or is not available in PATH.
    echo.
    pause
    exit /b 1
)

echo Node:
node --version
echo npm:
call npm --version
echo.

echo Publishing coastal hydro screening scope...
where py >nul 2>&1
if not errorlevel 1 (
    py pipelines\publish\build_kristal_hydro_scope.py
) else (
    where python >nul 2>&1
    if not errorlevel 1 python pipelines\publish\build_kristal_hydro_scope.py
)
echo.

pushd "apps\web"

if not exist "node_modules\maplibre-gl\package.json" (
    echo Frontend dependencies are missing or incomplete.
    echo Restoring the locked dependency set with npm ci...
    echo.
    call npm ci
    if errorlevel 1 (
        echo.
        echo ERROR: npm ci failed.
        popd
        pause
        exit /b 1
    )
    echo.
)

echo Starting Observatory...
echo URL: http://localhost:3000
echo.
echo Keep this window open while using the application.
echo Press Ctrl+C to stop the server.
echo.

rem Open the browser shortly after the dev server starts.
start "" powershell -NoProfile -WindowStyle Hidden -Command "Start-Sleep -Seconds 3; Start-Process 'http://localhost:3000'"

call npm run dev
set "EXITCODE=%ERRORLEVEL%"

popd

echo.
if not "%EXITCODE%"=="0" (
    echo Observatory stopped with exit code %EXITCODE%.
) else (
    echo Observatory stopped.
)
echo.
pause
exit /b %EXITCODE%
