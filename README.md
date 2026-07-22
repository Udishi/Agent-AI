# AI Agent using Ollama

Overview

This project is a modular AI Agent built in Python using Ollama for local Large Language Model (LLM) inference. The agent is designed to process user queries intelligently by utilizing separate components for planning, memory management, and tool execution.

The system follows an agent-based architecture where user inputs are first analyzed by the Planner module, stored using the Memory module, and then executed through the Tools module to generate meaningful responses.

To improve usability, the project also includes a chatbot-based frontend interface built using HTML, CSS, and JavaScript and can be integrated with FastAPI for API communication.

 Features

- Local AI Agent powered by Ollama
- Modular and scalable architecture
- Conversation memory management
- Query planning and execution
- Tool integration system
- Interactive chatbot interface
- REST API support using FastAPI
- Responsive UI design
- Easy to extend with new tools and functionalities

Project Architecture


                    User
                      |
                      v
                Frontend UI
                      |
                      v
                  FastAPI
                      |
                      v
                   Agent
            --------------------
            |        |         |
         Memory   Planner    Tools
            |        |         |
            --------------------
                      |
                      v
                   Ollama
                      |
                      v
                 AI Response


Folder Structure


AI-Agent/

│
├── agent.py
├── planner.py
├── memory.py
├── tools.py
├── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

Technologies Used

- Python
- Ollama
- FastAPI
- HTML
- CSS
- JavaScript
- Git & GitHub
- VS Code

Working of the AI Agent

1. The user enters a query through the chatbot interface.

2. The query is sent to the FastAPI backend.

3. The Agent module receives the query and stores it using the Memory module.

4. The Planner module determines the appropriate action required for the given query.

5. The Tools module executes the planned action.

6. Ollama generates the response locally.

7. The generated response is sent back to the frontend and displayed to the user.

---

## Installation Guide

### Clone the Repository

```bash
git clone https://github.com/your-github-username/AI-Agent.git


 Navigate to the Project Directory

```bash
cd AI-Agent
```

 Install Dependencies

```bash
pip install -r requirements.txt
```

Run Ollama

Make sure Ollama is installed and running on your system.

Example:

```bash
ollama run llama3
```

### Run the FastAPI Server

```bash
uvicorn main:app --reload
```

The backend server will start at:

```
http://127.0.0.1:8000
```

---

## Frontend Interface

The project includes a chatbot-based frontend that provides:

- Clean and responsive user interface
- Real-time query submission
- AI-generated responses
- Interactive chatbot experience
- Dark mode design

---

## Modules Description

### Agent Module

Responsible for managing the complete execution pipeline of the AI agent.

### Memory Module

Stores user inputs and AI-generated responses for maintaining conversational context.

### Planner Module

Analyzes user queries and determines the action to be performed.

### Tools Module

Executes the planned action and returns the appropriate output.

Future Enhancements

The project can be further extended with:

- Voice assistant capabilities
- PDF and document analysis
- Web search integration
- Multi-agent systems
- Image processing support
- Deployment using Docker
- User authentication
- Cloud-based deployment
- Integration with external APIs

Applications

- Personal AI Assistant
- Educational Chatbot
- Productivity Assistant
- Research Assistant
- Local LLM Applications
- AI-powered Automation Systems

Conclusion

This project demonstrates the implementation of an AI Agent using a modular architecture and local LLM inference through Ollama. By combining memory management, planning capabilities, and tool execution, the system provides a scalable foundation for building intelligent AI applications while maintaining user privacy through local model execution.
