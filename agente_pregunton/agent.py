import random

from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.genai import types


sustainability_agent = RemoteA2aAgent(
    name="sustainability_agent",
    description="Answers questions about BBVAs sustainability practices.",
    agent_card=(
        f"http://localhost:8001/{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    instruction="""
      You are a helpful assistant that can answer questions about BBVAs sustainability practices.
      You delegate answering the questions to the sustainability_agent.

      Follow these steps:
      1. If the user asks a question related to sustainability at BBVA, delegate it to the sustainability_agent.
      2. If the question is not related to sustainability or BBVA do not answer it, and politely tell the user that you cannot help them.

      Always answer in spanish.
    """,
    sub_agents=[sustainability_agent],
)