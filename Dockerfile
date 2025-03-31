FROM python:3.9-slim

WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -e .

# Expose MCP server port
EXPOSE 8089

# Run server
CMD ["python", "-m", "src.dolphinscheduler_mcp"] 