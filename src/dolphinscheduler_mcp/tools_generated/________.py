"""Tools for ________ operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class GetProjectsProjectParameter(FastMCPTool):
    """Tool to 查询项目参数"""

    name = "get_projects_project_parameter"
    description = "查询项目参数"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76ee\u53c2\u6570code"
                }
        },
        "required": [
                "project_code",
                "code"
        ]
}

    async def _run(self, project_code, code) -> Dict:
        """Execute the GET operation on /projects/{projectCode}/project-parameter/{code}."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/{project_code}/project-parameter/{code}"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class UpdateProjectsProjectParameter(FastMCPTool):
    """Tool to 更新项目参数"""

    name = "update_projects_project_parameter"
    description = "更新项目参数"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76ee\u53c2\u6570code"
                },
                "project_parameter_name": {
                        "type": "string",
                        "description": "\u9879\u76ee\u53c2\u6570\u540d\u79f0"
                },
                "project_parameter_value": {
                        "type": "string",
                        "description": "\u9879\u76ee\u53c2\u6570\u503c"
                }
        },
        "required": [
                "project_code",
                "code",
                "project_parameter_name",
                "project_parameter_value"
        ]
}

    async def _run(self, project_code, code, project_parameter_name, project_parameter_value) -> Dict:
        """Execute the PUT operation on /projects/{projectCode}/project-parameter/{code}."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "projectParameterName": project_parameter_name,
                "projectParameterValue": project_parameter_value,
            }
            response = await client.request(
                "PUT", 
                f"/projects/{project_code}/project-parameter/{code}", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsProjectParameter2(FastMCPTool):
    """Tool to 分页查询项目参数"""

    name = "get_projects_project_parameter2"
    description = "分页查询项目参数"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "search_val": {
                        "type": "string",
                        "description": "\u641c\u7d22\u503c"
                },
                "page_no": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u7801\u53f7"
                },
                "page_size": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u5927\u5c0f"
                }
        },
        "required": [
                "project_code",
                "page_no",
                "page_size"
        ]
}

    async def _run(self, project_code, search_val, page_no, page_size) -> Dict:
        """Execute the GET operation on /projects/{projectCode}/project-parameter."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "searchVal": search_val,
                "pageNo": page_no,
                "pageSize": page_size,
            }
            response = await client.request(
                "GET", 
                f"/projects/{project_code}/project-parameter", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateProjectsProjectParameter(FastMCPTool):
    """Tool to 新增项目参数"""

    name = "create_projects_project_parameter"
    description = "新增项目参数"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "project_parameter_name": {
                        "type": "string",
                        "description": "\u9879\u76ee\u53c2\u6570\u540d\u79f0"
                },
                "project_parameter_value": {
                        "type": "string",
                        "description": "\u9879\u76ee\u53c2\u6570\u503c"
                }
        },
        "required": [
                "project_code",
                "project_parameter_name",
                "project_parameter_value"
        ]
}

    async def _run(self, project_code, project_parameter_name, project_parameter_value) -> Dict:
        """Execute the POST operation on /projects/{projectCode}/project-parameter."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "projectParameterName": project_parameter_name,
                "projectParameterValue": project_parameter_value,
            }
            response = await client.request(
                "POST", 
                f"/projects/{project_code}/project-parameter", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateProjectsProjectParameterDelete(FastMCPTool):
    """Tool to 删除项目参数"""

    name = "create_projects_project_parameter_delete"
    description = "删除项目参数"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "code": {
                        "type": "string",
                        "description": "\u9879\u76ee\u53c2\u6570code"
                }
        },
        "required": [
                "project_code",
                "code"
        ]
}

    async def _run(self, project_code, code) -> Dict:
        """Execute the POST operation on /projects/{projectCode}/project-parameter/delete."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "code": code,
            }
            response = await client.request(
                "POST", 
                f"/projects/{project_code}/project-parameter/delete", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateProjectsProjectParameterBatchDelete(FastMCPTool):
    """Tool to 删除项目参数"""

    name = "create_projects_project_parameter_batch_delete"
    description = "删除项目参数"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "project_code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "codes": {
                        "type": "string",
                        "description": "\u9879\u76ee\u53c2\u6570code"
                }
        },
        "required": [
                "project_code",
                "codes"
        ]
}

    async def _run(self, project_code, codes) -> Dict:
        """Execute the POST operation on /projects/{projectCode}/project-parameter/batch-delete."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "codes": codes,
            }
            response = await client.request(
                "POST", 
                f"/projects/{project_code}/project-parameter/batch-delete", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register__________tools(mcp):
    """Register ________ tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, CreateProjectsProjectParameter)
    register_tool_class(mcp, CreateProjectsProjectParameterBatchDelete)
    register_tool_class(mcp, CreateProjectsProjectParameterDelete)
    register_tool_class(mcp, GetProjectsProjectParameter)
    register_tool_class(mcp, GetProjectsProjectParameter2)
    register_tool_class(mcp, UpdateProjectsProjectParameter)
