from mcp import Tool
from github_client import GitHubClient
from pdf_utils import extract_pdf_text
from mcp.server.fastmcp import FastMCP
server = FastMCP("research_papers_mcp")
@server.tool()
def search_papers(repo_owner: str, repo_name: str, keyword: str) -> dict:
    try:
        client = GitHubClient()
        files = client.get_repo_files(repo_owner, repo_name, path="papers")
        matches = []
        for file in files:
            if not file.name.endswith('.pdf'):
                continue
            # Check filename
            if keyword.lower() in file.name.lower():
                matches.append({"file": file.name, "match_type": "filename"})
                continue
            # Check content
            text = extract_pdf_text(file.content)
            if keyword.lower() in text.lower():
                matches.append({"file": file.name, "match_type": "content"})
        return {"matches": matches}
    except Exception as e:
        return {"error": str(e)}