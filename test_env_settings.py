#!/usr/bin/env python
"""
测试 DolphinScheduler MCP 的环境变量配置
"""

import os
import sys
import json
from pathlib import Path

# 尝试导入 Config 类
try:
    from src.dolphinscheduler_mcp.config import Config
    HAS_CONFIG = True
except ImportError:
    HAS_CONFIG = False

def check_env_variables():
    """检查环境变量是否正确设置"""
    api_url = os.environ.get("DOLPHINSCHEDULER_API_URL")
    api_key = os.environ.get("DOLPHINSCHEDULER_API_KEY")
    
    print("环境变量检查:")
    print(f"DOLPHINSCHEDULER_API_URL: {'已设置' if api_url else '未设置'}")
    if api_url:
        print(f"  值: {api_url}")
    
    print(f"DOLPHINSCHEDULER_API_KEY: {'已设置' if api_key else '未设置'}")
    if api_key:
        print(f"  值: {api_key}")
    
    # 检查 Config 类中的值
    if HAS_CONFIG:
        config = Config()
        print("\nConfig 类中的值:")
        print(f"API URL: {config.api_url}")
        print(f"API Key: {'已设置' if config.has_api_key() else '未设置'}")

def find_mcp_settings():
    """查找 MCP 设置文件"""
    # 根据操作系统查找设置文件
    if sys.platform == "darwin":  # macOS
        base_path = Path.home() / "Library/Application Support/Cursor/User/globalStorage/rooveterinaryinc.roo-cline/settings"
    elif sys.platform == "win32":  # Windows
        base_path = Path.home() / "AppData/Roaming/Cursor/User/globalStorage/rooveterinaryinc.roo-cline/settings"
    elif sys.platform == "linux":  # Linux
        base_path = Path.home() / ".config/Cursor/User/globalStorage/rooveterinaryinc.roo-cline/settings"
    else:
        print(f"不支持的平台: {sys.platform}")
        return None
    
    settings_path = base_path / "mcp_settings.json"
    
    if settings_path.exists():
        print(f"\nMCP 设置文件: {settings_path}")
        return settings_path
    
    print(f"\nMCP 设置文件未找到: {settings_path}")
    return None

def check_mcp_settings():
    """检查 MCP 设置"""
    settings_path = find_mcp_settings()
    if not settings_path:
        return
    
    try:
        with open(settings_path, "r") as f:
            settings = json.load(f)
        
        if "mcpServers" not in settings:
            print("MCP 设置文件中没有 mcpServers 配置")
            return
        
        if "dolphinscheduler" not in settings["mcpServers"]:
            print("MCP 设置文件中没有 dolphinscheduler 配置")
            return
        
        ds_settings = settings["mcpServers"]["dolphinscheduler"]
        print("\nDolphinScheduler MCP 配置:")
        print(json.dumps(ds_settings, indent=2, ensure_ascii=False))
        
        if "env" in ds_settings:
            print("\nMCP 环境变量配置:")
            for key, value in ds_settings["env"].items():
                print(f"{key}: {value}")
    except Exception as e:
        print(f"读取 MCP 设置文件出错: {e}")

def main():
    """主函数"""
    print("DolphinScheduler MCP 环境变量测试")
    print("=" * 40)
    
    # 检查环境变量
    check_env_variables()
    
    # 检查 MCP 设置
    check_mcp_settings()
    
    # 生成示例 MCP 配置
    print("\n推荐 MCP 配置:")
    mcp_config = {
        "mcpServers": {
            "dolphinscheduler": {
                "command": "python",
                "args": ["-m", "src.dolphinscheduler_mcp"],
                "cwd": str(Path.cwd()),
                "env": {
                    "DOLPHINSCHEDULER_API_URL": "http://www.sjjc.dolphinscheduler.dsj.com/dolphinscheduler",
                    "DOLPHINSCHEDULER_API_KEY": "08f2eacbc53656ab2f6f3366e8844845"
                }
            }
        }
    }
    print(json.dumps(mcp_config, indent=2, ensure_ascii=False))
    
    # 保存推荐配置
    with open("dolphinscheduler-mcp-config.json", "w") as f:
        json.dump(mcp_config, f, indent=2, ensure_ascii=False)
    
    print(f"\n已将推荐配置保存至: {Path.cwd() / 'dolphinscheduler-mcp-config.json'}")
    print("您可以将此配置内容添加到 MCP 设置文件中")

if __name__ == "__main__":
    main() 