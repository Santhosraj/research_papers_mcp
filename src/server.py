from mcp.server.fastmcp import FastMCP
from tools.list_papers import list_papers
from tools.search_papers import search_papers
from tools.read_paper import read_paper
from prompts.search_prompts import search_papers_prompt
import uvicorn
import os

# Initialize FastMCP server
server = FastMCP("research_papers_mcp")

# Register tools with proper decorators
@server.tool()
def list_papers_tool(repo_owner: str, repo_name: str) -> dict:
    """List all PDF papers in the repository"""
    return list_papers(repo_owner, repo_name)

@server.tool()
def search_papers_tool(repo_owner: str, repo_name: str, query: str) -> dict:
    """Search for papers matching the query"""
    return search_papers(repo_owner, repo_name, query)

@server.tool()
def read_paper_tool(repo_owner: str, repo_name: str, paper_name: str) -> dict:
    """Read content of a specific paper"""
    return read_paper(repo_owner, repo_name, paper_name)

@server.prompt()
def search_prompt(query: str = ""):
    """Search prompt for research papers"""
    return search_papers_prompt(query)

if __name__ == "__main__":
    print("Server initialized")
    port = int(os.getenv("PORT", 8000))
    
    # For Smithery deployment, use HTTP transport
    if os.getenv("SMITHERY_DEPLOYMENT", "false").lower() == "true":
        # HTTP transport for Smithery
        server.run(transport="http", port=port, host="0.0.0.0")
    else:
        # Local development with stdio
        server.run(transport="stdio")