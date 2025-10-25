import os
from dotenv import load_dotenv
from letta_client import Letta

# Load environment variables from .env (if present)
load_dotenv()

# Initialize the Letta client using LETTA_API_KEY environment variable
api_key = os.getenv("LETTA_API_KEY")
if not api_key:
    raise RuntimeError("LETTA_API_KEY not found in environment. Please set LETTA_API_KEY in your environment or .env file.")

client = Letta(token=api_key)

# Create an agent with memory blocks
agent = client.agents.create(
    memory_blocks=[
        {
            "label": "human",
            "value": "The user is interested in learning about AI and technology."
        },
        {
            "label": "persona",
            "value": "I am Alex, a knowledgeable and friendly AI assistant. I explain complex concepts in simple terms and always aim to be helpful while maintaining a warm, approachable demeanor."
        }
    ],
    # Use built-in tools for web search and code execution
    tools=["web_search", "run_code"],
    # Use the recommended models
    model="openai/gpt-4.1",
    embedding="openai/text-embedding-3-small"
)

print(f"Created agent with ID: {agent.id}")

# Function to handle conversation
def chat_with_agent(message):
    response = client.agents.messages.create(
        agent_id=agent.id,
        messages=[{"role": "user", "content": message}]
    )
    
    # Extract and print responses
    for msg in response.messages:
        if msg.message_type == "assistant_message":
            print("\nAssistant:", msg.content)
        elif msg.message_type == "reasoning_message":
            print("\nReasoning:", msg.reasoning)
        elif msg.message_type == "tool_call_message":
            print(f"\nTool Call: {msg.tool_call.name}")
            print(f"Arguments: {msg.tool_call.arguments}")
        elif msg.message_type == "tool_return_message":
            print(f"\nTool Result: {msg.tool_return}")

'''
def check_agent_memory():
    """Retrieve and display the agent's memory blocks"""
    try:
        # Get list of memory blocks for the agent
        blocks = client.agents.blocks.list(agent_id=agent.id)
        
        print("\n" + "="*60)
        print("🧠 AGENT MEMORY")
        print("="*60)
        
        # Print each memory block's contents
        for block in blocks:
            print(f"\n📝 {block.label.upper()}:")
            print(f"   {block.value}")
        
        return blocks
        
    except Exception as e:
        print(f"❌ Error getting memory blocks: {e}")
        return None

'''

# Start with a simple greeting
print("\nStarting conversation with AI Assistant...")
chat_with_agent("Hello! I'm ready to help you learn about AI and technology.")

# Interactive chat loop
print("\nChat with the AI Assistant (type 'exit' to end the conversation)")
print("--------------------------------------------------------")

while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("\nGoodbye!")
        break
    if user_input:
        chat_with_agent(user_input)
