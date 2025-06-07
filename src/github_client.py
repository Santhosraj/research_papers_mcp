from github import Github
import os
import sys

class GitHubClient:
    def __init__(self):
        self.client = Github(os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN"))

    def get_repo_files(self, repo_owner: str, repo_name: str, path: str = "papers"):
        print(f"Debug: Fetching files from {repo_owner}/{repo_name}/{path}", file=sys.stderr)
        repo = self.client.get_repo(f"{repo_owner}/{repo_name}")
        contents = repo.get_contents(path)
        files = []
        for item in contents:
            if item.type == "file" and item.name.endswith('.pdf'):
                files.append(item)
            elif item.type == "dir":
                files.extend(self.get_repo_files(repo_owner, repo_name, item.path))
        return files

    def get_file_content(self, repo_owner: str, repo_name: str, file_path: str):
        print(f"Debug: Fetching content for {file_path}", file=sys.stderr)
        repo = self.client.get_repo(f"{repo_owner}/{repo_name}")
        file = repo.get_contents(file_path)
        return file.content  # Base64-encoded content
