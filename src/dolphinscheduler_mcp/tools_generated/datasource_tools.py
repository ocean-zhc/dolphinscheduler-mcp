"""Tools for data source operations in DolphinScheduler."""

from typing import Dict, List, Optional

from ..fastmcp_compat import FastMCPTool

from ..client import DolphinSchedulerClient


class GetDatasources(FastMCPTool):
    """Tool to 查询数据源通过id"""

    name = "get_datasources"
    description = "查询数据源通过ID"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u6570\u636e\u6e90ID"
                }
        },
        "required": [
                "id"
        ]
}

    async def _run(self, id) -> Dict:
        """Execute the GET operation on /datasources/{id}."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/datasources/{id}"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class UpdateDatasources(FastMCPTool):
    """Tool to 更新数据源"""

    name = "update_datasources"
    description = "更新数据源"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u6570\u636e\u6e90ID"
                },
                "data_source_param": {
                        "type": "object",
                        "description": "\u6570\u636e\u6e90\u53c2\u6570"
                }
        },
        "required": [
                "id",
                "data_source_param"
        ]
}

    async def _run(self, id, data_source_param) -> Dict:
        """Execute the PUT operation on /datasources/{id}."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "PUT", 
                f"/datasources/{id}"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class DeleteDatasources(FastMCPTool):
    """Tool to 删除数据源"""

    name = "delete_datasources"
    description = "删除数据源"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u6570\u636e\u6e90ID"
                }
        },
        "required": [
                "id"
        ]
}

    async def _run(self, id) -> Dict:
        """Execute the DELETE operation on /datasources/{id}."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "DELETE", 
                f"/datasources/{id}"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetDatasources2(FastMCPTool):
    """Tool to 分页查询数据源列表"""

    name = "get_datasources2"
    description = "分页查询数据源列表"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "search_val": {
                        "type": "string",
                        "description": "\u641c\u7d22\u503c"
                },
                "page_no": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u7801\u53f7"
                },
                "page_size": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u9875\u5927\u5c0f"
                }
        },
        "required": [
                "page_no",
                "page_size"
        ]
}

    async def _run(self, search_val, page_no, page_size) -> Dict:
        """Execute the GET operation on /datasources."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "searchVal": search_val,
                "pageNo": page_no,
                "pageSize": page_size,
            }
            response = await client.request(
                "GET", 
                f"/datasources", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateDatasources(FastMCPTool):
    """Tool to 创建数据源"""

    name = "create_datasources"
    description = "创建数据源"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the POST operation on /datasources."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "POST", 
                f"/datasources"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class CreateDatasourcesConnect(FastMCPTool):
    """Tool to 连接数据源"""

    name = "create_datasources_connect"
    description = "连接数据源"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the POST operation on /datasources/connect."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "POST", 
                f"/datasources/connect"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetDatasourcesConnectTest(FastMCPTool):
    """Tool to 连接数据源测试"""

    name = "get_datasources_connect_test"
    description = "连接数据源测试"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u6570\u636e\u6e90ID"
                }
        },
        "required": [
                "id"
        ]
}

    async def _run(self, id) -> Dict:
        """Execute the GET operation on /datasources/{id}/connect-test."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/datasources/{id}/connect-test"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetDatasourcesVerifyName(FastMCPTool):
    """Tool to 验证数据源"""

    name = "get_datasources_verify_name"
    description = "验证数据源"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "name": {
                        "type": "string",
                        "description": "\u6570\u636e\u6e90\u540d\u79f0"
                }
        },
        "required": [
                "name"
        ]
}

    async def _run(self, name) -> Dict:
        """Execute the GET operation on /datasources/verify-name."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "name": name,
            }
            response = await client.request(
                "GET", 
                f"/datasources/verify-name", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetDatasourcesUnauthDatasource(FastMCPTool):
    """Tool to 未授权的数据源"""

    name = "get_datasources_unauth_datasource"
    description = "未授权的数据源"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "user_id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u7528\u6237ID"
                }
        },
        "required": [
                "user_id"
        ]
}

    async def _run(self, user_id) -> Dict:
        """Execute the GET operation on /datasources/unauth-datasource."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": user_id,
            }
            response = await client.request(
                "GET", 
                f"/datasources/unauth-datasource", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListDatasourcesTables(FastMCPTool):
    """Tool to 获取数据源表列表"""

    name = "list_datasources_tables"
    description = "获取数据源表列表"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "datasource_id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u6570\u636e\u6e90ID"
                },
                "database": {
                        "type": "string",
                        "description": "DATABASE"
                }
        },
        "required": [
                "datasource_id",
                "database"
        ]
}

    async def _run(self, datasource_id, database) -> Dict:
        """Execute the GET operation on /datasources/tables."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "datasourceId": datasource_id,
                "database": database,
            }
            response = await client.request(
                "GET", 
                f"/datasources/tables", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListDatasourcesTablecolumns(FastMCPTool):
    """Tool to 获取数据源表列名"""

    name = "list_datasources_tablecolumns"
    description = "获取数据源表列名"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "datasource_id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u6570\u636e\u6e90ID"
                },
                "table_name": {
                        "type": "string",
                        "description": "\u8868\u540d"
                },
                "database": {
                        "type": "string",
                        "description": "DATABASE"
                }
        },
        "required": [
                "datasource_id",
                "table_name",
                "database"
        ]
}

    async def _run(self, datasource_id, table_name, database) -> Dict:
        """Execute the GET operation on /datasources/tableColumns."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "datasourceId": datasource_id,
                "tableName": table_name,
                "database": database,
            }
            response = await client.request(
                "GET", 
                f"/datasources/tableColumns", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListDatasourcesList(FastMCPTool):
    """Tool to 通过数据源类型查询数据源列表"""

    name = "list_datasources_list"
    description = "通过数据源类型查询数据源列表"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "type": {
                        "type": "string",
                        "enum": [
                                "MYSQL",
                                "POSTGRESQL",
                                "HIVE",
                                "SPARK",
                                "CLICKHOUSE",
                                "ORACLE",
                                "SQLSERVER",
                                "DB2",
                                "PRESTO",
                                "H2",
                                "REDSHIFT",
                                "ATHENA",
                                "TRINO",
                                "STARROCKS",
                                "AZURESQL",
                                "DAMENG",
                                "OCEANBASE",
                                "SSH",
                                "KYUUBI",
                                "DATABEND",
                                "SNOWFLAKE",
                                "VERTICA",
                                "HANA",
                                "DORIS",
                                "ZEPPELIN",
                                "SAGEMAKER"
                        ],
                        "description": "\u6570\u636e\u6e90\u7c7b\u578b"
                }
        },
        "required": [
                "type"
        ]
}

    async def _run(self, type) -> Dict:
        """Execute the GET operation on /datasources/list."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "type": type,
            }
            response = await client.request(
                "GET", 
                f"/datasources/list", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetDatasourcesKerberosStartupState(FastMCPTool):
    """Tool to 获取用户信息"""

    name = "get_datasources_kerberos_startup_state"
    description = "获取用户信息"
    is_async = True

    async def _run(self) -> Dict:
        """Execute the GET operation on /datasources/kerberos-startup-state."""
        client = DolphinSchedulerClient()
        try:
            response = await client.request(
                "GET", 
                f"/datasources/kerberos-startup-state"
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class ListDatasourcesDatabases(FastMCPTool):
    """Tool to get_datasource_database_notes"""

    name = "list_datasources_databases"
    description = "GET_DATASOURCE_DATABASE_NOTES"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "datasource_id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u6570\u636e\u6e90ID"
                }
        },
        "required": [
                "datasource_id"
        ]
}

    async def _run(self, datasource_id) -> Dict:
        """Execute the GET operation on /datasources/databases."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "datasourceId": datasource_id,
            }
            response = await client.request(
                "GET", 
                f"/datasources/databases", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


class GetDatasourcesAuthedDatasource(FastMCPTool):
    """Tool to 授权的数据源"""

    name = "get_datasources_authed_datasource"
    description = "授权的数据源"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
                "user_id": {
                        "type": "integer",
                        "format": "int32",
                        "description": "\u7528\u6237ID"
                }
        },
        "required": [
                "user_id"
        ]
}

    async def _run(self, user_id) -> Dict:
        """Execute the GET operation on /datasources/authed-datasource."""
        client = DolphinSchedulerClient()
        try:
            params = {
                "userId": user_id,
            }
            response = await client.request(
                "GET", 
                f"/datasources/authed-datasource", params=params
            )
            return {"success": True, "data": response}
        finally:
            await client.close()


def register_datasource_tools(mcp):
    """Register datasource tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    register_tool_class(mcp, CreateDatasources)
    register_tool_class(mcp, CreateDatasourcesConnect)
    register_tool_class(mcp, DeleteDatasources)
    register_tool_class(mcp, GetDatasources)
    register_tool_class(mcp, GetDatasources2)
    register_tool_class(mcp, GetDatasourcesAuthedDatasource)
    register_tool_class(mcp, GetDatasourcesConnectTest)
    register_tool_class(mcp, GetDatasourcesKerberosStartupState)
    register_tool_class(mcp, GetDatasourcesUnauthDatasource)
    register_tool_class(mcp, GetDatasourcesVerifyName)
    register_tool_class(mcp, ListDatasourcesDatabases)
    register_tool_class(mcp, ListDatasourcesList)
    register_tool_class(mcp, ListDatasourcesTablecolumns)
    register_tool_class(mcp, ListDatasourcesTables)
    register_tool_class(mcp, UpdateDatasources)
