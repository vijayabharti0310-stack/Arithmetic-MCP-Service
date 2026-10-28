# This code will use when you want to work with same workflow in langgraph just copy this code and paste it 
# into your vs with .py

from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent


@tool
def add_numbers(num1: float, num2: float) -> float:
  """Add two numbers together (num1 + num2)."""
  print(f"[TOOL] Adding {num1} + {num2}")
  return num1 + num2


@tool
def subtract_numbers(num1: float, num2: float) -> float:
  """Subtract num2 from num1 (num1 - num2)."""
  print(f"[TOOL] Subtracting {num1} - {num2}")
  return num1 - num2


@tool
def multiplication_numbers(num1: float, num2: float) -> float:
  """Multiply two numbers together (num1 * num2)."""
  print(f"[TOOL] Multiplying {num1} * {num2}")
  return num1 * num2


@tool
def divide_numbers(num1: float, num2: float) -> str | float:
  """Divide num1 by num2 (num1 / num2)."""
  print(f"[TOOL] Dividing {num1} / {num2}")
  if num2 == 0:
    return "Error: Division by zero is not allowed."
  return num1 / num2


# Define all tools in a list
tools = [add_numbers, subtract_numbers, multiplication_numbers, divide_numbers]

# Initialize the local Ollama model (Make sure Ollama is running)
# Change the model to qwen2.5:3b
model = ChatOllama(model="qwen2.5:3b", temperature=0)
# Create the LangGraph ReAct agent
app = create_react_agent(model, tools)


# Function to test the agent
def run_agent(query: str):
  print(f"\nUser: {query}")
  inputs = {"messages": [("user", query)]}

  for step in app.stream(inputs, stream_mode="updates"):
    for node_name, output_values in step.items():
      if "messages" in output_values:
        for msg in output_values["messages"]:
          if msg.content:
            print(f"AI: {msg.content}")


if __name__ == "__main__":
  # Test queries
  run_agent("What is 45 plus 15?")
  run_agent("10 divided by 2")



# after writing above code make a new file and give name like :- langgrapg.json 
# and paste given code in langgrapg.json

{
  "dependencies": ["."],
  "graphs": {
    "arithmetic_mcp_service_langgrapg": "./arithmetic_mcp_service_langgrapg.py:app"
  },
  "env": ".env"
}


# after writing this code 
# go to the vs code terminal (which is below of your code area ) and type -   langgrapg dev
# After sometime you can see on your screen a new page will apper named LangSmith studio-....
# here you see your recent project 
# in langgrapg window you can see 2 options graph and chat.



