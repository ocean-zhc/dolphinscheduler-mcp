#!/usr/bin/env python
"""
DolphinScheduler MCP Server Runner

This script sets up environment variables and runs the DolphinScheduler MCP server.
"""

import os
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("dolphinscheduler_mcp.runner")

def main():
    """Main entry point for running DolphinScheduler MCP server."""
    # Default host and port
    host = os.environ.get("DOLPHINSCHEDULER_MCP_HOST", "0.0.0.0")
    port = int(os.environ.get("DOLPHINSCHEDULER_MCP_PORT", "8089"))
    
    # Check if API URL is set
    api_url = os.environ.get("DOLPHINSCHEDULER_API_URL")
    if not api_url:
        logger.warning("DOLPHINSCHEDULER_API_URL environment variable is not set!")
        logger.warning("Using default URL from Config class.")
    
    # Check if API key is set - this is required for all API requests
    api_key = os.environ.get("DOLPHINSCHEDULER_API_KEY")
    if not api_key:
        logger.warning("DOLPHINSCHEDULER_API_KEY environment variable is not set!")
        logger.warning("API requests may fail due to missing authentication.")
    else:
        logger.info("Using API key from environment variables.")
    
    # Print configuration
    logger.info(f"Starting DolphinScheduler MCP Server on {host}:{port}")
    if api_url:
        logger.info(f"Using DolphinScheduler API URL: {api_url}")
    
    # Import and run the server
    try:
        from src.dolphinscheduler_mcp.server import run_server
        run_server(host=host, port=port)
        return 0
    except ImportError:
        logger.error("Could not import dolphinscheduler_mcp. Make sure it's installed.")
        return 1
    except Exception as e:
        logger.error(f"Error running server: {e}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main()) 