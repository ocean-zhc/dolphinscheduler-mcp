"""Compatibility layer for FastMCP.

This module provides a FastMCPTool class that emulates the old interface,
but actually uses the new MCP API under the hood.
"""

from typing import Any, Dict, Optional, Type, TypeVar, get_type_hints
import inspect

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.tools import Tool
from mcp.types import TextContent, ImageContent, EmbeddedResource

T = TypeVar('T', bound='FastMCPTool')


class FastMCPTool:
    """Base class for FastMCP tools that emulates the old interface."""

    name: str
    description: str
    is_async: bool = True
    schema: Dict[str, Any]

    def __init__(self, mcp: FastMCP):
        """Initialize the tool with the MCP instance."""
        self.mcp = mcp
        self._register()

    def _register(self):
        """Register the tool with the MCP instance."""
        if not hasattr(self, '_run'):
            raise NotImplementedError(f"Tool {self.__class__.__name__} must implement _run")

        # Get the run method
        run_method = getattr(self, '_run')
        
        # Get the parameters from the type hints
        type_hints = get_type_hints(run_method)
        
        # Remove return type if present
        if 'return' in type_hints:
            del type_hints['return']
        
        # Get the signature
        sig = inspect.signature(run_method)
        
        # Remove 'self' parameter
        parameters = list(sig.parameters.values())
        if parameters and parameters[0].name == 'self':
            parameters = parameters[1:]
        
        # 获取 schema 中定义的参数
        param_names = []
        if hasattr(self, 'schema') and self.schema and 'properties' in self.schema:
            param_names = list(self.schema['properties'].keys())
        else:
            param_names = [p.name for p in parameters]
        
        # 构造接收具体参数的装饰器函数
        # 这是为了避免使用 *args, **kwargs 通用参数
        param_decl = ", ".join(param_names)
        
        # 创建工具函数的代码
        tool_func_code = f"""
async def tool_fn({param_decl}):
    \"\"\"
    {self.description}
    \"\"\"
    # 调用原始 run 方法
    result = await self._run({param_decl})
    # 返回文本内容
    return TextContent(type="text", text=str(result))
"""
        
        # 执行代码创建函数
        namespace = {
            'self': self,
            'TextContent': TextContent
        }
        exec(tool_func_code, namespace)
        tool_fn = namespace['tool_fn']
        
        # 装饰并注册工具
        self.mcp.tool(name=self.name, description=self.description)(tool_fn)

    @classmethod
    def register(cls: Type[T], mcp: FastMCP) -> T:
        """Register the tool with the MCP instance."""
        return cls(mcp)


def register_tool_class(mcp: FastMCP, tool_class: Type[FastMCPTool]) -> FastMCPTool:
    """Register a tool class with the MCP instance."""
    return tool_class.register(mcp) 