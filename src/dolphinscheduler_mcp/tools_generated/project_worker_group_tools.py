"""Tools for project worker group operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class GetProjectsWorkerGroup(FastMCPTool):
    """Tool to query_worker_group_list"""

    name = "get_projects_worker_group"
    description = "QUERY_WORKER_GROUP_LIST"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                }
        },
        "required": [
                "project_code"
        ]
}

    async def _run(self, project_code) -> Dict:
        """Execute the GET operation on /projects/{projectCode}/worker-group."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/{project_code}/worker-group"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateProjectsWorkerGroup(FastMCPTool):
    """Tool to assign_worker_groups_notes"""

    name = "create_projects_worker_group"
    description = "ASSIGN_WORKER_GROUPS_NOTES"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "worker_groups": {
                        "type": "string",
                        "description": "Worker\u5de5\u4f5c\u7ec4\u5217\u8868"
                }
        },
        "required": [
                "project_code"
        ]
}

    async def _run(self, project_code, worker_groups) -> Dict:
        """Execute the POST operation on /projects/{projectCode}/worker-group."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "POST", 
                f"/projects/{project_code}/worker-group"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register_project_worker_group_tools(mcp):
    """Register project worker group tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, CreateProjectsWorkerGroup)
    register_tool_class(mcp, GetProjectsWorkerGroup)
