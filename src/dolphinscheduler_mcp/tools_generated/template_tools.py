"""Template for creating new tools in DolphinScheduler MCP.

这是一个工具模板文件，用于创建新的DolphinScheduler MCP工具。
复制此文件并修改内容以创建新的工具。

注意：
1. 确保正确处理路径参数
2. 添加适当的错误处理
3. 所有请求都应包含 Token 认证头
"""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool
from ..client import DolphinSchedulerClient


class TemplatePathParameterTool(FastMCPTool):
    """包含路径参数的工具模板"""

    name = "template_path_parameter_tool"
    description = "包含路径参数的工具模板"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "资源ID"
                }
        },
        "required": [
                "id"
        ]
    }

    async def _run(self, id) -> Dict:
        """执行包含路径参数的API请求
        
        Args:
            id: 资源ID
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 确保路径参数正确处理
            resource_id = int(id) if id is not None else None
            if resource_id is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: id"
                }
                
            response = await client.request(
                "GET", 
                f"/resources/{resource_id}"
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


class TemplateQueryParameterTool(FastMCPTool):
    """包含查询参数的工具模板"""

    name = "template_query_parameter_tool"
    description = "包含查询参数的工具模板"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "search_val": {
                        "type": "string",
                        "description": "搜索值"
                },
                "page_no": {
                        "type": "integer",
                        "format": "int32",
                        "description": "页码"
                },
                "page_size": {
                        "type": "integer",
                        "format": "int32",
                        "description": "每页大小"
                }
        },
        "required": [
                "page_no",
                "page_size"
        ]
    }

    async def _run(self, search_val, page_no, page_size) -> Dict:
        """执行包含查询参数的API请求
        
        Args:
            search_val: 搜索值
            page_no: 页码
            page_size: 每页大小
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 验证必要参数
            if page_no is None or page_size is None:
                return {
                    "success": False, 
                    "error": "Missing required parameters: page_no, page_size"
                }
                
            # 构建查询参数
            params = {
                "searchVal": search_val,
                "pageNo": page_no,
                "pageSize": page_size,
            }
            
            response = await client.request(
                "GET", 
                "/resources", 
                params=params
            )
            return {"success": True, "data": response}
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            await client.close()


class TemplatePostTool(FastMCPTool):
    """包含POST请求的工具模板"""

    name = "template_post_tool"
    description = "包含POST请求的工具模板"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "name": {
                        "type": "string",
                        "description": "资源名称"
                },
                "description": {
                        "type": "string",
                        "description": "资源描述"
                }
        },
        "required": [
                "name"
        ]
    }

    async def _run(self, name, description) -> Dict:
        """执行POST请求创建资源
        
        Args:
            name: 资源名称
            description: 资源描述
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 验证必要参数
            if not name:
                return {
                    "success": False, 
                    "error": "Missing required parameter: name"
                }
                
            # 构建请求体
            json_data = {
                "name": name,
                "desc": description or ""
            }
            
            response = await client.request(
                "POST", 
                "/resources", 
                json_data=json_data
            )
            return {"success": True, "data": response}
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            await client.close()


# 注册工具
def register_template_tools(mcp):
    """注册模板工具
    
    Args:
        mcp: FastMCP实例
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, TemplatePathParameterTool)
    register_tool_class(mcp, TemplateQueryParameterTool)
    register_tool_class(mcp, TemplatePostTool) 