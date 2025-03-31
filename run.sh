#!/bin/bash

# Check for Python
if ! command -v python3 &>/dev/null; then
    echo "Python 3 could not be found. Please install Python 3."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -e .

# Run the server
echo "Starting DolphinScheduler MCP Server..."
python -m src.dolphinscheduler_mcp 