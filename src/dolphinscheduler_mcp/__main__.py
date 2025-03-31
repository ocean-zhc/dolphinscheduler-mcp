"""Main entry point for DolphinScheduler MCP."""

import sys
import os
import importlib
from typing import List

# Clear cache for fastmcp_compat module to ensure changes are loaded
if "dolphinscheduler_mcp.fastmcp_compat" in sys.modules:
    del sys.modules["dolphinscheduler_mcp.fastmcp_compat"]

from .server import run_server


def main(args: List[str] = None) -> int:
    """Run the MCP server with the given arguments."""
    if args is None:
        args = sys.argv[1:]
    
    # Default configuration
    host = "0.0.0.0"
    port = 8089
    
    # Check for environment variables first
    if "DOLPHINSCHEDULER_MCP_HOST" in os.environ:
        host = os.environ["DOLPHINSCHEDULER_MCP_HOST"]
    if "DOLPHINSCHEDULER_MCP_PORT" in os.environ:
        try:
            port = int(os.environ["DOLPHINSCHEDULER_MCP_PORT"])
        except ValueError:
            print(f"Invalid port number in DOLPHINSCHEDULER_MCP_PORT: {os.environ['DOLPHINSCHEDULER_MCP_PORT']}")
            return 1
    
    # Override with command line arguments if provided
    if len(args) >= 1:
        host = args[0]
    if len(args) >= 2:
        try:
            port = int(args[1])
        except ValueError:
            print(f"Invalid port number: {args[1]}")
            return 1
    
    # Check if API URL and key are set
    if "DOLPHINSCHEDULER_API_URL" not in os.environ:
        print("Warning: DOLPHINSCHEDULER_API_URL environment variable is not set.")
        print("Using default: http://localhost:12345/dolphinscheduler")
    
    if "DOLPHINSCHEDULER_API_KEY" not in os.environ:
        print("Warning: DOLPHINSCHEDULER_API_KEY environment variable is not set.")
        print("Authentication to the DolphinScheduler API may fail.")
    
    # Run the server
    try:
        run_server(host=host, port=port)
        return 0
    except Exception as e:
        print(f"Error running server: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 