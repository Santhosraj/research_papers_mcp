from mcp.server import FastMCP
from github_client import GitHubClient
from pdf_utils import extract_pdf_text
import sys
server = FastMCP("research_papers_mcp")
@server.tool()
def read_paper(repo_owner: str = "Santhosraj", repo_name: str = "research_papers_mcp", file_name: str = "") -> dict:
    try:
        client = GitHubClient()
        file_path = f"papers/{file_name}"
        content = client.get_file_content(repo_owner, repo_name, file_path)
        text = extract_pdf_text(content)
        return {"content": text}
    except Exception as e:
        return {"error": str(e)}
