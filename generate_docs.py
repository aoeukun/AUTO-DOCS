import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # Load your API key from .env

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-thinking-exp-01-21:generateContent"

# Prompt template
SYSTEM_PROMPT = """You are an expert technical writer and software engineer.

Given the following Python code, generate clear, concise, and professional documentation in Markdown format.

- For each function or class:
  - Explain **what it does**, its **purpose**, and **use cases**
  - Include input parameters with **types** and **descriptions**
  - Describe the **return value** with type and meaning
  - Mention any **side effects**, **exceptions**, or special behaviors
  - Write in a friendly, human-readable tone for developers
  - Format the output using **Markdown** with proper headers, bullet points, and code blocks
  - If there is no function or class in the code, don't mention it.

Output only the documentation markdown.

Here is the code:
"""

def call_gemini(code: str) -> str:
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": GEMINI_API_KEY
    }
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": SYSTEM_PROMPT + "\n\n```python\n" + code + "\n```"}
                ]
            }
        ]
    }

    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=data)
    response.raise_for_status()
    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"]

def generate_docs(code_path: Path, output_path: Path):
    with open(code_path, "r", encoding="utf-8") as f:
        code = f.read()

    markdown = call_gemini(code)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Documentation for `{code_path.name}`\n\n")
        f.write(markdown)

def main():
    src_dir = Path("src")
    out_dir = Path("docs/generated")

    for py_file in src_dir.rglob("*.py"):
        output_file = out_dir / f"{py_file.stem}.md"
        generate_docs(py_file, output_file)

if __name__ == "__main__":
    main()
