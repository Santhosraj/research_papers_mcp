from mcp.server.fastmcp import FastMCP
from github_client import GitHubClient
from pdf_utils import extract_pdf_text


def search_papers(input_data: dict) -> dict:
    try:
        repo_owner = input_data.get('repo_owner')
        repo_name = input_data.get('repo_name')
        keyword = input_data.get('keyword')
        
        # Validate required parameters
        if not repo_owner:
            return {"error": "repo_owner is required"}
        if not repo_name:
            return {"error": "repo_name is required"}
        if not keyword:
            return {"error": "keyword is required"}
        
        client = GitHubClient()
        files = client.get_repo_files(repo_owner, repo_name, path="papers")
        matches = []
        for file in files:
            if not file.name.endswith('.pdf'):
                continue
            # Check if keyword is in filename
            if keyword.lower() in file.name.lower():
                matches.append({"file": file.name, "match_type": "filename"})
                continue
            # Check if keyword is in PDF content
            # Note: Assumes file.content is base64-encoded
            text = extract_pdf_text(file.content)
            if keyword.lower() in text.lower():
                matches.append({"file": file.name, "match_type": "content"})
        return {"matches": matches}
    except Exception as e:
        return {"error": str(e)}