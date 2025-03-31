"""Tools for DYNAMIC_TASK_TYPE operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class ListDynamicTasktypes(FastMCPTool):
    """Tool to list_dynamic_task_types"""

    name = "list_dynamic_tasktypes"
    description = "LIST_DYNAMIC_TASK_TYPES"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "task_category": {
                        "type": "string"
                }
        },
        "required": [
                "task_category"
        ]
}

    async def _run(self, task_category) -> Dict:
        """Execute the GET operation on /dynamic/{taskCategory}/taskTypes."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/dynamic/{task_category}/taskTypes"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListDynamicTaskcategories(FastMCPTool):
    """Tool to list_task_type_categories"""

    name = "list_dynamic_taskcategories"
    description = "LIST_TASK_TYPE_CATEGORIES"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /dynamic/taskCategories."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/dynamic/taskCategories"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register_DYNAMIC_TASK_TYPE_tools(mcp):
    """Register DYNAMIC_TASK_TYPE tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, ListDynamicTaskcategories)
    register_tool_class(mcp, ListDynamicTasktypes)
