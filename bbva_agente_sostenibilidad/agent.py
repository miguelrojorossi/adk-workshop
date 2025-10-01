from google.adk.agents import LlmAgent
from google.adk.tools import VertexAiSearchTool
from google.adk.a2a.utils.agent_to_a2a import to_a2a
 
PROJECT_ID = "mrr-ai"
LOCATION = "global"
DATASTORE_ID = "bbva-sustainability-docs_1759233294445"
GEMINI_MODEL = "gemini-2.0-flash"

GOOGLE_GENAI_USE_VERTEXAI="TRUE"
GOOGLE_CLOUD_PROJECT="mrr-ai"
GOOGLE_CLOUD_LOCATION="europe-southwest1"

# The full datastore path is constructed from the environment variables.
full_datastore_path = f"projects/{PROJECT_ID}/locations/{LOCATION}/collections/default_collection/dataStores/{DATASTORE_ID}"

# Tool Instantiation
vertex_search_tool = VertexAiSearchTool(data_store_id=full_datastore_path)

# Agent Definition
# This agent is designed to be run with the ADK CLI.
# The ADK expects to find a variable named `root_agent`.
root_agent = LlmAgent(
    name="bbva_agente_sostenibilidad",
    model=GEMINI_MODEL,
    tools=[vertex_search_tool],
    instruction=f"""
        You are an agent that can answer questions about BBVAs sustabinility practices. In order to do it you use tool vertex_search_tool.
        If the answer isn't in the search tool, say that you couldn't find the information, DO NOT INVENT IT OR USE YOUR OWN KNOWLEDGE TO ANSWER.
        At the end of the conversation, you thank the user and wish them a nice day.
        You always speak in spanish, no matter what language they have talked to you in.
    """,
    description="Answers questions about BBVAs sustainability practices.",
)

a2a_app = to_a2a(root_agent, port=8001)
