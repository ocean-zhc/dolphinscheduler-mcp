"""Tools for CLOUD_TAG operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class ListCloudAzureDatafactoryResourcegroups(FastMCPTool):
    """Tool to list_resource_group"""

    name = "list_cloud_azure_datafactory_resourcegroups"
    description = "LIST_RESOURCE_GROUP"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /cloud/azure/datafactory/resourceGroups."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/cloud/azure/datafactory/resourceGroups"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListCloudAzureDatafactoryPipelines(FastMCPTool):
    """Tool to list_pipeline"""

    name = "list_cloud_azure_datafactory_pipelines"
    description = "LIST_PIPELINE"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "factoryName": {
                        "type": "string"
                },
                "resourceGroupName": {
                        "type": "string"
                }
        },
        "required": [
                "factoryName",
                "resourceGroupName"
        ]
}

    async def _run(self, factoryName, resourceGroupName) -> Dict:
        """Execute the GET operation on /cloud/azure/datafactory/pipelines."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "factoryName": factoryName,
                "resourceGroupName": resourceGroupName,
            }
            response = await client.request(
                "GET", 
                f"/cloud/azure/datafactory/pipelines", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListCloudAzureDatafactoryFactories(FastMCPTool):
    """Tool to list_data_factory"""

    name = "list_cloud_azure_datafactory_factories"
    description = "LIST_DATA_FACTORY"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /cloud/azure/datafactory/factories."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/cloud/azure/datafactory/factories"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register_CLOUD_TAG_tools(mcp):
    """Register CLOUD_TAG tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, ListCloudAzureDatafactoryFactories)
    register_tool_class(mcp, ListCloudAzureDatafactoryPipelines)
    register_tool_class(mcp, ListCloudAzureDatafactoryResourcegroups)
