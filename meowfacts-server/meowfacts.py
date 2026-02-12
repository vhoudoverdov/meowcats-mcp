from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("meowfacts")

MEOWFACTS_API_URL = "https://meowfacts.herokuapp.com/"

@mcp.tool()
async def get_cat_fact() -> str:
    """Get a random cat fact."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(MEOWFACTS_API_URL, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            if "data" in data and isinstance(data["data"], list) and len(data["data"]) > 0:
                return data["data"][0]
            return "Could not find a cat fact in the response."
        except Exception as e:
            return f"Error fetching cat fact: {str(e)}"

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
