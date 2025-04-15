import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

SYSTEM_PROMPT = """You are an expert technical writer and software engineer.

Given the following Python code, generate clear, concise, and professional documentation in Markdown format.

- For each function or class:
  - Explain what it does, its purpose, and use cases
  - Include input parameters with types and descriptions
  - Describe the return value with type and meaning
  - Mention any side effects, exceptions, or special behaviors
  - Write in a friendly, human-readable tone for developers
  - Format the output using Markdown with proper headers, bullet points, and code blocks
  - If there is no function or class, don't generate anything.
"""

def call_groq(code: str) -> str:
    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"```python\n{code}\n```"}
        ]
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def generate_docs(code_path: Path, output_path: Path):
    code = code_path.read_text(encoding="utf-8")
    documentation = call_groq(code)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"# Documentation for `{code_path.name}`\n\n{documentation}", encoding="utf-8")

def main():
    src_dir = Path("src")
    out_dir = Path("docs/generated")
    for file in src_dir.rglob("*.py"):
        generate_docs(file, out_dir / f"{file.stem}.md")

if __name__ == "__main__":
    main()
