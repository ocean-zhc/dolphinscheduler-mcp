"""DolphinScheduler API Client for MCP tools."""

import os
import json
import logging
from typing import Dict, Any, Optional, Union, List, Tuple, BinaryIO

import aiohttp
from aiohttp import FormData

from .config import Config


class DolphinSchedulerClient:
    """Client for interacting with DolphinScheduler REST API."""

    def __init__(self, api_url: Optional[str] = None, api_key: Optional[str] = None):
        """Initialize the client.
        
        Args:
            api_url: API URL for DolphinScheduler
            api_key: API key for authentication
        """
        self.config = Config()
        if api_url:
            self.config.api_url = api_url
        if api_key:
            self.config.api_key = api_key
        
        self.session: Optional[aiohttp.ClientSession] = None
        self.logger = logging.getLogger("dolphinscheduler_mcp.client")

    async def _ensure_session(self) -> aiohttp.ClientSession:
        """Ensure that a session exists.
        
        Returns:
            An aiohttp ClientSession.
        """
        if self.session is None:
            self.session = aiohttp.ClientSession()
        return self.session

    async def close(self) -> None:
        """Close the session."""
        if self.session:
            await self.session.close()
            self.session = None

    async def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make a request to the DolphinScheduler API.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            path: API path
            params: Query parameters
            json_data: JSON data for the request body
            
        Returns:
            Response from the API
        """
        session = await self._ensure_session()
        
        # Build the full URL
        url = f"{self.config.api_url.rstrip('/')}/{path.lstrip('/')}"
        
        # Build headers
        headers = {}
        if self.config.has_api_key():
            headers["Token"] = self.config.api_key
        
        # Make the request
        async with session.request(method, url, params=params, json=json_data, headers=headers) as response:
            # Raise an exception for 4XX/5XX responses
            response.raise_for_status()
            
            # Parse the response
            return await response.json()

    async def request_with_files(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        files: Optional[Dict[str, Tuple[str, Union[str, bytes]]]] = None,
    ) -> Dict[str, Any]:
        """
        Send a multipart request with files to the DolphinScheduler API.
        
        Args:
            method: HTTP method (typically POST)
            endpoint: API endpoint
            params: Form parameters
            headers: Request headers
            files: Dictionary of files to upload {field_name: (filename, content)}
            
        Returns:
            Response JSON
        """
        await self._ensure_session()
        
        url = f"{self.config.api_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        if not headers:
            headers = {}
        
        # Add token if available
        if self.config.has_api_key():
            headers["Token"] = self.config.api_key
        
        try:
            # Create form data
            form = FormData()
            
            # Add files to form data
            if files:
                for field_name, (filename, content) in files.items():
                    form.add_field(field_name, content, filename=filename)
            
            # Add other parameters to form data
            if params:
                for key, value in params.items():
                    if isinstance(value, (dict, list)):
                        form.add_field(key, json.dumps(value))
                    else:
                        form.add_field(key, str(value))
            
            self.logger.debug(f"Sending multipart {method} request to {url}")
            
            async with self.session.request(
                method=method,
                url=url,
                headers=headers,
                data=form
            ) as response:
                result = await response.json()
                
                if response.status >= 400:
                    self.logger.error(f"API error: {response.status} - {result}")
                    return {
                        "success": False,
                        "error": f"API error: {response.status}",
                        "data": result
                    }
                
                return result
        except Exception as e:
            self.logger.exception(f"Error in API request to {url}: {str(e)}")
            return {
                "success": False,
                "error": f"Request error: {str(e)}"
            }

    async def request_raw(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> bytes:
        """
        Send a request to the DolphinScheduler API and return raw bytes response.
        Useful for downloading files.
        
        Args:
            method: HTTP method (typically GET)
            endpoint: API endpoint
            params: URL parameters
            headers: Request headers
            
        Returns:
            Raw response bytes
        """
        await self._ensure_session()
        
        url = f"{self.config.api_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        if not headers:
            headers = {}
        
        # Add token if available
        if self.config.has_api_key():
            headers["Token"] = self.config.api_key
        
        try:
            self.logger.debug(f"Sending {method} request to {url} for raw response")
            
            async with self.session.request(
                method=method,
                url=url,
                params=params,
                headers=headers
            ) as response:
                if response.status >= 400:
                    error_text = await response.text()
                    self.logger.error(f"API error: {response.status} - {error_text}")
                    raise Exception(f"API error: {response.status} - {error_text}")
                
                return await response.read()
        except Exception as e:
            self.logger.exception(f"Error in API request to {url}: {str(e)}")
            raise

    # Project management methods
    
    async def get_projects(self, search_val: Optional[str] = None) -> Dict[str, Any]:
        """Get a list of projects.
        
        Args:
            search_val: Optional search value to filter projects by name
            
        Returns:
            Response from the API
        """
        params = {}
        if search_val:
            params["searchVal"] = search_val
        
        return await self.request("GET", "projects", params=params)
    
    async def get_project(self, project_code: int) -> Dict[str, Any]:
        """Get project details.
        
        Args:
            project_code: Project code
            
        Returns:
            Response from the API
        """
        return await self.request("GET", f"projects/{project_code}")
    
    async def create_project(self, name: str, description: str = "") -> Dict[str, Any]:
        """Create a new project.
        
        Args:
            name: Project name
            description: Project description
            
        Returns:
            Response from the API
        """
        data = {
            "projectName": name
        }
        if description:
            data["description"] = description
        
        return await self.request("POST", "projects", json_data=data)
    
    async def update_project(self, project_code: int, name: str, description: str = "") -> Dict[str, Any]:
        """Update a project.
        
        Args:
            project_code: Project code
            name: Project name
            description: Project description
            
        Returns:
            Response from the API
        """
        params = {
            "projectName": name
        }
        if description:
            params["description"] = description
        
        return await self.request("PUT", f"projects/{project_code}", params=params)
    
    async def delete_project(self, project_code: int) -> Dict[str, Any]:
        """Delete a project.
        
        Args:
            project_code: Project code
            
        Returns:
            Response from the API
        """
        return await self.request("DELETE", f"projects/{project_code}") 