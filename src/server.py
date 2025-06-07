import mcp
from mcp.server import FastMCP
from tools.list_papers import list_papers
from tools.search_papers import search_papers
from tools.read_paper import read_paper
from prompts.search_prompts import search_papers_prompt

server = FastMCP("research_papers_mcp")
server.add_tool(list_papers)
server.add_tool(search_papers)
server.add_tool(read_paper)
@server.prompt(name="search_papers_prompt")
def search_prompt(keyword: str = ""):
    """Search prompt for research papers"""
    return search_papers_prompt(keyword)
if __name__ == "__main__":
    print("server initialized")
    server.run(transport="stdio")
