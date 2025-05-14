"""Tools for audit log operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class GetProjectsAuditAuditLogOperationType(FastMCPTool):
    """Tool to query_audit_operation_type_list"""

    name = "get_projects_audit_audit_log_operation_type"
    description = "QUERY_AUDIT_OPERATION_TYPE_LIST"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /projects/audit/audit-log-operation-type."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/audit/audit-log-operation-type"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsAuditAuditLogModelType(FastMCPTool):
    """Tool to query_audit_model_type_list"""

    name = "get_projects_audit_audit_log_model_type"
    description = "QUERY_AUDIT_MODEL_TYPE_LIST"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /projects/audit/audit-log-model-type."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/projects/audit/audit-log-model-type"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetProjectsAuditAuditLogList(FastMCPTool):
    """Tool to 查询审计日志"""

    name = "get_projects_audit_audit_log_list"
    description = "查询审计日志"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "page_no": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u7801\u53f7"
                },
                "page_size": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u5927\u5c0f"
                },
                "model_types": {
                        "type": "string"
                },
                "operation_types": {
                        "type": "string",
                        "description": "OPERATION_TYPES"
                },
                "start_date": {
                        "type": "string",
                        "description": "\u5f00\u59cb\u65f6\u95f4"
                },
                "end_date": {
                        "type": "string",
                        "description": "\u7ed3\u675f\u65f6\u95f4"
                },
                "user_name": {
                        "type": "string",
                        "description": "\u7528\u6237\u540d"
                },
                "model_name": {
                        "type": "string"
                },
                "object_types": {
                        "type": "string",
                        "description": "MODEL_TYPES"
                },
                "object_name": {
                        "type": "string",
                        "description": "MODEL_NAME"
                }
        },
        "required": [
                "page_no",
                "page_size"
        ]
}

    async def _run(self, page_no, page_size, model_types, operation_types, start_date, end_date, user_name, model_name, object_types, object_name) -> Dict:
        """Execute the GET operation on /projects/audit/audit-log-list."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "pageNo": page_no,
                "pageSize": page_size,
                "modelTypes": model_types,
                "operationTypes": operation_types,
                "startDate": start_date,
                "endDate": end_date,
                "userName": user_name,
                "modelName": model_name,
            }
            response = await client.request(
                "GET", 
                f"/projects/audit/audit-log-list", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register_audit_log_tools(mcp):
    """Register audit log tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, GetProjectsAuditAuditLogList)
    register_tool_class(mcp, GetProjectsAuditAuditLogModelType)
    register_tool_class(mcp, GetProjectsAuditAuditLogOperationType)
