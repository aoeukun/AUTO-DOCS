# Documentation for `gen.py`

```python
"""This script automatically generates documentation for Python code using the Gemini AI model and updates the mkdocs navigation file.

It reads Python files from the 'src' directory, generates documentation in Markdown format using the Gemini model,
saves the documentation to the 'docs/generated' directory, and updates the 'mkdocs.yml' file to include the generated documentation in the MkDocs navigation.
"""
import os
import json
from pathlib import Path
import yaml
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini setup
genai.configure(api_key=API_KEY)

MODEL_NAME = "models/gemini-2.0-flash-thinking-exp-01-21"

SYSTEM_PROMPT = """Act as a Python code documentation assistant. Your task is to add comprehensive documentation to the provided Python code snippet, making it clear, understandable, and maintainable.

**Instructions:**

1.  **Analyze the Code:** Understand the purpose and logic of the provided Python code.
2.  **Add Docstrings:**
    * Include a **module-level docstring** at the very beginning of the script explaining its overall purpose and functionality.
    * Add **function/method/class docstrings** immediately following their definition lines (`def` or `class`).
    * Follow a clear and standard convention, preferably **Google style**:
        * Start with a concise one-line summary (using the imperative mood, e.g., "Calculate..." not "Calculates..."). End with a period.
        * Include a blank line after the summary if more detail follows.
        * Add further elaboration on the object's purpose or logic if necessary.
        * Use an `Args:` section to detail each parameter (`parameter_name (type): Description of the parameter.`).
        * Use a `Returns:` section to detail the return value (`type: Description of the return value.`). If the function doesn't return anything explicitly (returns `None`), you can state that or omit the section.
        * Use a `Raises:` section (if applicable) to detail any specific exceptions the code might intentionally raise (`ExceptionType: Condition under which it's raised.`).
3.  **Add Inline Comments:** Insert inline comments (`#`) judiciously to clarify specific lines or blocks of code that involve complex logic, non-obvious operations, or important algorithmic steps. Avoid commenting on obvious code.
4.  **Maintain Code Integrity:** Do not change the original code's logic or functionality. Only add documentation elements (docstrings and comments).
5.  **Output Format:** Return the *complete* Python code, including the original logic, with all the added docstrings and relevant inline comments integrated directly into the code. Ensure the output is presented as a single, well-formatted Python code block.

**Python Code to Document:**
"""

def call_gemini(code: str) -> str:
    """Calls the Gemini AI model to generate documentation for the given Python code.

    This function sends a request to the Gemini model with a system prompt instructing it to act as a Python code documentation assistant,
    along with the provided Python code snippet. It then returns the text response from the Gemini model, which is expected to be the generated documentation.

    Args:
        code (str): The Python code snippet to be documented.

    Returns:
        str: The generated documentation text from the Gemini model.
    """
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content([
        {"role": "user", "parts": [{"text": f"{SYSTEM_PROMPT}\n```python\n{code}\n```"}]}
    ])
    return response.text

def generate_docs(code_path: Path, output_path: Path):
    """Generates documentation for a Python file and saves it to a Markdown file.

    Reads the content of the Python file specified by `code_path`, calls the `call_gemini` function to generate documentation,
    creates the parent directories for the output file if they don't exist, and then writes the generated documentation
    to a Markdown file at `output_path`. The output Markdown file includes a header with the name of the documented Python file.

    Args:
        code_path (Path): Path to the Python file for which documentation needs to be generated.
        output_path (Path): Path to the Markdown file where the generated documentation will be saved.
    """
    code = code_path.read_text(encoding="utf-8") # Read the content of the Python file.
    documentation = call_gemini(code) # Generate documentation using Gemini.
    output_path.parent.mkdir(parents=True, exist_ok=True) # Create parent directories if they don't exist.
    output_path.write_text(f"# Documentation for `{code_path.name}`\n\n{documentation}", encoding="utf-8") # Write documentation to Markdown file.

def update_mkdocs_yml():
    """Updates the mkdocs.yml file to include a navigation section for the generated documentation.

    This function reads the `mkdocs.yml` configuration file, identifies or creates a 'Generated Docs' section in the navigation,
    and adds links to all generated Markdown documentation files (located in the 'docs/generated' directory) to this section.
    It ensures that if a 'Generated Docs' section already exists, it is replaced with the updated list of generated documentation files.
    Finally, it writes the updated configuration back to `mkdocs.yml`.
    """
    GENERATED_DIR = Path("docs/generated")
    MKDOCS_YML_PATH = Path("mkdocs.yml")

    with open(MKDOCS_YML_PATH, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f) # Load the mkdocs.yml configuration.

    files = [f for f in GENERATED_DIR.iterdir() if f.suffix == ".md"] # Get all Markdown files in the generated docs directory.
    files.sort() # Sort the files alphabetically.

    new_nav = []
    for item in config.get("nav", []): # Iterate through existing navigation items.
        if isinstance(item, dict) and "Generated Docs" in item:
            continue # Skip the existing 'Generated Docs' section to replace it.
        new_nav.append(item) # Keep other existing navigation items.

    generated_section = {"Generated Docs": []} # Initialize a new 'Generated Docs' section.
    for file in files:
        title = file.stem.replace("_", " ").title() # Create title from filename, replacing underscores and capitalizing.
        generated_section["Generated Docs"].append({title: f"generated/{file.name}"}) # Add file link to the 'Generated Docs' section.

    new_nav.append(generated_section) # Append the new 'Generated Docs' section to the navigation.
    config["nav"] = new_nav # Update the navigation in the configuration.

    with open(MKDOCS_YML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(config, f, sort_keys=False) # Write the updated configuration back to mkdocs.yml, preserving order.

    print("✅ mkdocs.yml updated successfully.")

def main():
    """Main function to orchestrate the documentation generation process.

    This function sets up the source and output directories, iterates through all Python files in the 'src' directory recursively,
    generates documentation for each Python file using the `generate_docs` function, and finally updates the `mkdocs.yml`
    file to include the generated documentation in the navigation using the `update_mkdocs_yml` function.
    """
    src_dir = Path("src")
    out_dir = Path("docs/generated")

    for file in src_dir.rglob("*.py"): # Recursively find all Python files in the source directory.
        generate_docs(file, out_dir / f"{file.stem}.md") # Generate documentation for each Python file.

    update_mkdocs_yml() # Update mkdocs.yml with the new documentation files.
    print("🎉 Documentation generated and mkdocs navigation updated.")

if __name__ == "__main__":
    main()
```