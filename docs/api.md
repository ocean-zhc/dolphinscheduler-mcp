# DolphinScheduler MCP Server API

This document describes the tools available in the DolphinScheduler MCP server and how to use them.

## Connection Management Tools

### Get Connection Settings

Retrieves the current connection settings for the DolphinScheduler API.

**Tool Name:** `get-connection-settings`

**Arguments:** None

**Example Request:**
```json
{
  "name": "get-connection-settings"
}
```

**Example Response:**
```json
{
  "url": "http://localhost:12345/dolphinscheduler/api",
  "has_api_key": true
}
```

### Update Connection Settings

Updates the connection settings for the DolphinScheduler API.

**Tool Name:** `update-connection-settings`

**Arguments:**
- `url` (string, optional): The new DolphinScheduler API URL
- `api_key` (string, optional): The new API key for authentication

**Example Request:**
```json
{
  "name": "update-connection-settings",
  "arguments": {
    "url": "http://new-host:12345/dolphinscheduler",
    "api_key": "new-api-key"
  }
}
```

**Example Response:**
```json
{
  "success": true,
  "url": "http://new-host:12345/dolphinscheduler",
  "has_api_key": true
}
```

## Project Management Tools

### Get Projects

Retrieves a list of all projects in DolphinScheduler.

**Tool Name:** `get-projects`

**Arguments:** None

**Example Request:**
```json
{
  "name": "get-projects"
}
```

### Get Project

Retrieves details of a specific project.

**Tool Name:** `get-project`

**Arguments:**
- `project_id` (integer): The ID of the project to retrieve

**Example Request:**
```json
{
  "name": "get-project",
  "arguments": {
    "project_id": 1
  }
}
```

## Workflow Management Tools

### Get Workflows

Retrieves workflows for a specific project.

**Tool Name:** `get-workflows`

**Arguments:**
- `project_id` (integer): The ID of the project

**Example Request:**
```json
{
  "name": "get-workflows",
  "arguments": {
    "project_id": 1
  }
}
```

### Get Workflow

Retrieves details of a specific workflow.

**Tool Name:** `get-workflow`

**Arguments:**
- `project_id` (integer): The ID of the project
- `workflow_id` (integer): The ID of the workflow

**Example Request:**
```json
{
  "name": "get-workflow",
  "arguments": {
    "project_id": 1,
    "workflow_id": 1
  }
}
```

## Workflow Instance Management Tools

### Get Workflow Instances

Retrieves workflow instances for a specific project.

**Tool Name:** `get-workflow-instances`

**Arguments:**
- `project_id` (integer): The ID of the project

**Example Request:**
```json
{
  "name": "get-workflow-instances",
  "arguments": {
    "project_id": 1
  }
}
```

### Get Workflow Instance

Retrieves details of a specific workflow instance.

**Tool Name:** `get-workflow-instance`

**Arguments:**
- `project_id` (integer): The ID of the project
- `instance_id` (integer): The ID of the workflow instance

**Example Request:**
```json
{
  "name": "get-workflow-instance",
  "arguments": {
    "project_id": 1,
    "instance_id": 1
  }
}
```

### Start Workflow

Starts a workflow execution.

**Tool Name:** `start-workflow`

**Arguments:**
- `project_id` (integer): The ID of the project
- `workflow_id` (integer): The ID of the workflow to execute
- `params` (object, optional): Workflow parameters

**Example Request:**
```json
{
  "name": "start-workflow",
  "arguments": {
    "project_id": 1,
    "workflow_id": 1,
    "params": {
      "param1": "value1",
      "param2": "value2"
    }
  }
}
```

### Stop Workflow Instance

Stops a running workflow instance.

**Tool Name:** `stop-workflow-instance`

**Arguments:**
- `project_id` (integer): The ID of the project
- `instance_id` (integer): The ID of the workflow instance to stop

**Example Request:**
```json
{
  "name": "stop-workflow-instance",
  "arguments": {
    "project_id": 1,
    "instance_id": 1
  }
}
```

## Task Instance Management Tools

### Get Task Instances

Retrieves task instances for a workflow instance.

**Tool Name:** `get-task-instances`

**Arguments:**
- `project_id` (integer): The ID of the project
- `instance_id` (integer): The ID of the workflow instance

**Example Request:**
```json
{
  "name": "get-task-instances",
  "arguments": {
    "project_id": 1,
    "instance_id": 1
  }
}
```

## System Status Tools

### Get System Status

Retrieves overall system status including master and worker nodes.

**Tool Name:** `get-system-status`

**Arguments:** None

**Example Request:**
```json
{
  "name": "get-system-status"
}
```

## Resource Management Tools

### Get Resources

Retrieves a list of resources (files and directories).

**Tool Name:** `get-resources`

**Arguments:** None

**Example Request:**
```json
{
  "name": "get-resources"
}
``` 