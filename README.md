# Expense Tracker MCP Server

A Model Context Protocol (MCP) server built with **FastMCP** (v3.x) and **Python**, designed to provide tools and resources for expense tracking to MCP-compliant clients like Claude Desktop and the MCP Inspector.

---

## 📋 Prerequisites

- **Python**: 3.10+ (tested with Python 3.14)
- **uv**: Fast Python package installer and resolver ([astral.sh/uv](https://astral.sh/uv))
- **Node.js**: `v22.x` or `v24.x` (LTS) — *Required for MCP Inspector UI*
- **Claude Desktop** *(optional)*: For testing tools directly within Claude

---

## 🚀 Setup & Installation

### 1. Initialize Project & Environment

```powershell
# Initialize uv project (if starting fresh)
uv init .

# Install FastMCP
uv add fastmcp
```

### 2. Prepare Node.js for MCP Inspector UI

The MCP Inspector (`@modelcontextprotocol/inspector`) requires Node.js `v22.19.0+` or `v24+`. If using `nvm-windows`:

```powershell
nvm install lts
nvm use 24
```

Install the inspector globally or allow `npx` to fetch it:

```powershell
npm install -g @modelcontextprotocol/inspector
```

---

## 🛠️ Running & Development

### Option A: Interactive Web UI (MCP Inspector)

To launch the MCP Inspector web UI with **hot reloading**:

```powershell
uv run fastmcp dev inspector main.py
```

- Keep this terminal window open.
- The console will output a local URL with an authentication token:
  ```text
  MCP Inspector Web is up and running at:
     http://127.0.0.1:6274?MCP_INSPECTOR_API_TOKEN=<token>
  ```
- Open that link in your browser to test tools, inspect schemas, and view real-time request/response logs.

### Option B: Run Server Directly (STDIO)

To run the MCP server in standard I/O mode:

```powershell
uv run fastmcp run main.py
```
*(or `uv run python main.py`)*

---

## 🤖 Connecting to Claude Desktop

### 1. Configuration File Location

On Windows, Claude Desktop's configuration is stored at:
```text
%APPDATA%\Claude\claude_desktop_config.json
```
*(Full path: `C:\Users\<YourUsername>\AppData\Roaming\Claude\claude_desktop_config.json`)*

### 2. Configuration Settings

Add the `expense-server` definition under `mcpServers`.

> **Note**: On Windows, GUI applications like Claude Desktop often do not inherit the shell `PATH`. Always specify the absolute path to `uv.exe`.

```json
{
  "mcpServers": {
    "expense-server": {
      "command": "C:\\Users\\hp\\AppData\\Local\\Python\\pythoncore-3.14-64\\Scripts\\uv.exe",
      "args": [
        "run",
        "--directory",
        "g:\\Projects\\expense-tracker-mcp-server",
        "fastmcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

### 3. Restart Claude Desktop
1. Completely close Claude Desktop (ensure it is quit from the Windows system tray near the clock).
2. Reopen Claude Desktop.
3. Check **Settings > Developer** to verify `expense-server` is connected.

---

## 🧰 Available Tools (Current `main.py`)

| Tool | Parameters | Description |
| :--- | :--- | :--- |
| `roll_dice` | `n_dice: int = 1` | Rolls `n_dice` 6-sided dice and returns results list. |
| `add_numbers` | `a: float, b: float` | Adds two numbers together and returns the sum. |

---

## 🔧 Troubleshooting

### 1. `Unknown command "main.py". Available commands: inspector, apps.`
In FastMCP 3.x, `fastmcp dev` is a command group. Use `fastmcp dev inspector main.py` instead of `fastmcp dev main.py`.

### 2. `node:util does not provide an export named 'styleText'`
Node.js is older than v20.12. Update to Node v22+ or v24+ via `nvm install lts && nvm use 24`.

### 3. `Cannot find native binding (npm optional dependencies bug)`
Corrupted npx cache from switching Node versions. Run:
```powershell
npm cache clean --force
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\npm-cache\_npx" -ErrorAction SilentlyContinue
npm install -g @modelcontextprotocol/inspector
```
