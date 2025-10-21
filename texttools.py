from mcp.server.fastmcp import FastMCP
mcp = FastMCP("TextTools")
@mcp.tool()
def count_words(text: str) -> int:
    """Count the number of words in given text."""
    return len(text.split())

@mcp.tool()
def uppercase_text(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

@mcp.tool()
def reverse_text(text: str) -> str:
    """Reverse the given text."""
    return text[::-1]

if __name__ == "__main__":
    mcp.run(transport="stdio")