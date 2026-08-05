TaskManager Agent
A lightweight, LangChain‑powered AI agent that manages tasks using a local SQLite3 database.
The agent can:

Add new tasks

List all tasks

Mark tasks as completed

Update task status

Persist tasks in SQLite

Interact through natural language using an LLM (OpenRouter models)

This project is ideal for learning LangChain agents, tool usage, and simple DB-backed workflows.
Features
✔ Add Tasks
Create new tasks with a description and timestamp.

✔ List Tasks
Retrieve all tasks stored in the SQLite database.

✔ Update Task Status
Mark tasks as completed or update their status.

✔ Natural Language Interface
The agent interprets user instructions like:

“Add a task to call the client tomorrow.”

“Show me all pending tasks.”

“Mark task 3 as completed.”

✔ SQLite3 Storage
All tasks are stored locally in a SQLite database (tasks.db).

| Component | Purpose |
| --- | --- |
| **LangChain** | Agent framework, tools, LLM orchestration |
| **LangChain‑OpenRouter** | Connects LangChain to OpenRouter LLMs |
| **SQLite3** | Lightweight local database |
| **Python‑dotenv** | Loads API keys from ``.env`` |

dependencies:
langchain>=1.3.14
langchain-openrouter>=0.2.7
python-dotenv>=1.2.2

Project structure:
taskmanager_agent/
│
├── agent.py               # Main agent logic
├── db.py                  # SQLite helper functions
├── tools.py               # Tools exposed to the agent
├── tasks.db               # SQLite database (auto-created)
├── .env                   # OPENROUTER_API_KEY
├── requirements.txt
└── README.md

Setup Instructions:

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. 4. Add your OpenRouter API key
  
