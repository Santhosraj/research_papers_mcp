from mcp.server.fastmcp import FastMCP
from tools.list_papers import list_papers
from tools.search_papers import search_papers
from tools.read_paper import read_paper
from prompts.search_prompts import search_papers_prompt
import os

# Initialize FastMCP server
server = FastMCP("research_papers_mcp")

# Add tools
server.add_tool(list_papers)
server.add_tool(search_papers)
server.add_tool(read_paper)
server.add_tool(search_papers_prompt)

# For Smithery deployment - always use HTTP
if __name__ == "__main__":
    print("Smithery deployment server starting...")
    port = int(os.getenv("PORT", 8000))
    server.run(transport="http", port=port, host="0.0.0.0")