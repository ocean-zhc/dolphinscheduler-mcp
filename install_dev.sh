#!/bin/bash
# Install the package in development mode

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
fi

# Install the package in development mode
echo "Installing package in development mode..."
pip install -e .

echo "Installation complete!" 