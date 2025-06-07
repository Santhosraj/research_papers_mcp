import os
from github import Github

class GitHubClient:
    def __init__(self):
        self._client = None
    
    @property
    def client(self):
        """Lazy load GitHub client"""
        if self._client is None:
            token = os.environ.get('GITHUB_PERSONAL_ACCESS_TOKEN')
            if not token:
                raise ValueError("GitHub Personal Access Token not provided")
            self._client = Github(token)
        return self._client
    
    def get_repo_files(self, repo_owner: str, repo_name: str, path: str = ""):
        """Get files from repository"""
        repo = self.client.get_repo(f"{repo_owner}/{repo_name}")
        contents = repo.get_contents(path)
        return contents