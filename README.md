# 🤖 CrewAI Engineering Team

An automated multi-agent software engineering team built with **CrewAI** 🚀 and powered by local LLMs via **Ollama** 𦙙. This project orchestrates multiple specialized AI agents to design, implement, test, and generate a user interface for Python applications.

---

## 🏗️ Architecture & Agents

The crew consists of four specialized AI agents working together:

1. **🏗️ Engineering Lead**: Analyzes requirements and drafts a structured `Architecture_Plan.json` outlining the required modules, classes, and methods.
2. **💻 Backend Engineer**: Generates clean, modular Python backend code based on the architecture plan.
3. **🧪 Test Engineer**: Writes unit tests for each generated backend module to ensure functionality.
4. **🖼️ Frontend Engineer**: Constructs a single-file interactive **Gradio** web interface to demonstrate the backend module.

---

## 📁 Project Structure

```text
engineering_team_x/
├── knowledge/          # Knowledge base files for agents
├── output/             # Output directory for generated code & tests
│   ├── Architecture_Plan.json
│   ├── account.py
│   ├── auth.py
│   ├── test_account.py
│   ├── test_auth.py
│   └── app.py
├── src/                # Core CrewAI source code & workflows
├── tests/              # Project test suites
├── .gitignore          # Excluded environment and build files
├── AGENTS.md           # Agent roles and configuration details
├── NOTES.md            # Troubleshooting guide & technical notes
├── pyproject.toml      # Project dependencies and setup
└── README.md           # Project documentation
