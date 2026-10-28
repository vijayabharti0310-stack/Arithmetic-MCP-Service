# Arithmetic-MCP-Service

A local AI-powered math assistant built using n8n, Ollama (Local LLM), and a custom Python Backend powered by the Model Context Protocol (MCP).

Instead of relying on the AI to guess or hallucinate calculations, this agent securely connects to a custom Python server to perform precise arithmetic operations (Addition, Subtraction, Multiplication, and Division).

🛠️ Tech Stack
n8n: Low-code workflow automation platform handling the chat interface and agent orchestration.

Ollama: Runs a local Large Language Model (LLM) to process natural language queries and math symbols (+, -, *, /).

Python (FastMCP): Custom backend server that defines the mathematical tools.

Model Context Protocol (MCP): Connects n8n to the Python script seamlessly via Server-Sent Events (SSE).

🏗️ Architecture & Workflow Flow
When chat message received: The entry point where the user types a query (e.g., "10 divided by 2").

AI Agent & Ollama Model: The brain analyzes the request and determines which math tool is required.

MCP Client: The bridge node in n8n that communicates with your local Python server.

Python Backend (math_server.py): Executes the specific function safely and returns the exact result back to the chat interface.

⚙️ Getting Started / Setup
1. Prerequisites
Make sure you have the following installed on your machine:

Python (v3.10+)

n8n (Desktop app or self-hosted)

Ollama with your preferred local model downloaded.

2. Python Server Setup
Clone this repository or create a new project folder in VS Code.

Install the required MCP Python package:

Bash
pip install mcp
Create a file named math_server.py and add your Python FastMCP code (handling addition, subtraction, multiplication, and division with error checks for division by zero).

Run your MCP server:

Bash
python math_server.py
(The server will start running locally, typically via SSE transport).

3. n8n Workflow Setup
Open n8n and create a new workflow.

Add a When chat message received node.

Connect an AI Agent node configured with an Ollama Chat Model.

Add an MCP Client node under Tools and link it to your running local Python server endpoint.

Save, test your chat window, and enjoy your local AI math agent!

💡 Example Queries
"What is 45 plus 15?"

"Subtract 10 from 60"

"Multiply 2 by 5"

"10 divided by 2"

📄 License
This project is open-source and available under the MIT License.
