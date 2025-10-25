from letta_client import Letta
from dotenv import load_dotenv
import os

load_dotenv()
client = Letta(
    token=os.getenv("LETTA_TOKEN")
)
agent = client.agents.create(
    project_id= os.getenv("PROJECT_ID"),
    model="openai/gpt-4o-mini",
    memory_blocks=[
        {"label": "human", "limit": 2000, "value": "Name: Bob"},
        {"label": "persona", "limit": 2000, "value": "You are a friendly agent"}
    ]
)
