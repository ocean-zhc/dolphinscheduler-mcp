#!/usr/bin/env python3
"""Example script to list DolphinScheduler projects using the MCP client."""

import asyncio
import json
import os
import sys

# For local development, add the parent directory to the Python path
sys.path.append(".")

# Import the MCPClient from simple_client.py
from examples.simple_client import MCPClient


async def main():
    """List all DolphinScheduler projects using MCP."""
    # Set up the MCP server URL
    mcp_url = os.environ.get("MCP_URL", "http://localhost:8089/mcp")
    
    print(f"Connecting to MCP server at {mcp_url}")
    
    async with MCPClient(mcp_url) as client:
        # Get project list
        print("Getting project list:")
        response = await client.invoke_tool("get-project-list")
        
        # Pretty print the result
        if "result" in response and "data" in response["result"]:
            projects = response["result"]["data"]
            print(f"Found {len(projects)} projects:")
            for project in projects:
                print(f"- {project['name']} (Code: {project['code']})")
        else:
            print("Error or no projects found:")
            print(json.dumps(response, indent=2))


if __name__ == "__main__":
    asyncio.run(main()) 