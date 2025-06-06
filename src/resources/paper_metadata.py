from mcp import resource
from github_client import GitHubClient
import base64
import json

@resource()
def paper_metadata(repo_owner: str, repo_name: str) -> dict:
    try:
        client = GitHubClient()
        repo = client.client.get_repo(f"{repo_owner}/{repo_name}")
        metadata_file = repo.get_contents("metadata.json")
        metadata = json.loads(base64.b64decode(metadata_file.content).decode('utf-8'))
        return metadata
    except Exception as e:
        return {"error": str(e)}