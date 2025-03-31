"""Tools for __token____ operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class UpdateAccessTokens(FastMCPTool):
    """Tool to 更新指定用户的安全令牌"""

    name = "update_access_tokens"
    description = "更新指定用户的安全令牌"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u5b89\u5168\u4ee4\u724c\u7684ID"
                },
                "user_id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u7528\u6237ID"
                },
                "expire_time": {
                        "type": "string",
                        "description": "\u5b89\u5168\u4ee4\u724c\u7684\u8fc7\u671f\u65f6\u95f4"
                },
                "token": {
                        "type": "string",
                        "description": "\u5b89\u5168\u4ee4\u724c\u5b57\u7b26\u4e32\uff0c\u82e5\u672a\u663e\u5f0f\u6307\u5b9a\u5c06\u4f1a\u81ea\u52a8\u751f\u6210"
                }
        },
        "required": [
                "id",
                "user_id",
                "expire_time"
        ]
}

    async def _run(self, id, user_id, expire_time, token) -> Dict:
        """Execute the PUT operation on /access-tokens/{id}."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": user_id,
                "expireTime": expire_time,
                "token": token,
            }
            response = await client.request(
                "PUT", 
                f"/access-tokens/{id}", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class DeleteAccessTokens(FastMCPTool):
    """Tool to delete_token_notes"""

    name = "delete_access_tokens"
    description = "DELETE_TOKEN_NOTES"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32"
                }
        },
        "required": [
                "id"
        ]
}

    async def _run(self, id) -> Dict:
        """Execute the DELETE operation on /access-tokens/{id}."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "DELETE", 
                f"/access-tokens/{id}"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetAccessTokens(FastMCPTool):
    """Tool to 分页查询access token列表"""

    name = "get_access_tokens"
    description = "分页查询access token列表"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "page_no": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u7801\u53f7"
                },
                "search_val": {
                        "type": "string",
                        "description": "\u641c\u7d22\u503c"
                },
                "page_size": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u5927\u5c0f"
                }
        },
        "required": [
                "page_no",
                "page_size"
        ]
}

    async def _run(self, page_no, search_val, page_size) -> Dict:
        """Execute the GET operation on /access-tokens."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "pageNo": page_no,
                "searchVal": search_val,
                "pageSize": page_size,
            }
            response = await client.request(
                "GET", 
                f"/access-tokens", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateAccessTokens(FastMCPTool):
    """Tool to 为指定用户创建安全令牌"""

    name = "create_access_tokens"
    description = "为指定用户创建安全令牌"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "user_id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u7528\u6237ID"
                },
                "expire_time": {
                        "type": "string",
                        "description": "\u5b89\u5168\u4ee4\u724c\u7684\u8fc7\u671f\u65f6\u95f4"
                },
                "token": {
                        "type": "string",
                        "description": "\u5b89\u5168\u4ee4\u724c\u5b57\u7b26\u4e32\uff0c\u82e5\u672a\u663e\u5f0f\u6307\u5b9a\u5c06\u4f1a\u81ea\u52a8\u751f\u6210"
                }
        },
        "required": [
                "user_id",
                "expire_time"
        ]
}

    async def _run(self, user_id, expire_time, token) -> Dict:
        """Execute the POST operation on /access-tokens."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": user_id,
                "expireTime": expire_time,
                "token": token,
            }
            response = await client.request(
                "POST", 
                f"/access-tokens", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateAccessTokensGenerate(FastMCPTool):
    """Tool to no description available."""

    name = "create_access_tokens_generate"
    description = "No description available."
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "user_id": {
                        "type": "integer",
                        "format": "int32"
                },
                "expire_time": {
                        "type": "string"
                }
        },
        "required": [
                "user_id",
                "expire_time"
        ]
}

    async def _run(self, user_id, expire_time) -> Dict:
        """Execute the POST operation on /access-tokens/generate."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": user_id,
                "expireTime": expire_time,
            }
            response = await client.request(
                "POST", 
                f"/access-tokens/generate", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetAccessTokensUser(FastMCPTool):
    """Tool to 查询指定用户的access token"""

    name = "get_access_tokens_user"
    description = "查询指定用户的access token"
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
        """Execute the GET operation on /access-tokens/user/{userId}."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/access-tokens/user/{user_id}"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register___token_____tools(mcp):
    """Register __token____ tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, CreateAccessTokens)
    register_tool_class(mcp, CreateAccessTokensGenerate)
    register_tool_class(mcp, DeleteAccessTokens)
    register_tool_class(mcp, GetAccessTokens)
    register_tool_class(mcp, GetAccessTokensUser)
    register_tool_class(mcp, UpdateAccessTokens)
