from main import mcp

if __name__ == "__main__":
    # mcp.run()  # Default STDIO transport for MCP Inspector & Claude Desktop
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    # To run as HTTP server: mcp.run(transport="http", host="0.0.0.0", port=8000)
