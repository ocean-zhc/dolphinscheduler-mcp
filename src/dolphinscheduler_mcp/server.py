"""DolphinScheduler MCP Server implementation using FastMCP."""

import logging
import sys
import os
from typing import Dict, List, Optional

# Clear module cache for fastmcp_compat
if "dolphinscheduler_mcp.fastmcp_compat" in sys.modules:
    del sys.modules["dolphinscheduler_mcp.fastmcp_compat"]

from mcp.server.fastmcp import FastMCP

# 导入工具加载器
from .tools_loader import register_all_generated_tools as register_all_tools
from .config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP(
    title="DolphinScheduler MCP",
    description="MCP interface for DolphinScheduler API",
)

def register_tools() -> None:
    """Register all tools with the MCP server."""
    # Check environment variables first
    api_url = os.environ.get("DOLPHINSCHEDULER_API_URL")
    api_key = os.environ.get("DOLPHINSCHEDULER_API_KEY")
    
    # Update config if environment variables are set
    if api_url or api_key:
        config = Config()
        if api_url:
            logger.info(f"Using API URL from environment: {api_url}")
            config.api_url = api_url
        if api_key:
            logger.info("Using API key from environment")
            config.api_key = api_key
    
    # 注册工具
    try:
        logger.info("Registering tools...")
        count = register_all_tools(mcp)
        logger.info(f"Registered {count} tool modules successfully")
    except Exception as e:
        logger.error(f"Error registering tools: {e}", exc_info=True)

# Register all tools
register_tools()

def run_server(host: str = "0.0.0.0", port: int = 8089) -> None:
    """Run the DolphinScheduler MCP server.
    
    Args:
        host: Host to bind the server to
        port: Port to bind the server to
    """
    logger.info(f"Starting DolphinScheduler MCP Server on {host}:{port}")
    logger.info(f"API URL: {Config().api_url}")
    logger.info(f"API Key is {'set' if Config().has_api_key() else 'not set'}")
    
    try:
        # FastMCP.run() does not accept uvicorn_config parameter
        # Simply call run() without parameters
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Error running server: {e}", exc_info=True)
        sys.exit(1) 