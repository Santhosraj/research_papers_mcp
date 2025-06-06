from mcp import Tool
from github_client import GitHubClient
from mcp.server.fastmcp import FastMCP
from pdf_utils import extract_pdf_text
server = FastMCP("research_papers_mcp")
@server.tool()
def read_paper(repo_owner: str, repo_name: str, file_name: str) -> dict:
    try:
        client = GitHubClient()
        file_path = f"papers/{file_name}"
        content = client.get_file_content(repo_owner, repo_name, file_path)
        text = extract_pdf_text(content)
        return {"content": text}
    except Exception as e:
        return {"error": str(e)}