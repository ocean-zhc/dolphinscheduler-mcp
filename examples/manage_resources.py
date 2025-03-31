#!/usr/bin/env python3
"""Example script to manage DolphinScheduler resources using the MCP client."""

import argparse
import asyncio
import json
import os
import sys
from typing import Dict, Any

# For local development, add the parent directory to the Python path
sys.path.append(".")

# Import the MCPClient from simple_client.py
from examples.simple_client import MCPClient


async def list_resources(client: MCPClient, args: argparse.Namespace) -> None:
    """List resources in DolphinScheduler."""
    parameters: Dict[str, Any] = {}
    
    if args.pid is not None:
        parameters["pid"] = args.pid
    
    if args.resource_type is not None:
        parameters["resource_type"] = args.resource_type
        
    if args.search_val is not None:
        parameters["search_val"] = args.search_val
    
    response = await client.invoke_tool("get-resource-list", parameters)
    
    if "result" in response and "data" in response["result"]:
        resources = response["result"]["data"]
        print(f"Found {len(resources)} resources:")
        for resource in resources:
            print(f"- {resource.get('name', 'Unknown')} (ID: {resource.get('id', 'Unknown')})")
            print(f"  Type: {resource.get('type', 'Unknown')}")
            if "description" in resource and resource["description"]:
                print(f"  Description: {resource['description']}")
            print()
    else:
        print("Error or no resources found:")
        print(json.dumps(response, indent=2))


async def upload_resource(client: MCPClient, args: argparse.Namespace) -> None:
    """Upload a resource to DolphinScheduler."""
    with open(args.file_path, "rb") as file:
        file_content = file.read()
    
    parameters = {
        "pid": args.pid,
        "name": os.path.basename(args.file_path),
        "description": args.description or "",
        "content": file_content.decode("utf-8") if args.is_text else "",
        "is_text": args.is_text,
    }
    
    response = await client.invoke_tool("create-resource", parameters)
    print(json.dumps(response, indent=2))


async def delete_resource(client: MCPClient, args: argparse.Namespace) -> None:
    """Delete a resource from DolphinScheduler."""
    parameters = {
        "resource_id": args.resource_id
    }
    
    response = await client.invoke_tool("delete-resource", parameters)
    print(json.dumps(response, indent=2))


async def main():
    """Manage DolphinScheduler resources using MCP."""
    parser = argparse.ArgumentParser(description="Manage DolphinScheduler resources")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # List resources command
    list_parser = subparsers.add_parser("list", help="List resources")
    list_parser.add_argument("--pid", type=int, help="Parent directory ID (0 for root)")
    list_parser.add_argument("--resource-type", type=str, choices=["FILE", "UDF"], help="Resource type")
    list_parser.add_argument("--search-val", type=str, help="Search value")
    
    # Upload resource command
    upload_parser = subparsers.add_parser("upload", help="Upload a resource")
    upload_parser.add_argument("--pid", type=int, required=True, help="Parent directory ID")
    upload_parser.add_argument("--file-path", type=str, required=True, help="Path to the file to upload")
    upload_parser.add_argument("--description", type=str, help="Resource description")
    upload_parser.add_argument("--is-text", action="store_true", help="Whether the file is a text file")
    
    # Delete resource command
    delete_parser = subparsers.add_parser("delete", help="Delete a resource")
    delete_parser.add_argument("--resource-id", type=int, required=True, help="Resource ID to delete")
    
    args = parser.parse_args()
    
    # Set up the MCP server URL
    mcp_url = os.environ.get("MCP_URL", "http://localhost:8089/mcp")
    
    print(f"Connecting to MCP server at {mcp_url}")
    
    async with MCPClient(mcp_url) as client:
        if args.command == "list":
            await list_resources(client, args)
        elif args.command == "upload":
            await upload_resource(client, args)
        elif args.command == "delete":
            await delete_resource(client, args)
        else:
            parser.print_help()


if __name__ == "__main__":
    asyncio.run(main()) 