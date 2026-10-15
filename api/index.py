from fastmcp import FastMCP
from server import mcp

app = mcp.http_app(path="/")
