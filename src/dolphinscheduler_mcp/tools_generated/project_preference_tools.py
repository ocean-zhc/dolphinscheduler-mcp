"""Tools for project preference operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class GetProjectsProjectPreference(FastMCPTool):
    """Tool to query project preference"""

    name = "get_projects_project_preference"
    description = "query project preference"
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
        """Execute the GET operation on /projects/{projectCode}/project-preference."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/{project_code}/project-preference"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class UpdateProjectsProjectPreference(FastMCPTool):
    """Tool to update project preference"""

    name = "update_projects_project_preference"
    description = "update project preference"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "project_preferences": {
                        "type": "string",
                        "description": "project preferences"
                }
        },
        "required": [
                "project_code",
                "project_preferences"
        ]
}

    async def _run(self, project_code, project_preferences) -> Dict:
        """Execute the PUT operation on /projects/{projectCode}/project-preference."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "projectPreferences": project_preferences,
            }
            response = await client.request(
                "PUT", 
                f"/projects/{project_code}/project-preference", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateProjectsProjectPreference(FastMCPTool):
    """Tool to update the state of the project preference"""

    name = "create_projects_project_preference"
    description = "update the state of the project preference"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "state": {
                        "type": "string",
                        "description": "the state of the project preference"
                }
        },
        "required": [
                "project_code",
                "state"
        ]
}

    async def _run(self, project_code, state) -> Dict:
        """Execute the POST operation on /projects/{projectCode}/project-preference."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "state": state,
            }
            response = await client.request(
                "POST", 
                f"/projects/{project_code}/project-preference", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register_project_preference_tools(mcp):
    """Register project preference tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, CreateProjectsProjectPreference)
    register_tool_class(mcp, GetProjectsProjectPreference)
    register_tool_class(mcp, UpdateProjectsProjectPreference)
