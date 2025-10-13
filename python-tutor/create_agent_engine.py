import vertexai
from vertexai import agent_engines

PROJECT_ID = "YOUR_PROJECT_ID"
LOCATION = "YOUR_LOCATION"

display_name = "Python Tutor"

vertexai.init(project=PROJECT_ID, location=LOCATION)

python_tutor_agent_engine = agent_engines.create(display_name = display_name)
