from google.adk.agents import Agent, LlmAgent

GEMINI_MODEL = "gemini-2.0-flash"

code_writer_agent = LlmAgent(
    name="CodeWriterAgent",
    model=GEMINI_MODEL,

    instruction="""You are a Python Code Generator.
Based *only* on the user's request, write Python code that fulfills the requirement.
Output *only* the complete Python code block, enclosed in triple backticks (```python ... ```). 
Do not add any other text before or after the code block.
""",
    description="Writes initial Python code based on a specification.",
)

root_agent = code_writer_agent