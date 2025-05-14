"""Tool for checking environment settings."""

import json
import logging
from typing import Dict, Any, Optional

from ..client import DolphinSchedulerClient
from ..config import Config
from ..fastmcp_compat import FastMCPTool


class CheckEnvironmentSettings(FastMCPTool):
    """Tool for checking the current environment settings for DolphinScheduler API."""

    name = "check_environment_settings"
    description = "Check the current environment settings for DolphinScheduler API"
    is_async = False
    schema = {
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                "description": "Not used, included for compatibility with FastMCP"
            }
        }
    }

    def _run(self, id: Optional[str] = None) -> Dict[str, Any]:
        """Check the current environment settings.
        
        Args:
            id: Not used, included for compatibility with FastMCP
            
        Returns:
            Dictionary containing current settings
        """
        try:
            config = Config()

            return {
                "success": True,
                "api_url": config.api_url,
                "has_api_key": config.has_api_key(),
                "api_key_value": config.api_key if config.has_api_key() else None
            }
        except Exception as e:
            self.logger.error(f"Error checking environment settings: {e}")
            return {
                "success": False,
                "error": str(e)
            }


def register_environment_check_tools(mcp):
    """Register environment check tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class

    register_tool_class(mcp, CheckEnvironmentSettings)
