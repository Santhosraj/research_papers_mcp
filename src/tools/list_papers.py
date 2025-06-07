from mcp.server.fastmcp import FastMCP
import mcp
from mcp.server import Server
from github_client import GitHubClient

def list_papers(repo_owner: str, repo_name: str) -> dict:
    try:
        client = GitHubClient()
        files = client.get_repo_files(repo_owner, repo_name, path="papers")
        pdf_files = [f.name for f in files if f.name.endswith('.pdf')]
        return {"files": pdf_files}
    except Exception as e:
        return {"error": str(e)}