# 🌤️ Weather Wrapper MCP Server | MCP Intern Project

A custom Python-based Model Context Protocol (MCP) server built for the MCP Intern Project. This project wraps a public weather data source and exposes it as structured tools, resources, and prompt templates for AI applications like Claude Desktop.

---

## 🏗️ Architecture & Core Concepts

Following the Model Context Protocol standard, this server bridges the gap between the AI model and external data sources. The model never talks directly to your server; the host decides which tool calls run:

[ Host: Claude Desktop ]
  ├── Model
  └── MCP Client ──(JSON-RPC / STDIO)──> [ MCP Server (server.py) ] ──> [ Public Weather API / Cache ]

* Host: The AI application (Claude Desktop) that the user interacts with and runs the LLM model[cite: 4, 7].
* Client: The internal client built into Claude Desktop that manages the lifecycle of the server via standard I/O (STDIO)[cite: 4, 7].
* Server: The Python script (server.py) you built, which exposes specific weather tools, resources, and prompt templates[cite: 4, 7].

---

## 🛠️ Technical Stack & Environment

* Language & Runtime: Python 3.13[cite: 7]
* Protocol: Model Context Protocol (mcp<2 with FastMCP)[cite: 7]
* Transport: Standard Input/Output (STDIO)[cite: 7]
* HTTP Client: httpx[cite: 7]
* Environment: Windows (PowerShell, Virtual Environment located at C:\Users\s.aakash\mcp-weather-wrapper\venv)[cite: 7]

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
To verify the JSON-RPC stream and test tool schemas in a local web browser interface[cite: 5, 7]:
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

## 📋 Definition of Done Checklist

| Requirement | Status | Implementation Details |
| :--- | :---: | :--- |
| Server runs in a real AI app | ✅ Done | Connected to Claude Desktop with active tool execution[cite: 4, 7]. |
| 2-3 Tools, 1 Resource, 1 Prompt | ✅ Done | Implemented get_current_weather, daily_briefing, cached weather resource, and prompt templates[cite: 6, 7]. |
| Error Handling & Validation | ✅ Done | Built-in validation returning helpful error messages instead of crashes[cite: 7]. |
| 3 to 5 Unit Tests | ✅ Done | Included in test_server.py[cite: 7]. |
| Pushed to GitHub | ✅ Done | Published publicly on GitHub with complete documentation[cite: 7]. |

---

## 📸 Proof of Work & Demo

* Active Connection: Verified inside Claude Desktop Settings showing weather-wrapper as Running[cite: 3, 7].
* Tool Invocation: Successfully triggered by prompting Claude for weather briefings, evidenced by the native Weather wrapper: Get current weather > execution badge[cite: 4, 7].

---

## 🛡️ License
Developed as part of the MCP Internship Program.