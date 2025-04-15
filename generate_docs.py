import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv
import yaml

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-70b-8192"

SYSTEM_PROMPT = """You are an expert technical writer and software engineer.

Given the following Python code, generate clear, concise, and professional documentation in Markdown format.

- For each function or class:
  - Explain what it does, its purpose, and use cases
  - Include input parameters with types and descriptions
  - Describe the return value with type and meaning
  - Mention any side effects, exceptions, or special behaviors
  - Write in a friendly, human-readable tone for developers
  - Format the output using Markdown with proper headers, bullet points, and code blocks
  - If there is no function or class in the code, don't mention it.

Output only the documentation markdown.
"""

def call_groq(code: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"```python\n{code}\n```"}
        ]
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    return result["choices"][0]["message"]["content"]

def generate_docs(code_path: Path, output_path: Path):
    with open(code_path, "r", encoding="utf-8") as f:
        code = f.read()

    documentation = call_groq(code)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Documentation for `{code_path.name}`\n\n")
        f.write(documentation)

def update_mkdocs_nav(generated_dir: Path, mkdocs_yml_path: Path):
    with open(mkdocs_yml_path, "r") as f:
        config = yaml.safe_load(f)

    # Preserve manual entries
    config["nav"] = [entry for entry in config.get("nav", []) if not isinstance(entry, dict) or "Generated Docs" not in entry]

    # Create updated "Generated Docs" nav
    generated_nav = []
    for file in sorted(generated_dir.glob("*.md")):
        title = file.stem.replace("_", " ").title()
        path = str(file.relative_to("docs"))
        generated_nav.append({title: path})

    config["nav"].append({"Generated Docs": generated_nav})

    with open(mkdocs_yml_path, "w") as f:
        yaml.dump(config, f)

def main():
    src_dir = Path("src")
    out_dir = Path("docs/generated")
    mkdocs_yml = Path("mkdocs.yml")

    for file in src_dir.rglob("*.py"):
        output_file = out_dir / f"{file.stem}.md"
        generate_docs(file, output_file)

    update_mkdocs_nav(out_dir, mkdocs_yml)
    print("✅ Documentation generated and mkdocs.yml updated!")

if __name__ == "__main__":
    main()
