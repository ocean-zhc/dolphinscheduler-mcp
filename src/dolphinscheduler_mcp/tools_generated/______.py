"""Tools for ______ operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class GetProjects(FastMCPTool):
    """Tool to 通过项目id查询项目信息"""

    name = "get_projects"
    description = "通过项目ID查询项目信息"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                }
        },
        "required": [
                "code"
        ]
}

    async def _run(self, code) -> Dict:
        """Execute the GET operation on /projects/{code}."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/{code}"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class UpdateProjects(FastMCPTool):
    """Tool to 更新项目"""

    name = "update_projects"
    description = "更新项目"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                },
                "projectName": {
                        "type": "string",
                        "description": "\u9879\u76ee\u540d\u79f0"
                },
                "description": {
                        "type": "string",
                        "description": "\u9879\u76ee\u63cf\u8ff0"
                }
        },
        "required": [
                "code",
                "projectName"
        ]
}

    async def _run(self, code, projectName, description) -> Dict:
        """Execute the PUT operation on /projects/{code}."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "projectName": projectName,
                "description": description,
            }
            response = await client.request(
                "PUT", 
                f"/projects/{code}", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class DeleteProjects(FastMCPTool):
    """Tool to 通过id删除项目"""

    name = "delete_projects"
    description = "通过ID删除项目"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "code": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u9879\u76eeCode"
                }
        },
        "required": [
                "code"
        ]
}

    async def _run(self, code) -> Dict:
        """Execute the DELETE operation on /projects/{code}."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "DELETE", 
                f"/projects/{code}"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjects36(FastMCPTool):
    """Tool to 分页查询项目列表"""

    name = "get_projects36"
    description = "分页查询项目列表"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "searchVal": {
                        "type": "string",
                        "description": "\u641c\u7d22\u503c"
                },
                "pageSize": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u5927\u5c0f"
                },
                "pageNo": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u7801\u53f7"
                }
        },
        "required": [
                "pageSize",
                "pageNo"
        ]
}

    async def _run(self, searchVal, pageSize, pageNo) -> Dict:
        """Execute the GET operation on /projects."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "searchVal": searchVal,
                "pageSize": pageSize,
                "pageNo": pageNo,
            }
            response = await client.request(
                "GET", 
                f"/projects", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateProjects(FastMCPTool):
    """Tool to 创建项目"""

    name = "create_projects"
    description = "创建项目"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "projectName": {
                        "type": "string",
                        "description": "\u9879\u76ee\u540d\u79f0"
                },
                "description": {
                        "type": "string",
                        "description": "\u9879\u76ee\u63cf\u8ff0"
                }
        },
        "required": [
                "projectName"
        ]
}

    async def _run(self, projectName, description) -> Dict:
        """Execute the POST operation on /projects."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "projectName": projectName,
                "description": description,
            }
            response = await client.request(
                "POST", 
                f"/projects", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsUnauthProject(FastMCPTool):
    """Tool to 查询未授权的项目"""

    name = "get_projects_unauth_project"
    description = "查询未授权的项目"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "userId": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u7528\u6237ID"
                }
        },
        "required": [
                "userId"
        ]
}

    async def _run(self, userId) -> Dict:
        """Execute the GET operation on /projects/unauth-project."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": userId,
            }
            response = await client.request(
                "GET", 
                f"/projects/unauth-project", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsProjectWithAuthorizedLevel(FastMCPTool):
    """Tool to query_project_authorized_level"""

    name = "get_projects_project_with_authorized_level"
    description = "QUERY_PROJECT_AUTHORIZED_LEVEL"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "user_id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u7528\u6237ID"
                }
        },
        "required": [
                "user_id"
        ]
}

    async def _run(self, user_id) -> Dict:
        """Execute the GET operation on /projects/project-with-authorized-level."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": user_id,
            }
            response = await client.request(
                "GET", 
                f"/projects/project-with-authorized-level", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsProjectWithAuthorizedLevelListPaging(FastMCPTool):
    """Tool to query_project_with_auth_level_list_paging_notes"""

    name = "get_projects_project_with_authorized_level_list_paging"
    description = "QUERY_PROJECT_WITH_AUTH_LEVEL_LIST_PAGING_NOTES"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "user_id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u7528\u6237ID"
                },
                "search_val": {
                        "type": "string",
                        "description": "\u641c\u7d22\u503c"
                },
                "page_size": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u5927\u5c0f"
                },
                "page_no": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u7801\u53f7"
                }
        },
        "required": [
                "user_id",
                "page_size",
                "page_no"
        ]
}

    async def _run(self, user_id, search_val, page_size, page_no) -> Dict:
        """Execute the GET operation on /projects/project-with-authorized-level-list-paging."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": user_id,
                "searchVal": search_val,
                "pageSize": page_size,
                "pageNo": page_no,
            }
            response = await client.request(
                "GET", 
                f"/projects/project-with-authorized-level-list-paging", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListProjectsList(FastMCPTool):
    """Tool to 查询所有项目"""

    name = "list_projects_list"
    description = "查询所有项目"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /projects/list."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/list"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsListDependent(FastMCPTool):
    """Tool to 查询dependent节点所有项目"""

    name = "get_projects_list_dependent"
    description = "查询Dependent节点所有项目"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /projects/list-dependent."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/list-dependent"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsCreatedAndAuthed(FastMCPTool):
    """Tool to 查询授权和用户创建的项目"""

    name = "get_projects_created_and_authed"
    description = "查询授权和用户创建的项目"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /projects/created-and-authed."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/created-and-authed"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsAuthedUser(FastMCPTool):
    """Tool to 查询拥有项目授权的用户"""

    name = "get_projects_authed_user"
    description = "查询拥有项目授权的用户"
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
        """Execute the GET operation on /projects/authed-user."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "projectCode": project_code,
            }
            response = await client.request(
                "GET", 
                f"/projects/authed-user", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsAuthedProject(FastMCPTool):
    """Tool to 查询授权项目"""

    name = "get_projects_authed_project"
    description = "查询授权项目"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "user_id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u7528\u6237ID"
                }
        },
        "required": [
                "user_id"
        ]
}

    async def _run(self, user_id) -> Dict:
        """Execute the GET operation on /projects/authed-project."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": user_id,
            }
            response = await client.request(
                "GET", 
                f"/projects/authed-project", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register________tools(mcp):
    """Register ______ tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, CreateProjects)
    register_tool_class(mcp, DeleteProjects)
    register_tool_class(mcp, GetProjects)
    register_tool_class(mcp, GetProjects36)
    register_tool_class(mcp, GetProjectsAuthedProject)
    register_tool_class(mcp, GetProjectsAuthedUser)
    register_tool_class(mcp, GetProjectsCreatedAndAuthed)
    register_tool_class(mcp, GetProjectsListDependent)
    register_tool_class(mcp, GetProjectsProjectWithAuthorizedLevel)
    register_tool_class(mcp, GetProjectsProjectWithAuthorizedLevelListPaging)
    register_tool_class(mcp, GetProjectsUnauthProject)
    register_tool_class(mcp, ListProjectsList)
    register_tool_class(mcp, UpdateProjects)
