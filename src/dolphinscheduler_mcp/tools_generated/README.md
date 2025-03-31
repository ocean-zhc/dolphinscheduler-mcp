# DolphinScheduler MCP 工具开发指南

本文档提供了在 DolphinScheduler MCP 项目中创建新工具的指南。

## 工具开发规范

### 1. 工具命名规范

- 类名应该使用 CamelCase 命名法，例如 `GetResources`, `CreateProject`
- 方法名应该使用 snake_case 命名法，例如 `get_project`, `create_resource`
- 参数名应该使用 snake_case 命名法，例如 `project_code`, `resource_id`
- 不要在类名和方法名中使用连字符（-），应使用下划线（_）替代

### 2. 路径参数处理

对于包含路径参数的 API，需要正确处理参数类型转换和验证：

```python
# 确保路径参数正确处理
resource_id = int(id) if id is not None else None
if resource_id is None:
    return {
        "success": False, 
        "error": "Missing required parameter: id"
    }
    
response = await client.request(
    "GET", 
    f"/resources/{resource_id}"
)
```

### 3. 错误处理

每个工具方法都应该包含适当的错误处理：

```python
try:
    # API请求代码
    return {"success": True, "data": response}
except ValueError:
    return {
        "success": False,
        "error": f"Invalid parameter format"
    }
except Exception as e:
    return {
        "success": False,
        "error": str(e)
    }
finally:
    await client.close()  # 确保关闭客户端连接
```

### 4. 认证处理

所有 API 请求都必须包含 Token 认证。这已经在 `DolphinSchedulerClient` 类中处理，确保使用此客户端发送请求。

Token 值会从环境变量 `DOLPHINSCHEDULER_API_KEY` 获取。

## 开发新工具的步骤

1. 复制 `template_tool.py` 文件作为起点
2. 根据 OpenAPI 规范定义工具类
3. 实现 `_run` 方法，处理参数和 API 请求
4. 在 `__init__.py` 文件中导入和注册新工具

## 常见问题

### 问题：路径参数处理错误

**错误示例**：
```python
# 错误：直接使用参数而不进行验证
response = await client.request("GET", f"/resources/{id}")
```

**正确示例**：
```python
# 正确：验证并转换参数
resource_id = int(id) if id is not None else None
if resource_id is None:
    return {"success": False, "error": "Missing required parameter: id"}
response = await client.request("GET", f"/resources/{resource_id}")
```

### 问题：缺少错误处理

**错误示例**：
```python
# 错误：没有错误处理
response = await client.request("GET", "/resources")
return {"success": True, "data": response}
```

**正确示例**：
```python
# 正确：包含错误处理
try:
    response = await client.request("GET", "/resources")
    return {"success": True, "data": response}
except Exception as e:
    return {"success": False, "error": str(e)}
```

### 问题：忘记关闭客户端连接

**错误示例**：
```python
# 错误：没有关闭客户端连接
client = DolphinSchedulerClient()
response = await client.request("GET", "/resources")
return {"success": True, "data": response}
```

**正确示例**：
```python
# 正确：使用 finally 块关闭连接
client = DolphinSchedulerClient()
try:
    response = await client.request("GET", "/resources")
    return {"success": True, "data": response}
finally:
    await client.close()
```

## 参考资源

- [OpenAPI 规范文档](https://swagger.io/specification/)
- [DolphinScheduler API 文档](https://dolphinscheduler.apache.org/en-us/docs/latest/user_doc/api/overview.html)
- [Python Asyncio 文档](https://docs.python.org/3/library/asyncio.html) 