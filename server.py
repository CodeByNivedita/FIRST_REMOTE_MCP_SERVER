from fastmcp import FastMCP

mcp = FastMCP("My First MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}! Welcome to my MCP server."

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    