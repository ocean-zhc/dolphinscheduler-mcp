# __init__.py
"""Tools package for DolphinScheduler MCP."""

from mcp.server.fastmcp import FastMCP

# Import registration functions for each tool module
from .azure_data_factory_tools import register_azure_data_factory_tools
from .dynamic_task_type_tools import register_dynamic_task_type_tools
from .k8s_namespace_tools import register_k8s_namespace_tools
from .project_worker_group_tools import register_project_worker_group_tools
from .ui_plugin_tools import register_ui_plugin_tools
from .worker_group_tools import register_worker_group_tools
from .project_tools import register_project_tools
from .datasource_tools import register_datasource_tools
from .project_parameter_tools import register_project_parameter_tools
from .lineage_tools import register_lineage_tools
from .audit_log_tools import register_audit_log_tools
from .access_token_tools import register_access_token_tools
from .project_preference_tools import register_project_preference_tools
from .environment_check_tools import register_environment_check_tools
from .environment_update_tools import register_environment_update_tools
from .process_task_relation_tools import register_process_task_relation_tools

# The all_tools list is no longer used since we now rely on registration functions
all_tools = []


def register_all_tools(mcp: FastMCP) -> None:
    """Register all available tools with the FastMCP instance.

    Args:
        mcp: The FastMCP instance to register tools with.
    """
    # Register Cloud-related Tools (e.g., Azure Data Factory)
    register_azure_data_factory_tools(mcp)

    # Register Dynamic Task Type Tools
    register_dynamic_task_type_tools(mcp)

    # Register Kubernetes Namespace Tools
    register_k8s_namespace_tools(mcp)

    # Register Project Worker Group Tools
    register_project_worker_group_tools(mcp)

    # Register UI Plugin Tools
    register_ui_plugin_tools(mcp)

    # Register Worker Group Tools
    register_worker_group_tools(mcp)

    # Register Project Management Tools
    register_project_tools(mcp)

    # Register Datasource Management Tools
    register_datasource_tools(mcp)

    # Register Project Parameter Tools
    register_project_parameter_tools(mcp)

    # Register Data Lineage Tools
    register_lineage_tools(mcp)

    # Register Audit Log Tools
    register_audit_log_tools(mcp)

    # Register Access Token Tools
    register_access_token_tools(mcp)

    # Register Project Preference Tools
    register_project_preference_tools(mcp)

    # Register Environment Check Tools
    register_environment_check_tools(mcp)

    # Register Environment Update Tools
    register_environment_update_tools(mcp)

    # Register Process-Task Relation Tools
    register_process_task_relation_tools(mcp)


__all__ = ["all_tools", "register_all_tools"]
