"""Tool for updating environment settings."""

import json
import logging
import os
from typing import Dict, Any, Optional

from ..client import DolphinSchedulerClient
from ..config import Config
from ..fastmcp_compat import FastMCPTool

class UpdateEnvironmentSettings(FastMCPTool):
    """Tool for updating the environment settings for DolphinScheduler API."""
    
    name = "update_connection_settings"
    description = "更新DolphinScheduler API连接设置"
    is_async = True
    
    schema = {
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                "description": "No description"
            },
            "api_url": {
                "type": "string",
                "description": "New API URL to set"
            },
            "api_key": {
                "type": "string",
                "description": "New API key to set"
            }
        },
        "required": []
    }
    
    async def _run(self, id: Optional[str] = None, api_url: Optional[str] = None, api_key: Optional[str] = None) -> Dict[str, Any]:
        """Update the environment settings.
        
        Args:
            id: Not used, included for compatibility with FastMCP
            api_url: New API URL to set (optional)
            api_key: New API key to set (optional)
            
        Returns:
            Dictionary containing updated settings
        """
        logger = logging.getLogger("dolphinscheduler_mcp.tools.update_env")
        
        try:
            config = Config()
            
            # Update API URL if provided
            if api_url is not None:
                logger.info(f"Updating API URL to: {api_url}")
                config.api_url = api_url
                os.environ["DOLPHINSCHEDULER_API_URL"] = api_url
            
            # Update API key if provided
            if api_key is not None:
                logger.info("Updating API key")
                config.api_key = api_key
                os.environ["DOLPHINSCHEDULER_API_KEY"] = api_key
            
            return {
                "success": True,
                "api_url": config.api_url,
                "has_api_key": config.has_api_key()
            }
        except Exception as e:
            logger.error(f"Error updating environment settings: {e}")
            return {
                "success": False,
                "error": str(e)
            }

def register_update_env_tools(mcp):
    """Register environment update tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, UpdateEnvironmentSettings) 