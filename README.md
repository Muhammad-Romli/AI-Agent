# AI Agent (Boot.dev)

A lightweight CLI-based AI agent built as part of the backend development curriculum on [Boot.dev](https://www.boot.dev). This project demonstrates the fundamentals of building agentic workflows, function/tool calling, and managing stateful conversations with large language models.

---

> ⚠️ **WARNING: EXPERIMENTAL / TOY PROJECT**
> 
> This project is strictly an educational tool and experimental agent. Unlike production-grade tools (such as **Claude Code** or other managed agent environments), it **lacks advanced safety sandboxing, strict permission controls, and execution guardrails**. 
> 
> * **Do not** grant it unrestricted access to sensitive environments, sensitive API keys, or production systems.
> * **Do not** allow it to execute untrusted system commands or modify critical files without supervision.
> * Run strictly in an isolated local virtual environment (`venv`). Use at your own risk!

---

## 💡 How It Works & Key Architecture

1. **Prompt Processing Loop:** Listens to user inputs and passes context along with available tool definitions to the LLM.
2. **Function Calling / Tool Execution:** Decodes structured function calls returned by the model, executes the corresponding Python logic locally, and feeds the results back to the conversation stack.
3. **API Integration:** Uses the official `openai` SDK to handle structured outputs and agent responses.

---

## 🛠️ Stack & Dependencies

* **Language:** Python 3.10+
* **Environment & Package Manager:** [`uv`](https://github.com/astral-sh/uv) (or standard `venv`)
* **Key Packages:**
  * `openai == 2.44.0` — Official SDK for interacting with the model API
  * `python-dotenv == 1.1.0` — Environment variable management for API keys

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have [`uv`](https://github.com/astral-sh/uv) installed on your system:
```bash
# Install uv if you haven't already
pip install uv


# Clone the repositor
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

# Create virtual environment and install exact dependencies
uv venv
uv add openai==2.44.0 python-dotenv==1.1.0


