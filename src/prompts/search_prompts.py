from mcp.server.fastmcp import FastMCP
server = FastMCP("research_papers_mcp")
@server.prompt()
def search_papers_prompt(keyword: str):
    return {
        "messages": [{"role": "user", "content": f"Search for PDF papers containing '{keyword}' in filename or content"}]
    }