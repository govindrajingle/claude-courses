from mcp.server.fastmcp import FastMCP

from src.tools.health import execute as health_execute
from src.tools.deepseek_chat import execute as chat_execuse

mcp = FastMCP("DeepSeek MCP Server")


@mcp.tool()
async def health():
    return await health_execute()


@mcp.tool()
async def deepseek_chat(prompt: str):
    return await chat_execuse(prompt)


if __name__ == "__main__":
    mcp.run()
