# Research Papers MCP Server

An MCP server for accessing research papers in [Santhosraj/research_papers](https://github.com/Santhosraj/research_papers).

## Hosted on Smithery
- URL: https://server.smithery.ai/@Santhosraj/research-papers-mcp/sse
- Commands:
  - `/list_papers`: List all PDFs
  - `/search_papers <keyword>`: Search PDFs by keyword
  - `/read_paper <file_name>`: Read a PDF's content
- Config: Requires `GITHUB_PERSONAL_ACCESS_TOKEN`

## Local Setup
1. Clone: `git clone https://github.com/Santhosraj/research_papers_mcp`
2. Install: `uv pip install -r requirements.txt`
3. Set `GITHUB_PERSONAL_ACCESS_TOKEN` in `config/secrets.env`
4. Run: `python src/server.py`