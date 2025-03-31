"""Tools package for DolphinScheduler MCP."""

from mcp.server.fastmcp import FastMCP

from .CLOUD_TAG import register_CLOUD_TAG_tools
from .DYNAMIC_TASK_TYPE import register_DYNAMIC_TASK_TYPE_tools
from .K8S________ import register_K8S_________tools
from .PROJECT_WORKER_GROUP_TAG import register_PROJECT_WORKER_GROUP_TAG_tools
from .UI______ import register_UI_______tools
from .Worker____ import register_Worker_____tools
from .______ import register________tools
from ._______ import register_________tools
from .________ import register__________tools
from ._________ import register___________tools
from .__________ import register____________tools
from .__token____ import register___token_____tools
from .project_preference_related_operation import register_project_preference_related_operation_tools
from .check_env import register_check_env_tools
from .update_env import register_update_env_tools
from .process_task_relation import register_process_task_relation_tools

# Empty all_tools list since we're now using registration functions
all_tools = []

def register_all_tools(mcp: FastMCP) -> None:
    """Register all tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    # Register CLOUD_TAG tools
    register_CLOUD_TAG_tools(mcp)

    # Register DYNAMIC_TASK_TYPE tools
    register_DYNAMIC_TASK_TYPE_tools(mcp)

    # Register K8S________ tools
    register_K8S_________tools(mcp)

    # Register PROJECT_WORKER_GROUP_TAG tools
    register_PROJECT_WORKER_GROUP_TAG_tools(mcp)

    # Register UI______ tools
    register_UI_______tools(mcp)

    # Register Worker____ tools
    register_Worker_____tools(mcp)

    # Register ______ tools
    register________tools(mcp)

    # Register _______ tools
    register_________tools(mcp)

    # Register ________ tools
    register__________tools(mcp)

    # Register _________ tools
    register___________tools(mcp)

    # Register __________ tools
    register____________tools(mcp)

    # Register __token____ tools
    register___token_____tools(mcp)

    # Register project_preference_related_operation tools
    register_project_preference_related_operation_tools(mcp)
    
    # Register check_env tools
    register_check_env_tools(mcp)
    
    # Register update_env tools
    register_update_env_tools(mcp)
    
    # Register process_task_relation tools
    register_process_task_relation_tools(mcp)

__all__ = ["all_tools", "register_all_tools"]
