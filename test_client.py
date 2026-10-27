import asyncio
from fastmcp import Client

async def main():
    async with Client("http://localhost:8000/mcp") as client:
        tools = await client.list_tools()
        print("Tools:", [t.name for t in tools])

        result = await client.call_tool("add", {"a": 5, "b": 7})
        print("add(5, 7) =", result.data)

        result = await client.call_tool("greet", {"name": "Nivu"})
        print("greet:", result.data)

asyncio.run(main())