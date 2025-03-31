"""Tools for UI______ operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class GetUiPlugins(FastMCPTool):
    """Tool to 通过id查询ui插件详情"""

    name = "get_ui_plugins"
    description = "通过ID查询UI插件详情"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u63d2\u4ef6ID"
                }
        },
        "required": [
                "id"
        ]
}

    async def _run(self, id) -> Dict:
        """Execute the GET operation on /ui-plugins/{id}.
        
        Args:
            id: 插件ID
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 确保路径参数正确处理
            plugin_id = int(id) if id is not None else None
            if plugin_id is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: id"
                }
            
            response = await client.request(
                "GET", 
                f"/ui-plugins/{plugin_id}"
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


class GetUiPluginsQueryByType(FastMCPTool):
    """Tool to 通过类型查询ui插件"""

    name = "get_ui_plugins_query_by_type"
    description = "通过类型查询UI插件"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "plugin_type": {
                        "type": "string",
                        "enum": [
                                "ALERT",
                                "REGISTER",
                                "TASK"
                        ],
                        "description": "pluginType"
                }
        },
        "required": [
                "plugin_type"
        ]
}

    async def _run(self, plugin_type) -> Dict:
        """Execute the GET operation on /ui-plugins/query-by-type.
        
        Args:
            plugin_type: 插件类型
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            if not plugin_type:
                return {
                    "success": False, 
                    "error": "Missing required parameter: plugin_type"
                }
                
            params = {
                "pluginType": plugin_type,
            }
            response = await client.request(
                "GET", 
                f"/ui-plugins/query-by-type", 
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


def register_UI_______tools(mcp):
    """Register UI______ tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, GetUiPlugins)
    register_tool_class(mcp, GetUiPluginsQueryByType)
