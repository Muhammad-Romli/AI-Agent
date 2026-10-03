# AI Agent

> **Warning: experimental toy project.**
> This agent has no real sandboxing, permission system, or execution guardrails, unlike production tools such as Claude Code.
> - Don't run it on production systems or give it access to sensitive files or API keys.
> - Don't let it run untrusted code or modify important files unsupervised.
> - Use it only in an isolated environment.

## Table of Contents

- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Limitations](#limitations)
- [Dependencies](#dependencies)

## How It Works

1. The user's prompt is sent to the LLM along with the available tool definitions.
2. If the model requests a function call, the agent runs the matching Python function locally.
3. The result is appended to the conversation and sent back to the model.
4. The loop repeats until the model returns a final answer.

Available tools (in `functions/`):

| Tool | Purpose |
|---|---|
| `get_files_info` | List files in a directory |
| `get_file_content` | Read a file's contents |
| `write_file` | Create or overwrite a file |
| `run_python_file` | Execute a Python file |

The `calculator/` directory is the sample project the agent works on.

## Installation

Requires Python 3.10+ and [uv](https://github.com/astral-sh/uv).

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
uv sync
```

Create a `.env` file in the project root:

```
API_KEY=your_key_here
```

## Usage

```bash
uv run main.py "your prompt here"
```

Example:

```bash
uv run main.py "fix the bug in the calculator"
```

## Limitations

- No sandboxing: the agent can read, write, and execute files within its working directory.
- No permission prompts before running actions.
- Minimal error handling and no conversation persistence between runs.

## Dependencies

- `openai==2.44.0`
- `python-dotenv==1.1.0`
