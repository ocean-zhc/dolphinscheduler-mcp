"""Tests for the config module."""

import os
import unittest
from unittest.mock import patch

from src.dolphinscheduler_mcp.config import Config


class TestConfig(unittest.TestCase):
    """Test cases for the Config class."""

    def setUp(self):
        """Set up test cases."""
        # Reset the Config singleton instance before each test
        Config._instance = None
        # Clear environment variables that might affect the test
        if "DOLPHINSCHEDULER_API_URL" in os.environ:
            del os.environ["DOLPHINSCHEDULER_API_URL"]
        if "DOLPHINSCHEDULER_API_KEY" in os.environ:
            del os.environ["DOLPHINSCHEDULER_API_KEY"]

    def test_default_values(self):
        """Test default configuration values."""
        config = Config()
        self.assertEqual(config.api_url, "http://localhost:12345/dolphinscheduler")
        self.assertIsNone(config.api_key)
        self.assertFalse(config.has_api_key())

    @patch.dict(os.environ, {"DOLPHINSCHEDULER_API_URL": "http://test-server:8080"})
    def test_env_api_url(self):
        """Test API URL from environment variable."""
        config = Config()
        self.assertEqual(config.api_url, "http://test-server:8080")

    @patch.dict(os.environ, {"DOLPHINSCHEDULER_API_KEY": "test-api-key"})
    def test_env_api_key(self):
        """Test API key from environment variable."""
        config = Config()
        self.assertEqual(config.api_key, "test-api-key")
        self.assertTrue(config.has_api_key())

    def test_singleton(self):
        """Test that Config is a singleton."""
        config1 = Config()
        config2 = Config()
        self.assertIs(config1, config2)

    def test_update_values(self):
        """Test updating configuration values."""
        config = Config()
        config.api_url = "http://new-server:9000"
        config.api_key = "new-api-key"
        
        # Get a new instance and verify values are preserved (singleton)
        new_config = Config()
        self.assertEqual(new_config.api_url, "http://new-server:9000")
        self.assertEqual(new_config.api_key, "new-api-key")
        self.assertTrue(new_config.has_api_key())


if __name__ == "__main__":
    unittest.main() 