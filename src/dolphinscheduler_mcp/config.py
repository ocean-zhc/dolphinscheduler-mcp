"""Configuration for DolphinScheduler MCP."""

import os
import json
from pathlib import Path
from typing import Optional, Dict, Any

def read_mcp_settings() -> Dict[str, Any]:
    """Read MCP settings from the Cursor MCP settings file.
    
    Returns:
        A dictionary containing the MCP settings
    """
    # Default location for the Cursor MCP settings file
    settings_path = os.path.expanduser("~/Library/Application Support/Cursor/User/globalStorage/rooveterinaryinc.roo-cline/settings/mcp_settings.json")
    
    if os.path.exists(settings_path):
        try:
            with open(settings_path, 'r') as f:
                settings = json.load(f)
                return settings
        except Exception as e:
            print(f"Error reading MCP settings file: {e}")
    
    return {}

def get_env_from_mcp_settings() -> Dict[str, str]:
    """Get environment variables from MCP settings.
    
    Returns:
        A dictionary containing environment variables
    """
    settings = read_mcp_settings()
    env_vars = {}
    
    print("Reading MCP settings:", settings.keys() if settings else "No settings found")
    
    # Look for the dolphinscheduler server config
    if 'mcpServers' in settings and 'dolphinscheduler' in settings['mcpServers']:
        server_config = settings['mcpServers']['dolphinscheduler']
        print("Found dolphinscheduler server config:", server_config.keys())
        if 'env' in server_config:
            env_vars = server_config['env']
            print("Found environment variables in MCP settings:", env_vars)
    
    return env_vars

class Config:
    """Configuration for DolphinScheduler MCP."""
    
    _instance = None
    
    def __new__(cls):
        """Create a new instance of Config or return the existing one."""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            
            # First, try to get env variables from MCP settings
            mcp_env = get_env_from_mcp_settings()
            
            # Get API URL from MCP settings, env var, or use default
            cls._instance._api_url = mcp_env.get(
                "DOLPHINSCHEDULER_API_URL", 
                os.environ.get(
                    "DOLPHINSCHEDULER_API_URL", 
                    "http://localhost:12345/dolphinscheduler"
                )
            )
            
            # Get API key from MCP settings, env var, or use default
            cls._instance._api_key = mcp_env.get(
                "DOLPHINSCHEDULER_API_KEY",
                os.environ.get("DOLPHINSCHEDULER_API_KEY", "")
            )
            
            # Set the environment variables for other parts of the app
            if cls._instance._api_url:
                os.environ["DOLPHINSCHEDULER_API_URL"] = cls._instance._api_url
            if cls._instance._api_key:
                os.environ["DOLPHINSCHEDULER_API_KEY"] = cls._instance._api_key
        
        return cls._instance
    
    @property
    def api_url(self) -> str:
        """Get the API URL.
        
        Returns:
            The API URL.
        """
        return self._api_url
    
    @api_url.setter
    def api_url(self, value: str) -> None:
        """Set the API URL.
        
        Args:
            value: The API URL.
        """
        self._api_url = value
        # We could also update the environment variable here
        os.environ["DOLPHINSCHEDULER_API_URL"] = value
    
    @property
    def api_key(self) -> str:
        """Get the API key.
        
        Returns:
            The API key.
        """
        return self._api_key
    
    @api_key.setter
    def api_key(self, value: str) -> None:
        """Set the API key.
        
        Args:
            value: The API key.
        """
        self._api_key = value
        # We could also update the environment variable here
        os.environ["DOLPHINSCHEDULER_API_KEY"] = value
    
    def has_api_key(self) -> bool:
        """Check if an API key is set.
        
        Returns:
            True if an API key is set, False otherwise.
        """
        return bool(self._api_key) 