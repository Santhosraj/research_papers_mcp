from setuptools import setup, find_packages

setup(
    name="research-papers-mcp",
    version="0.1.0",
    description="MCP Server for Research Papers Repository",
    packages=find_packages(),
    install_requires=[
        "mcp>=1.0.0",
        "PyMuPDF>=1.23.0",
    ],
    entry_points={
        "console_scripts": [
            "research-mcp=research_mcp_server:main",
        ],
    },
    python_requires=">=3.8",
)