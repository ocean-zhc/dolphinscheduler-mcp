#!/usr/bin/env python3
"""Example script to execute a DolphinScheduler process definition using the MCP client."""

import argparse
import asyncio
import json
import os
import sys

# For local development, add the parent directory to the Python path
sys.path.append(".")

# Import the MCPClient from simple_client.py
from examples.simple_client import MCPClient


async def main():
    """Execute a DolphinScheduler process definition using MCP."""
    parser = argparse.ArgumentParser(description="Execute a DolphinScheduler process definition")
    parser.add_argument("--project-code", type=int, required=True, help="Project code")
    parser.add_argument("--process-definition-code", type=int, required=True, help="Process definition code")
    parser.add_argument("--schedule-time", type=str, help="Schedule time (yyyy-MM-dd HH:mm:ss)")
    parser.add_argument("--execution-type", type=str, default="PARALLEL", 
                       help="Execution type (PARALLEL/SERIAL_WAIT/SERIAL_DISCARD/SERIAL_PRIORITY)")
    args = parser.parse_args()

    # Set up the MCP server URL
    mcp_url = os.environ.get("MCP_URL", "http://localhost:8089/mcp")
    
    print(f"Connecting to MCP server at {mcp_url}")
    
    async with MCPClient(mcp_url) as client:
        # Execute process definition
        print(f"Executing process definition {args.process_definition_code} in project {args.project_code}:")
        
        # Prepare parameters
        parameters = {
            "project_code": args.project_code,
            "process_definition_code": args.process_definition_code,
            "execution_type": args.execution_type,
        }
        
        if args.schedule_time:
            parameters["schedule_time"] = args.schedule_time
        
        # Execute the process definition
        response = await client.invoke_tool("execute-process-definition", parameters)
        
        # Pretty print the result
        print(json.dumps(response, indent=2))


if __name__ == "__main__":
    asyncio.run(main()) 