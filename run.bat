@echo off
SETLOCAL

:: Check for Python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python could not be found. Please install Python 3.
    exit /b 1
)

:: Create virtual environment if it doesn't exist
IF NOT EXIST .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

:: Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

:: Install requirements
echo Installing requirements...
pip install -e .

:: Run the server
echo Starting DolphinScheduler MCP Server...
python -m src.dolphinscheduler_mcp

ENDLOCAL 