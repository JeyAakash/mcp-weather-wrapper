# Weather Wrapper MCP Server Integration

## Project Overview
Integrated a custom Python-based `weather-wrapper` Model Context Protocol (MCP) server into the Claude Desktop application on Windows.

## Technical Stack
- **Language & Runtime:** Python 3.13
- **Protocol:** Model Context Protocol (MCP v1.x / FastMCP)
- **Transport:** Standard Input/Output (STDIO)
- **Key Dependencies:** `mcp<2`, `httpx`, `pydantic`

## Architecture & Configuration
The server communicates via JSON-RPC over STDIO. The application configuration was deployed to `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "weather-wrapper": {
      "command": "C:\\Users\\s.aakash\\mcp-weather-wrapper\\venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\s.aakash\\mcp-weather-wrapper\\server.py"
      ],
      "env": {
        "PYTHONUNBUFFERED": "1",
        "MCP_SERVER_REQUEST_TIMEOUT": "120000"
      }
    }
  }
}