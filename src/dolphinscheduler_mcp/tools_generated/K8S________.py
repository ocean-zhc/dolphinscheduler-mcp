"""Tools for K8S________ operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class GetK8sNamespace(FastMCPTool):
    """Tool to 查询命名空间列表页面"""

    name = "get_k8s_namespace"
    description = "查询命名空间列表页面"
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
        """Execute the GET operation on /k8s-namespace."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "searchVal": searchVal,
                "pageSize": pageSize,
                "pageNo": pageNo,
            }
            response = await client.request(
                "GET", 
                f"/k8s-namespace", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateK8sNamespace(FastMCPTool):
    """Tool to 创建命名空间"""

    name = "create_k8s_namespace"
    description = "创建命名空间"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "namespace": {
                        "type": "string",
                        "description": "\u547d\u540d\u7a7a\u95f4"
                },
                "clusterCode": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u96c6\u7fa4\u4ee3\u7801"
                }
        },
        "required": [
                "namespace",
                "clusterCode"
        ]
}

    async def _run(self, namespace, clusterCode) -> Dict:
        """Execute the POST operation on /k8s-namespace."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "namespace": namespace,
                "clusterCode": clusterCode,
            }
            response = await client.request(
                "POST", 
                f"/k8s-namespace", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateK8sNamespaceVerify(FastMCPTool):
    """Tool to 校验命名空间"""

    name = "create_k8s_namespace_verify"
    description = "校验命名空间"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "namespace": {
                        "type": "string",
                        "description": "\u547d\u540d\u7a7a\u95f4"
                },
                "clusterCode": {
                        "type": "integer",
                        "format": "int64",
                        "description": "\u96c6\u7fa4\u4ee3\u7801"
                }
        },
        "required": [
                "namespace",
                "clusterCode"
        ]
}

    async def _run(self, namespace, clusterCode) -> Dict:
        """Execute the POST operation on /k8s-namespace/verify."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "namespace": namespace,
                "clusterCode": clusterCode,
            }
            response = await client.request(
                "POST", 
                f"/k8s-namespace/verify", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateK8sNamespaceDelete(FastMCPTool):
    """Tool to 通过id删除命名空间"""

    name = "create_k8s_namespace_delete"
    description = "通过ID删除命名空间"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "k8s\u547d\u540d\u7a7a\u95f4ID"
                }
        },
        "required": [
                "id"
        ]
}

    async def _run(self, id) -> Dict:
        """Execute the POST operation on /k8s-namespace/delete."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "id": id,
            }
            response = await client.request(
                "POST", 
                f"/k8s-namespace/delete", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetK8sNamespaceUnauthNamespace(FastMCPTool):
    """Tool to 查询未授权命名空间"""

    name = "get_k8s_namespace_unauth_namespace"
    description = "查询未授权命名空间"
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
        """Execute the GET operation on /k8s-namespace/unauth-namespace."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": userId,
            }
            response = await client.request(
                "GET", 
                f"/k8s-namespace/unauth-namespace", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetK8sNamespaceAvailableNamespaceList(FastMCPTool):
    """Tool to 获取可用命名空间列表"""

    name = "get_k8s_namespace_available_namespace_list"
    description = "获取可用命名空间列表"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /k8s-namespace/available-namespace-list."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/k8s-namespace/available-namespace-list"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetK8sNamespaceAuthorizedNamespace(FastMCPTool):
    """Tool to 获取命名空间列表"""

    name = "get_k8s_namespace_authorized_namespace"
    description = "获取命名空间列表"
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
        """Execute the GET operation on /k8s-namespace/authorized-namespace."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": userId,
            }
            response = await client.request(
                "GET", 
                f"/k8s-namespace/authorized-namespace", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register_K8S_________tools(mcp):
    """Register K8S________ tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, CreateK8sNamespace)
    register_tool_class(mcp, CreateK8sNamespaceDelete)
    register_tool_class(mcp, CreateK8sNamespaceVerify)
    register_tool_class(mcp, GetK8sNamespace)
    register_tool_class(mcp, GetK8sNamespaceAuthorizedNamespace)
    register_tool_class(mcp, GetK8sNamespaceAvailableNamespaceList)
    register_tool_class(mcp, GetK8sNamespaceUnauthNamespace)
