from github import Github

import os

class GitHubClient:
    def __init__(self):
        self.client = Github(os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN"))

    def get_repo_files(self, repo_owner: str, repo_name: str, path: str = "papers"):
        repo = self.client.get_repo(f"{repo_owner}/{repo_name}")
        return repo.get_contents(path)

    def get_file_content(self, repo_owner: str, repo_name: str, file_path: str):
        repo = self.client.get_repo(f"{repo_owner}/{repo_name}")
        file = repo.get_contents(file_path)
        return file.content  # Returns base64-encoded content