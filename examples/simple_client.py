#!/usr/bin/env python
"""
A simple example client for the DolphinScheduler MCP server.
This example demonstrates how to use the MCP client to interact with DolphinScheduler.
"""

import asyncio
import json
import os
from typing import Any, Dict, Optional

import aiohttp


class MCPClient:
    """A simple MCP client for DolphinScheduler."""

    def __init__(self, url: str):
        """Initialize the MCP client.

        Args:
            url: The URL of the MCP server.
        """
        self.url = url
        self.session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        """Enter the async context manager."""
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the async context manager."""
        if self.session:
            await self.session.close()
            self.session = None

    async def invoke_tool(self, tool_name: str, arguments: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Invoke a tool on the MCP server.

        Args:
            tool_name: The name of the tool to invoke.
            arguments: Optional arguments for the tool.

        Returns:
            The response from the tool.
        """
        if self.session is None:
            self.session = aiohttp.ClientSession()

        payload = {
            "toolName": tool_name,
        }
        if arguments:
            payload["arguments"] = arguments

        async with self.session.post(self.url, json=payload) as response:
            return await response.json()


async def main():
    """Run the example client."""
    # Set up the MCP server URL
    mcp_url = os.environ.get("MCP_URL", "http://localhost:8089/mcp")
    
    print(f"Connecting to MCP server at {mcp_url}")
    
    async with MCPClient(mcp_url) as client:
        # Get connection settings
        print("\n1. Getting connection settings:")
        response = await client.invoke_tool("get-connection-settings")
        print(json.dumps(response, indent=2))

        # Get project list
        print("\n2. Getting project list:")
        response = await client.invoke_tool("get-project-list")
        print(json.dumps(response, indent=2))

        # Create a new project
        print("\n3. Creating a new project:")
        response = await client.invoke_tool(
            "create-project", 
            {"name": "MCP Demo Project", "description": "Project created by MCP demo"}
        )
        print(json.dumps(response, indent=2))
        
        # If the project was created successfully, get its code
        if response.get("result", {}).get("success", False):
            project_code = response.get("result", {}).get("code")
            
            # Get project details
            print(f"\n4. Getting details for project {project_code}:")
            response = await client.invoke_tool("get-project", {"project_code": project_code})
            print(json.dumps(response, indent=2))
            
            # Create a process definition
            print(f"\n5. Creating a process definition in project {project_code}:")
            process_def = {
                "project_code": project_code,
                "name": "MCP Demo Process",
                "description": "Process created by MCP demo",
                "task_definitions": [],
                "execution_type": "PARALLEL"
            }
            response = await client.invoke_tool("create-process-definition", process_def)
            print(json.dumps(response, indent=2))
            
            # Delete the project
            print(f"\n6. Deleting project {project_code}:")
            response = await client.invoke_tool("delete-project", {"project_code": project_code})
            print(json.dumps(response, indent=2))


if __name__ == "__main__":
    asyncio.run(main()) 