from mcp.server.fastmcp import FastMCP
from tools.list_papers import list_papers
from tools.search_papers import search_papers
from tools.read_paper import read_paper
from prompts.search_prompts import search_papers_prompt
import uvicorn
import os

server = FastMCP("research_papers_mcp")
server.add_tool(list_papers)
server.add_tool(search_papers)
server.add_tool(read_paper)
server.add_prompt(search_papers_prompt)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(server.sse_app(), host="0.0.0.0", port=port)