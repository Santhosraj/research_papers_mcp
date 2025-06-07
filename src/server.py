from mcp.server.fastmcp import FastMCP
from tools.list_papers import list_papers
from tools.search_papers import search_papers
from tools.read_paper import read_paper
from prompts.search_prompts import search_papers_prompt
import os

# Initialize FastMCP server
server = FastMCP("research_papers_mcp")

# Register tools directly - FastMCP will auto-discover the function signatures
server.add_tool(list_papers)
server.add_tool(search_papers)
server.add_tool(read_paper)

# Add prompts
server.add_prompt(search_papers_prompt)

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