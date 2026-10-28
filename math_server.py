## python code of my project 

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math-mcp-server")


@mcp.tool()
def add_numbers(num1: float, num2: float) -> float:
  """Add two numbers together. Use this when the user uses 'plus', '+', 'add', or 'sum'.

  Example: 45 + 15 or 45 plus 15.
  """
  print(f"[MCP TOOL] Adding {num1} + {num2}")
  return num1 + num2


@mcp.tool()
def subtract_numbers(num1: float, num2: float) -> float:
  """Subtract num2 from num1. Use this when the user uses 'minus', '-', 'subtract', or 'difference'.

  Example: 60 - 10 or 60 minus 10.
  """
  print(f"[MCP TOOL] Subtracting {num1} - {num2}")
  return num1 - num2

@mcp.tool()
def multiplication_numbers(num1: float, num2: float) -> float:
  """Multiply num1 to num2. Use this when the user uses 'multiply','*','x','multiplication'.
  Example: 10 * 20 or 10 multiply 20 or 10 x 20 ."""
  print(f"[MCP TOOL] Multiplication {num1} * {num2}")
  return num1 * num2

@mcp.tool()
def divide_numbers(num1: float, num2: float) -> str | float:
  """Divide num1 by num2 (num1 / num2). Use this when the user uses 'divide','/','divide by', 'divided by'.

  Example: '10 divided by 2' means num1 = 10, num2 = 2.
  """
  print(f"[MCP TOOL] Dividing {num1} / {num2}")
  if num2 == 0:
    return "Error: Division by zero is not allowed."
  return num1 / num2


if __name__ == "__main__":
  mcp.run(transport="sse")
