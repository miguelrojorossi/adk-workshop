from google.adk.agents import Agent
from google.genai import types
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams
import os

GEMINI_MODEL = "gemini-2.0-flash"

prompt = """
  You're an assistant that helps with calculations. You handle adding and substracting. In order to do this you use the tools available.
"""

root_agent = Agent(
    model=GEMINI_MODEL,
    name='calcula_agent',
    description='A helpful calculations assistant.',
    instruction=prompt,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="YOUR_MCP_SERVER_URL",
                headers={}
                ),
                )
    ],
)
