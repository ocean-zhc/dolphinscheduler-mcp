"""Tool loader for DolphinScheduler MCP.

This module provides utilities to load tools from the tools directory.
"""

import importlib
import importlib.util
import os
import sys
import logging
from pathlib import Path
from typing import List, Optional

from mcp.server.fastmcp import FastMCP

logger = logging.getLogger(__name__)

def get_tools_dir() -> Path:
    """Get the path to the tools directory.
    
    Returns:
        Path to the tools directory
    """
    return Path(__file__).parent / "tools"

def get_tools_generated_dir() -> Path:
    """Get the path to the tools_generated directory.
    
    Returns:
        Path to the tools_generated directory
    """
    return Path(__file__).parent / "tools_generated"

def is_tool_module(filename: str) -> bool:
    """Check if a file is a tool module.
    
    Args:
        filename: Filename to check
        
    Returns:
        True if the file is a tool module, False otherwise
    """
    return (
        filename.endswith(".py") 
        and not filename.startswith("__") 
        and not filename.startswith("_")
    )


def get_tool_modules() -> List[str]:
    """Get a list of all tool modules.
    
    Returns:
        List of tool module names
    """
    tools_dir = get_tools_dir()
    if not tools_dir.exists():
        return []
    
    return [
        f.stem 
        for f in tools_dir.glob("*.py") 
        if is_tool_module(f.name)
    ]


def import_tools_module(module_name: str) -> Optional[object]:
    """Import a tools module.
    
    Args:
        module_name: Name of the module to import
        
    Returns:
        The imported module, or None if the module could not be imported
    """
    try:
        module = importlib.import_module(f"dolphinscheduler_mcp.tools.{module_name}")
        return module
    except ImportError as e:
        logger.error(f"Error importing module {module_name}: {e}")
        return None

def ensure_env_variables():
    """Ensure environment variables are properly set.
    
    Logs warnings if required environment variables are missing.
    """
    # Check if API URL and key are set in environment variables
    api_url = os.environ.get("DOLPHINSCHEDULER_API_URL")
    api_key = os.environ.get("DOLPHINSCHEDULER_API_KEY")
    
    if not api_url:
        logger.warning("DOLPHINSCHEDULER_API_URL environment variable is not set.")
        logger.warning("Using default URL from Config class.")
    else:
        logger.info(f"Using API URL: {api_url}")
    
    if not api_key:
        logger.warning("DOLPHINSCHEDULER_API_KEY environment variable is not set.")
        logger.warning("Authentication to the DolphinScheduler API may fail.")
    else:
        logger.info("API Key is set and will be used for authentication")

def register_all_generated_tools(mcp: FastMCP) -> int:
    """Register all tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with
        
    Returns:
        Number of modules successfully registered
    """
    # Make sure environment variables are properly set
    ensure_env_variables()
    
    try:
        # Import the register_all_tools function from tools_generated
        from dolphinscheduler_mcp.tools_generated import register_all_tools
        
        # Register all tools
        register_all_tools(mcp)
        
        # Count the number of tool modules in tools_generated
        tools_generated_dir = get_tools_generated_dir()
        if tools_generated_dir.exists():
            tool_count = len([
                f for f in tools_generated_dir.glob("*.py")
                if is_tool_module(f.name)
            ])
            return tool_count
        return 0
    except ImportError as e:
        logger.error(f"Error importing tools_generated: {e}")
        return 0
    except Exception as e:
        logger.error(f"Error registering tools: {e}")
        return 0 