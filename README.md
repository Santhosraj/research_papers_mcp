# Research Papers MCP Server

## 📚 Overview

The `research_papers_mcp` project is an MCP (Message Control Protocol) server that provides tools to interact with research papers stored in a GitHub repository ([Santhosraj/research_papers](https://github.com/Santhosraj/research_papers)). It allows users to list, search, and read PDF papers using an MCP client like Claude Desktop. The server is built using the FastMCP framework and runs locally with stdio transport.

## ✨ Features

- **List Papers**: Retrieve a list of PDF files in the `papers/` folder of the repository.
- **Search Papers**: Search for papers by keyword in filenames or content.
- **Read Papers**: Extract and read the content of a specific PDF file.
- **Prompt Support**: Includes a prompt (`search_papers_prompt`) to initiate searches.

## 📁 Project Structure


**research_papers_mcp/
├── src/
│   └── server.py           # Main server script
├── tools/
│   ├── list_papers.py     # Tool to list PDF files
│   ├── search_papers.py   # Tool to search papers by keyword
│   └── read_paper.py      # Tool to read a specific PDF
├── prompts/
│   └── search_prompts.py  # Prompt definition for searching papers
├── config/
│   └── config.json        # Claude Desktop configuration
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # License file (add your preferred license)
└── .gitignore             # Git ignore file**


## ✅ Prerequisites

- **Python 3.11**: Make sure Python 3.11 is installed.
- **GitHub Personal Access Token (PAT)**: Required to access private repos. [Generate one](https://github.com/settings/tokens) with `repo` scope.
- **Claude Desktop**: An MCP client to interact with this server. [Install here](https://claude.ai/).

## ⚙️ Setup Instructions


```
Setup Instructions

## 1. Clone the Repository

Clone the project to your local machine:
```bash
git clone https://github.com/Santhosraj/research_papers_mcp.git
cd research_papers_mcp
```
## 3. Set Up a Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On Unix/Linux/Mac
```
## 3. Install Dependencies
Install the required Python packages:
```bash
uv pip install -r requirements.txt
```
The requirements.txt includes dependencies like mcp, PyGitHub, PyPDF2, uvicorn, and fastapi.

## 4. Configure Claude Desktop
Create a config.json file in the project root to configure Claude Desktop for local use:
```bash
{
  "mcpServers": {
    "research-papers": {
      "url": "stdio://local",
      "command": "D:\\2025\\Study\\June\\mcp\\research_papers_mcp\\.venv\\Scripts\\python.exe",
      "args": [
        "D:\\2025\\Study\\June\\mcp\\research_papers_mcp\\src\\server.py"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_github_pat_here"
      }
    }
  }
}
```


***Replace "your_github_pat_here" with your GitHub PAT.***
***Adjust the command and args paths if your project directory differs.***

## 5. Run the Server
Start the MCP server locally:
```bash
python src/server.py
```
## You should see:
```bash Server initialized```

## 6. Interact with the Server Using Claude Desktop
```bash
Launch Claude Desktop:claude-desktop --config research_papers_mcp\config.json
```

## List Tools and Prompts:/list-tools

## Expected Output:Available tools:
**- list_papers**
**- search_papers**
**- read_paper**
## Available prompts:
**- search_papers_prompt**


**Search for Papers:/search_papers {"keyword": "cnn"}**
```bash
Expected Output (example):{
  "matches": [
    {"file": "papers/some_paper_with_cnn.pdf", "match_type": "filename"},
    {"file": "papers/another_paper.pdf", "match_type": "content"}
  ]
}

```

## Usage Examples

**List All Papers:/list_papers**


**Search for Papers with Keyword "transformer":/search_papers {"keyword": "transformer"}**


**Read a Specific Paper:/read_paper {"paper_name": "some_paper.pdf"}**



## Troubleshooting

**Server Fails to Start:**
**1)Ensure all dependencies are installed: uv pip install -r requirements.txt.**
**2)Verify your GitHub PAT has the repo scope.**


## Tool Errors:
**Check the server logs for GitHub API errors (e.g., rate limits, invalid PAT).**
**Ensure the papers folder exists in Santhosraj/research_papers.**


## Claude Desktop Not Connecting:
**Confirm the server is running before starting Claude Desktop.**
**Verify the config.json paths and url are correct.**



### Contributing 🚀
Feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss your ideas.
## License
This project is licensed under the MIT License. See the LICENSE file for details.
## Contact
For questions or support, reach out to Santhosraj at **[santhosraj14@gmail.com]**.
