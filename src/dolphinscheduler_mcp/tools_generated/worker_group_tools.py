"""Tools for worker group operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class GetWorkerGroups(FastMCPTool):
    """Tool to worker分组管理"""

    name = "get_worker_groups"
    description = "Worker分组管理"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "page_no": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u7801\u53f7"
                },
                "page_size": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u5927\u5c0f"
                },
                "search_val": {
                        "type": "string",
                        "description": "\u641c\u7d22\u503c"
                }
        },
        "required": [
                "page_no",
                "page_size"
        ]
}

    async def _run(self, page_no, page_size, search_val) -> Dict:
        """Execute the GET operation on /worker-groups."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "pageNo": page_no,
                "pageSize": page_size,
                "searchVal": search_val,
            }
            response = await client.request(
                "GET", 
                f"/worker-groups", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateWorkerGroups(FastMCPTool):
    """Tool to 创建worker分组"""

    name = "create_worker_groups"
    description = "创建Worker分组"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "Worker Server\u5206\u7ec4ID"
                },
                "name": {
                        "type": "string",
                        "description": "Worker\u5206\u7ec4\u540d\u79f0"
                },
                "addr_list": {
                        "type": "string",
                        "description": "worker\u5730\u5740\u5217\u8868"
                },
                "description": {
                        "type": "string",
                        "description": "WORKER_DESC"
                },
                "other_params_json": {
                        "type": "string",
                        "description": "WORKER_PARAMS_JSON"
                }
        },
        "required": [
                "name",
                "addr_list"
        ]
}

    async def _run(self, id, name, addr_list, description, other_params_json) -> Dict:
        """Execute the POST operation on /worker-groups."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "id": id,
                "name": name,
                "addrList": addr_list,
                "description": description,
                "otherParamsJson": other_params_json,
            }
            response = await client.request(
                "POST", 
                f"/worker-groups", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetWorkerGroupsWorkerAddressList(FastMCPTool):
    """Tool to 查询worker地址列表"""

    name = "get_worker_groups_worker_address_list"
    description = "查询worker地址列表"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /worker-groups/worker-address-list."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/worker-groups/worker-address-list"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetWorkerGroupsAll(FastMCPTool):
    """Tool to 查询worker group分组"""

    name = "get_worker_groups_all"
    description = "查询worker group分组"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /worker-groups/all."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/worker-groups/all"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class DeleteWorkerGroups(FastMCPTool):
    """Tool to 通过id删除worker group"""

    name = "delete_worker_groups"
    description = "通过ID删除worker group"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "Worker Server\u5206\u7ec4ID"
                }
        },
        "required": [
                "id"
        ]
}

    async def _run(self, id) -> Dict:
        """Execute the DELETE operation on /worker-groups/{id}.
        
        Args:
            id: Worker分组ID
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 确保路径参数正确处理
            worker_group_id = int(id) if id is not None else None
            if worker_group_id is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: id"
                }
                
            response = await client.request(
                "DELETE", 
                f"/worker-groups/{worker_group_id}"
            )
            return {"success": True, "data": response}
        except ValueError:
            return {
                "success": False,
                "error": f"Invalid ID format: {id}"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            await client.close()


def register_worker_group_tools(mcp):
    """Register worker group tool with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, CreateWorkerGroups)
    register_tool_class(mcp, DeleteWorkerGroups)
    register_tool_class(mcp, GetWorkerGroups)
    register_tool_class(mcp, GetWorkerGroupsAll)
    register_tool_class(mcp, GetWorkerGroupsWorkerAddressList)
