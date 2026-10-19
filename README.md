# 🌤️ Weather Wrapper MCP Server | MCP Intern Project

A custom Python-based Model Context Protocol (MCP) server built for the MCP Intern Project. This project wraps a public weather data source and exposes it as structured tools, resources, and prompt templates for AI applications like Claude Desktop.

---

## 🏗️ Architecture & Core Concepts

Following the Model Context Protocol standard, this server bridges the gap between the AI model and external data sources. The model never talks directly to your server; the host decides which tool calls run:

[ Host: Claude Desktop ]
  ├── Model
  └── MCP Client ──(JSON-RPC / STDIO)──> [ MCP Server (server.py) ] ──> [ Public Weather API / Cache ]

* Host: The AI application (Claude Desktop) that the user interacts with and runs the LLM model.
* Client: The internal client built into Claude Desktop that manages the lifecycle of the server via standard I/O (STDIO).
* Server: The Python script (server.py) you built, which exposes specific weather tools, resources, and prompt templates.

---

## 🛠️ Technical Stack & Environment

* Language & Runtime: Python 3.13
* Protocol: Model Context Protocol (mcp<2 with FastMCP)
* Transport: Standard Input/Output (STDIO)
* HTTP Client: httpx
* Environment: Windows (PowerShell, Virtual Environment located at C:\Users\s.aakash\mcp-weather-wrapper\venv)

---

## 📂 Project Structure

mcp-weather-wrapper/
├── server.py                   # Main FastMCP server implementation (Tools, Resources, Prompts)
├── test_server.py              # Unit test suite (3-5 tests)
├── requirements.txt            # Pinned Python dependencies
├── .gitignore                  # Git exclusion rules (venv, cache, logs)
└── README.md                   # Complete project documentation

---

## ⚙️ Setup & Installation Guide

Follow these steps to set up and run the server locally in under 10 minutes:

### 1. Clone the Repository & Navigate
git clone https://github.com/JeyAakash/mcp-weather-wrapper.git
cd mcp-weather-wrapper

### 2. Create and Activate a Virtual Environment
python -m venv venv
.\venv\Scripts\Activate.ps1

### 3. Install Dependencies
python -m pip install --upgrade pip
pip install "mcp<2" httpx pytest

---

## 🚀 Testing & Validation

### Validate via MCP Inspector
To verify the JSON-RPC stream and test tool schemas in a local web browser interface:
$env:PYTHONUNBUFFERED="1"
npx @modelcontextprotocol/inspector .\venv\Scripts\python.exe server.py

### Run Unit Tests
pytest test_server.py

---

## 🔌 Claude Desktop Integration

To register the server with Claude Desktop, add the configuration block to your claude_desktop_config.json (located at %APPDATA%\Claude\claude_desktop_config.json or MSIX package paths):

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

---

## 📸 Proof of Work & Demo

* Active Connection: Verified inside Claude Desktop Settings showing weather-wrapper as Running.
* Tool Invocation: Successfully triggered by prompting Claude for weather briefings, evidenced by the native Weather wrapper: Get current weather > execution badge.

---

## 🛡️ License
Developed as part of the MCP Internship Program.