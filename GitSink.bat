@echo off
setlocal

REM Run from repository root even when launched from Explorer.
cd /d "%~dp0"

REM Ensure this is a Git worktree.
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo ERROR: This folder is not a Git repository.
    pause
    exit /b 1
)

REM Ensure a push remote exists.
for /f "delims=" %%R in ('git remote') do set "HAS_REMOTE=1"
if not defined HAS_REMOTE (
    echo ERROR: No Git remote is configured.
    echo Configure origin before using this helper.
    pause
    exit /b 1
)

echo.
echo =================================
echo Kristal Farms - Git Update

echo =================================
echo.

echo Running: git add -A
git add -A
if errorlevel 1 goto :fail

REM Commit only when staged changes exist.
git diff --cached --quiet
if errorlevel 1 (
    if "%~1"=="" (
        set /p "commit_message=Enter commit message: "
    ) else (
        set "commit_message=%~1"
    )

    if not defined commit_message (
        echo ERROR: Commit message cannot be empty.
        pause
        exit /b 1
    )

    echo Running: git commit -m "%commit_message%"
    git commit -m "%commit_message%"
    if errorlevel 1 goto :fail
) else (
    echo No local changes to commit.
)

echo Running: git push
git push
if errorlevel 1 goto :fail

echo.
echo Git update complete.
pause
exit /b 0

:fail
echo.
echo ERROR: Git command failed. Review the message above.
pause
exit /b 1
