def search_papers_prompt(keyword: str):
    return [{"role": "user", "content": f"Search for PDF papers containing '{keyword}' in filename or content"}]