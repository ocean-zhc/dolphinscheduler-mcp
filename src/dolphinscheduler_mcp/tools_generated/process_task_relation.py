"""Process Task Relation related operations for DolphinScheduler MCP.

This module provides tools for managing workflow task relationships in DolphinScheduler.
"""

from typing import Dict, List, Optional, Any
import logging

from ..fastmcp_compat import FastMCPTool
from ..client import DolphinSchedulerClient

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.info("Loading process_task_relation tools module")


class CreateProcessTaskRelation(FastMCPTool):
    """创建工作流任务关系"""

    name = "create-process-task-relation"
    description = "创建工作流任务关系"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
            "projectCode": {
                "type": "integer",
                "format": "int64",
                "description": "项目Code"
            },
            "processDefinitionCode": {
                "type": "integer",
                "format": "int64",
                "description": "流程定义编码"
            },
            "preTaskCode": {
                "type": "integer",
                "format": "int64",
                "description": "上游任务编码"
            },
            "postTaskCode": {
                "type": "integer",
                "format": "int64",
                "description": "下游任务编码"
            }
        },
        "required": [
            "projectCode",
            "processDefinitionCode",
            "preTaskCode",
            "postTaskCode"
        ]
    }

    async def _run(self, projectCode, processDefinitionCode, preTaskCode, postTaskCode) -> Dict:
        """执行创建工作流任务关系API请求
        
        Args:
            projectCode: 项目Code
            processDefinitionCode: 流程定义编码
            preTaskCode: 上游任务编码
            postTaskCode: 下游任务编码
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 确保路径参数正确处理
            projectCode = int(projectCode) if projectCode is not None else None
            if projectCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: projectCode"
                }
                
            # 确保query参数正确处理
            processDefinitionCode = int(processDefinitionCode) if processDefinitionCode is not None else None
            preTaskCode = int(preTaskCode) if preTaskCode is not None else None
            postTaskCode = int(postTaskCode) if postTaskCode is not None else None
            
            if processDefinitionCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: processDefinitionCode"
                }
                
            if preTaskCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: preTaskCode"
                }
                
            if postTaskCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: postTaskCode"
                }
            
            # 构建请求参数 (query parameters)
            params = {
                "processDefinitionCode": processDefinitionCode,
                "preTaskCode": preTaskCode,
                "postTaskCode": postTaskCode
            }
                
            response = await client.request(
                "POST", 
                f"/projects/{projectCode}/process-task-relation",
                params=params  # 这些是query参数
            )
            return {"success": True, "data": response}
        except ValueError:
            return {
                "success": False,
                "error": "Invalid parameter format"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            await client.close()


class QueryUpstreamRelation(FastMCPTool):
    """查询上游工作流任务关系"""

    name = "query-upstream-relation"
    description = "查询上游工作流任务关系"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
            "projectCode": {
                "type": "integer",
                "format": "int64",
                "description": "项目Code"
            },
            "taskCode": {
                "type": "integer",
                "format": "int64",
                "description": "任务编码"
            }
        },
        "required": [
            "projectCode",
            "taskCode"
        ]
    }

    async def _run(self, projectCode, taskCode) -> Dict:
        """执行查询上游工作流任务关系API请求
        
        Args:
            projectCode: 项目Code
            taskCode: 任务编码
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 确保path参数正确处理
            projectCode = int(projectCode) if projectCode is not None else None
            taskCode = int(taskCode) if taskCode is not None else None
            
            if projectCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: projectCode"
                }
            
            if taskCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: taskCode"
                }
            
            # 所有参数都在URL路径中，不需要额外的query参数
            response = await client.request(
                "GET", 
                f"/projects/{projectCode}/process-task-relation/{taskCode}/upstream"
            )
            return {"success": True, "data": response}
        except ValueError:
            return {
                "success": False,
                "error": "Invalid parameter format"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            await client.close()


class DeleteUpstreamRelation(FastMCPTool):
    """删除上游工作流任务关系"""

    name = "delete-upstream-relation"
    description = "删除上游工作流任务关系"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
            "projectCode": {
                "type": "integer",
                "format": "int64",
                "description": "项目Code"
            },
            "taskCode": {
                "type": "integer",
                "format": "int64",
                "description": "任务编码"
            },
            "preTaskCodes": {
                "type": "string",
                "description": "上游任务编码列表，多个用逗号分隔"
            }
        },
        "required": [
            "projectCode",
            "taskCode",
            "preTaskCodes"
        ]
    }

    async def _run(self, projectCode, taskCode, preTaskCodes) -> Dict:
        """执行删除上游工作流任务关系API请求
        
        Args:
            projectCode: 项目Code
            taskCode: 任务编码
            preTaskCodes: 上游任务编码列表，多个用逗号分隔
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 确保path参数正确处理
            projectCode = int(projectCode) if projectCode is not None else None
            taskCode = int(taskCode) if taskCode is not None else None
            
            if projectCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: projectCode"
                }
            
            if taskCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: taskCode"
                }
            
            # 确保query参数正确处理
            if preTaskCodes is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: preTaskCodes"
                }
                
            # 构建请求参数 (query parameters)
            params = {
                "preTaskCodes": preTaskCodes
            }
                
            response = await client.request(
                "DELETE", 
                f"/projects/{projectCode}/process-task-relation/{taskCode}/upstream",
                params=params  # 这些是query参数
            )
            return {"success": True, "data": response}
        except ValueError:
            return {
                "success": False,
                "error": "Invalid parameter format"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            await client.close()


class QueryDownstreamRelation(FastMCPTool):
    """查询下游工作流任务关系"""

    name = "query-downstream-relation"
    description = "查询下游工作流任务关系"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
            "projectCode": {
                "type": "integer",
                "format": "int64",
                "description": "项目Code"
            },
            "taskCode": {
                "type": "integer",
                "format": "int64",
                "description": "任务编码"
            }
        },
        "required": [
            "projectCode",
            "taskCode"
        ]
    }

    async def _run(self, projectCode, taskCode) -> Dict:
        """执行查询下游工作流任务关系API请求
        
        Args:
            projectCode: 项目Code
            taskCode: 任务编码
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 确保path参数正确处理
            projectCode = int(projectCode) if projectCode is not None else None
            taskCode = int(taskCode) if taskCode is not None else None
            
            if projectCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: projectCode"
                }
            
            if taskCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: taskCode"
                }
            
            # 所有参数都在URL路径中，不需要额外的query参数
            response = await client.request(
                "GET", 
                f"/projects/{projectCode}/process-task-relation/{taskCode}/downstream"
            )
            return {"success": True, "data": response}
        except ValueError:
            return {
                "success": False,
                "error": "Invalid parameter format"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            await client.close()


class DeleteDownstreamRelation(FastMCPTool):
    """删除下游工作流任务关系"""

    name = "delete-downstream-relation"
    description = "删除下游工作流任务关系"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
            "projectCode": {
                "type": "integer",
                "format": "int64",
                "description": "项目Code"
            },
            "taskCode": {
                "type": "integer",
                "format": "int64",
                "description": "任务编码"
            },
            "postTaskCodes": {
                "type": "string",
                "description": "下游任务编码列表，多个用逗号分隔"
            }
        },
        "required": [
            "projectCode",
            "taskCode",
            "postTaskCodes"
        ]
    }

    async def _run(self, projectCode, taskCode, postTaskCodes) -> Dict:
        """执行删除下游工作流任务关系API请求
        
        Args:
            projectCode: 项目Code
            taskCode: 任务编码
            postTaskCodes: 下游任务编码列表，多个用逗号分隔
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 确保path参数正确处理
            projectCode = int(projectCode) if projectCode is not None else None
            taskCode = int(taskCode) if taskCode is not None else None
            
            if projectCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: projectCode"
                }
            
            if taskCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: taskCode"
                }
            
            # 确保query参数正确处理
            if postTaskCodes is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: postTaskCodes"
                }
                
            # 构建请求参数 (query parameters)
            params = {
                "postTaskCodes": postTaskCodes
            }
                
            response = await client.request(
                "DELETE", 
                f"/projects/{projectCode}/process-task-relation/{taskCode}/downstream",
                params=params  # 这些是query参数
            )
            return {"success": True, "data": response}
        except ValueError:
            return {
                "success": False,
                "error": "Invalid parameter format"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            await client.close()


class DeleteTaskProcessRelation(FastMCPTool):
    """删除工作流任务关系"""

    name = "delete-task-process-relation"
    description = "删除工作流任务关系"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
            "projectCode": {
                "type": "integer",
                "format": "int64",
                "description": "项目Code"
            },
            "taskCode": {
                "type": "integer",
                "format": "int64",
                "description": "任务编码"
            },
            "processDefinitionCode": {
                "type": "integer",
                "format": "int64",
                "description": "流程定义编码"
            }
        },
        "required": [
            "projectCode",
            "taskCode",
            "processDefinitionCode"
        ]
    }

    async def _run(self, projectCode, taskCode, processDefinitionCode) -> Dict:
        """执行删除工作流任务关系API请求
        
        Args:
            projectCode: 项目Code
            taskCode: 任务编码
            processDefinitionCode: 流程定义编码
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 确保path参数正确处理
            projectCode = int(projectCode) if projectCode is not None else None
            taskCode = int(taskCode) if taskCode is not None else None
            
            if projectCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: projectCode"
                }
            
            if taskCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: taskCode"
                }
            
            # 确保query参数正确处理
            processDefinitionCode = int(processDefinitionCode) if processDefinitionCode is not None else None
            if processDefinitionCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: processDefinitionCode"
                }
                
            # 构建请求参数 (query parameters)
            params = {
                "processDefinitionCode": processDefinitionCode
            }
                
            response = await client.request(
                "DELETE", 
                f"/projects/{projectCode}/process-task-relation/{taskCode}",
                params=params  # 这些是query参数
            )
            return {"success": True, "data": response}
        except ValueError:
            return {
                "success": False,
                "error": "Invalid parameter format"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            await client.close()


class DeleteEdge(FastMCPTool):
    """删除工作流任务连接线"""

    name = "delete-edge"
    description = "删除工作流任务连接线"
    is_async = True
    schema = {
        "type": "object",
        "properties": {
            "projectCode": {
                "type": "integer",
                "format": "int64",
                "description": "项目Code"
            },
            "processDefinitionCode": {
                "type": "integer",
                "format": "int64",
                "description": "流程定义编码"
            },
            "preTaskCode": {
                "type": "integer",
                "format": "int64",
                "description": "上游任务编码"
            },
            "postTaskCode": {
                "type": "integer",
                "format": "int64",
                "description": "下游任务编码"
            }
        },
        "required": [
            "projectCode",
            "processDefinitionCode",
            "preTaskCode",
            "postTaskCode"
        ]
    }

    async def _run(self, projectCode, processDefinitionCode, preTaskCode, postTaskCode) -> Dict:
        """执行删除工作流任务连接线API请求
        
        Args:
            projectCode: 项目Code
            processDefinitionCode: 流程定义编码
            preTaskCode: 上游任务编码
            postTaskCode: 下游任务编码
            
        Returns:
            API响应
        """
        client = DolphinSchedulerClient()
        try:
            # 确保path参数正确处理
            projectCode = int(projectCode) if projectCode is not None else None
            processDefinitionCode = int(processDefinitionCode) if processDefinitionCode is not None else None
            preTaskCode = int(preTaskCode) if preTaskCode is not None else None
            postTaskCode = int(postTaskCode) if postTaskCode is not None else None
            
            if projectCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: projectCode"
                }
            
            if processDefinitionCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: processDefinitionCode"
                }
                
            if preTaskCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: preTaskCode"
                }
                
            if postTaskCode is None:
                return {
                    "success": False, 
                    "error": "Missing required parameter: postTaskCode"
                }
            
            # 所有参数都在URL路径中，不需要额外的query参数
            response = await client.request(
                "DELETE", 
                f"/projects/{projectCode}/process-task-relation/{processDefinitionCode}/{preTaskCode}/{postTaskCode}"
            )
            return {"success": True, "data": response}
        except ValueError:
            return {
                "success": False,
                "error": "Invalid parameter format"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            await client.close()


def register_process_task_relation_tools(mcp):
    """Register process_task_relation tools with FastMCP.
    
    Args:
        mcp: The FastMCP instance to register tools with.
    """
    from ..fastmcp_compat import register_tool_class
    
    logger.info("Registering process_task_relation tools")
    
    register_tool_class(mcp, CreateProcessTaskRelation)
    register_tool_class(mcp, QueryUpstreamRelation)
    register_tool_class(mcp, DeleteUpstreamRelation)
    register_tool_class(mcp, QueryDownstreamRelation)
    register_tool_class(mcp, DeleteDownstreamRelation)
    register_tool_class(mcp, DeleteTaskProcessRelation)
    register_tool_class(mcp, DeleteEdge)
    
    logger.info("Successfully registered 7 process_task_relation tools") 