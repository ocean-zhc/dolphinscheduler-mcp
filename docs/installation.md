# Installation Guide

This guide provides detailed instructions for installing and setting up the DolphinScheduler MCP server.

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- A running DolphinScheduler instance
- (Optional) Docker and Docker Compose for containerized deployment

## Standard Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dolphinscheduler-mcp.git
   cd dolphinscheduler-mcp
   ```

2. Create and activate a virtual environment:
   ```bash
   # Linux/macOS
   python -m venv .venv
   source .venv/bin/activate
   
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

4. Configure environment variables by creating a `.env` file in the project root:
   ```
   DOLPHINSCHEDULER_API_URL=http://your-dolphinscheduler-server:12345/dolphinscheduler/api
   DOLPHINSCHEDULER_API_KEY=your_api_key
   ```

## Docker Installation

1. Build and run using Docker Compose:
   ```bash
   docker-compose up -d
   ```

   This will:
   - Build the Docker image
   - Start the DolphinScheduler MCP server on port 8089
   - Configure it to connect to your DolphinScheduler API

2. Check the logs:
   ```bash
   docker-compose logs -f
   ```

3. Stop the service:
   ```bash
   docker-compose down
   ```

## Using the Scripts

For convenience, we provide scripts to set up and run the server:

- Linux/macOS:
  ```bash
  chmod +x run.sh
  ./run.sh
  ```

- Windows:
  ```cmd
  run.bat
  ```

These scripts will:
1. Create a virtual environment if it doesn't exist
2. Activate the virtual environment
3. Install the package dependencies
4. Run the MCP server

## Verifying the Installation

To verify that the MCP server is running correctly:

1. Open a web browser and navigate to: `http://localhost:8089/mcp/tools`
2. You should see a JSON response listing all available tools.

Alternatively, use the MCP Inspector to test your server:

```bash
npx @modelcontextprotocol/inspector python -m src.dolphinscheduler_mcp
``` 