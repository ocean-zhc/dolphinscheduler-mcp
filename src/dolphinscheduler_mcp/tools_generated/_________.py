"""Tools for _________ operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class CreateProjectsLineagesTasksVerifyDelete(FastMCPTool):
    """Tool to 校验是否可以删除任务"""

    name = "create_projects_lineages_tasks_verify_delete"
    description = "校验是否可以删除任务"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "process_definition_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u6d41\u7a0b\u5b9a\u4e49\u7f16\u7801"
                },
                "task_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u4efb\u52a1\u5b9a\u4e49\u4ee3\u7801"
                }
        },
        "required": [
                "project_code",
                "process_definition_code",
                "task_code"
        ]
}

    async def _run(self, project_code, process_definition_code, task_code) -> Dict:
        """Execute the POST operation on /projects/{projectCode}/lineages/tasks/verify-delete."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "processDefinitionCode": process_definition_code,
                "taskCode": task_code,
            }
            response = await client.request(
                "POST", 
                f"/projects/{project_code}/lineages/tasks/verify-delete", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListProjectsLineages(FastMCPTool):
    """Tool to 通过血缘代码查询工作流血缘关系"""

    name = "list_projects_lineages"
    description = "通过血缘代码查询工作流血缘关系"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "work_flow_code": {
                        "type": "integer",
                        "format": "int64"
                }
        },
        "required": [
                "project_code",
                "work_flow_code"
        ]
}

    async def _run(self, project_code, work_flow_code) -> Dict:
        """Execute the GET operation on /projects/{projectCode}/lineages/{workFlowCode}."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/{project_code}/lineages/{work_flow_code}"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListProjectsLineagesQueryDependentTasks(FastMCPTool):
    """Tool to query_downstream_dependent_task_notes"""

    name = "list_projects_lineages_query_dependent_tasks"
    description = "QUERY_DOWNSTREAM_DEPENDENT_TASK_NOTES"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "work_flow_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u6d41\u7a0b\u5b9a\u4e49\u7f16\u7801"
                },
                "task_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u4efb\u52a1\u5b9a\u4e49\u4ee3\u7801"
                }
        },
        "required": [
                "work_flow_code"
        ]
}

    async def _run(self, work_flow_code, task_code) -> Dict:
        """Execute the GET operation on /projects/{projectCode}/lineages/query-dependent-tasks."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "workFlowCode": work_flow_code,
                "taskCode": task_code,
            }
            response = await client.request(
                "GET", 
                f"/projects/{project_code}/lineages/query-dependent-tasks", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsLineagesQueryByName(FastMCPTool):
    """Tool to 通过名称查询工作流血缘列表"""

    name = "get_projects_lineages_query_by_name"
    description = "通过名称查询工作流血缘列表"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "work_flow_name": {
                        "type": "string"
                }
        },
        "required": [
                "project_code"
        ]
}

    async def _run(self, project_code, work_flow_name) -> Dict:
        """Execute the GET operation on /projects/{projectCode}/lineages/query-by-name."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "workFlowName": work_flow_name,
            }
            response = await client.request(
                "GET", 
                f"/projects/{project_code}/lineages/query-by-name", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListProjectsLineagesList(FastMCPTool):
    """Tool to 查询工作量血缘关系"""

    name = "list_projects_lineages_list"
    description = "查询工作量血缘关系"
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
        """Execute the GET operation on /projects/{projectCode}/lineages/list."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/{project_code}/lineages/list"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register___________tools(mcp):
    """Register _________ tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, CreateProjectsLineagesTasksVerifyDelete)
    register_tool_class(mcp, GetProjectsLineagesQueryByName)
    register_tool_class(mcp, ListProjectsLineages)
    register_tool_class(mcp, ListProjectsLineagesList)
    register_tool_class(mcp, ListProjectsLineagesQueryDependentTasks)
