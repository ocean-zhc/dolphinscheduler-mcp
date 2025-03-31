"""Example MCP server using the latest FastMCP API."""

from fastmcp import FastMCP, Context

# Create an MCP server
mcp = FastMCP(title="Example MCP Server")

# Define a tool using the decorator pattern
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b

# Define an async tool
@mcp.tool()
async def fetch_data(url: str, ctx: Context) -> str:
    """Fetch data from a URL.
    
    Args:
        url: The URL to fetch data from
        ctx: The MCP context
        
    Returns:
        The fetched data
    """
    # Report progress
    ctx.info(f"Fetching data from {url}")
    
    # In a real implementation, we would fetch data here
    return f"Data from {url}"

if __name__ == "__main__":
    # Start the server
    mcp.run(host="0.0.0.0", port=8089) 