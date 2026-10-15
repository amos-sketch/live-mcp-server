
import hashlib
import os
import re

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_request

mcp = FastMCP("exam-challenge-server")

EMAIL = "24ds2000085@ds.study.iitm.ac.in"


@mcp.tool(name="solve_challenge")
def solve_challenge() -> str:
    """Solve the current exam challenge from the HTTP request header."""
    request = get_http_request()
    challenge = request.headers.get("x-exam-challenge", "")

    if not re.fullmatch(r"[0-9a-f]{32}", challenge):
        raise ValueError("Missing or invalid X-Exam-Challenge header")

    message = f"{challenge}:{EMAIL}"
    return hashlib.sha256(message.encode("utf-8")).hexdigest()[:16]


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
    )
