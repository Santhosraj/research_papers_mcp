from github_client import GitHubClient


def list_papers(repo_owner: str, repo_name: str) -> dict:
    client = GitHubClient()
    files = client.get_repo_files(repo_owner, repo_name)
    return {"files": [f.name for f in files if f.name.endswith(('.pdf', '.md', '.txt'))]}