MCP Weather Wrapper Server

A custom Model Context Protocol (MCP) server built as part of the MCP Internship Program. This project bridges the gap between AI applications (such as Claude Desktop) and external data sources by wrapping weather API functions into structured tools, resources, and prompt templates.

🚀 Architecture Overview

[Host: Claude Desktop] ──(STDIO)──> [MCP Client] ──> [MCP Server (server.py)] ──> [Weather API / Cache]


Host: Claude Desktop (running the LLM model).

Client: The internal MCP client built into Claude Desktop communicating over standard I/O (STDIO).

Server: Custom Python server (server.py) exposing weather briefing tools and cached data.

🛠️ Technical Stack & Architecture

Language & Runtime: Python 3.13

Protocol & Framework: Model Context Protocol (mcp<2) utilizing FastMCP

Transport Protocol: Standard Input/Output (STDIO)

HTTP Client: httpx for asynchronous HTTP requests

Testing & Inspection: pytest and @modelcontextprotocol/inspector

📂 Core Implementation Details

The core server logic is implemented in server.py and provides the following protocol features:

🛠️ Tools

get_current_weather(city: str): Fetches real-time or mocked current weather data for a specified location.

daily_briefing(city: str): Generates a comprehensive morning weather briefing for a specified location.

📦 Resources

weather://cached/latest: Exposes a cached endpoint for the last retrieved weather result.

💬 Prompt Templates

daily_briefing_prompt(city: str): Provides structured prompt templates to guide model interactions and user context.

🛡️ Error Handling & Validation

Built-in input validation handles missing parameters or invalid locations gracefully, returning descriptive error messages rather than throwing unhandled exceptions or stack traces.

⚙️ Setup, Configuration, and Integration

1. Local Environment Setup

Clone the repository and set up a virtual environment:

# Clone the repository
git clone https://github.com/JeyAakash/mcp-weather-wrapper.git
cd mcp-weather-wrapper

# Create and activate a Python virtual environment
python -m venv venv

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install "mcp<2" httpx pytest


2. Claude Desktop Integration

Register the server in Claude Desktop by editing %APPDATA%\Claude\claude_desktop_config.json (Windows) or ~/Library/Application Support/Claude/claude_desktop_config.json (macOS):

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


🧪 Verification & Testing

Unit Testing Suite

A suite of automated unit tests (test_server.py) ensures reliability and protocol compliance. Run the tests using pytest:

pytest test_server.py


MCP Inspector Validation

To inspect the JSON-RPC stream and test tool schemas interactively in a web interface:

$env:PYTHONUNBUFFERED="1"
npx @modelcontextprotocol/inspector .\venv\Scripts\python.exe server.py


📸 Proof of Work & Demonstration

Once configured, the weather-wrapper server connects directly with Claude Desktop. The model can automatically discover, select, and execute weather tools to generate structured, context-aware briefings based on user prompts.
