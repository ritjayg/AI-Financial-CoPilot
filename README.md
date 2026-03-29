# AI Financial Copilot

A full-stack scaffold for an **AI-powered financial assistant**: a **FastAPI** backend (LangChain + OpenAI, **yfinance** for market data, modular **data** and **decision** agents) and a **React + Vite** frontend. This repository is structured for clarity and growth—implement business logic in `agents/` and `services/` without bloating route handlers.

> **Note:** The app currently exposes a minimal API and UI (“ping” the chat status). Wire the LLM, stock service, and chat endpoints as you build out features.

---

## Features (target architecture)

| Area | Description |
|------|-------------|
| **Chat** | Conversational API backed by OpenAI via LangChain |
| **Market data** | Real-time / delayed quotes and context via `yfinance` |
| **Agents** | **Data agent** (fetch & format market context) · **Decision agent** (reasoning & replies) |
| **Frontend** | Simple React UI ready to connect to `/api` |

---

## Tech stack

- **Backend:** Python 3.11+, FastAPI, Uvicorn, LangChain, OpenAI, python-dotenv, yfinance, Pydantic  
- **Frontend:** React 18, Vite 6  
- **Repo:** Monorepo layout (`backend/`, `frontend/`)

---

## Repository layout

```
AI-Financial-CoPilot/
├── .env.example
├── .gitignore
├── README.md
├── backend/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app + CORS + routers
│   ├── requirements.txt
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── data_agent.py       # Market context orchestration
│   │   └── decision_agent.py   # LLM-driven responses
│   ├── routes/
│   │   ├── __init__.py
│   │   └── chat.py             # Chat-related HTTP routes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_service.py      # LangChain + OpenAI
│   │   └── stock_service.py    # yfinance helpers
│   └── utils/
│       ├── __init__.py
│       └── ticker.py           # Optional ticker heuristics
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── main.jsx
        ├── index.css
        ├── App.jsx
        ├── App.css
        ├── api.js
        └── components/
            └── ChatBox.jsx
```

---

## Prerequisites

- **Python** 3.11 or newer  
- **Node.js** 18+ and npm  
- **OpenAI API key** (for future LLM integration; not required to run the scaffold)

---

## Setup (step by step)

### 1. Clone and enter the project

```bash
git clone <your-fork-or-repo-url>.git
cd AI-Financial-CoPilot
```

### 2. Backend virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt
```

### 3. Environment variables

```bash
cp .env.example .env
# Edit .env and set OPENAI_API_KEY when you implement the LLM layer.
```

### 4. Run the API

From the **repository root** (so `backend` imports resolve):

```bash
source .venv/bin/activate
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

- Health check: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)  
- OpenAPI docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 5. Frontend

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173). The dev server proxies `/api` to `http://127.0.0.1:8000` (see `frontend/vite.config.js`). Use **“Ping chat API status”** to verify the backend.

### 6. Production build (frontend)

```bash
cd frontend
npm run build
npm run preview   # optional: test the static build
```

Serve `frontend/dist/` with any static host; set `VITE_API_URL` at build time to your API origin if the API is on another domain.

---

## API overview (scaffold)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Liveness |
| GET | `/api/chat/status` | Placeholder until real chat is implemented |

---

## Development conventions

- Keep **HTTP** thin in `routes/`; put integrations in `services/` and orchestration in `agents/`.
- Load secrets with **python-dotenv** (`load_dotenv()` is called in `backend/main.py`).
- Prefer **async** route handlers when calling async agents or I/O.

---

## Future improvements

- **POST /api/chat** with message history and streaming (SSE or WebSockets).
- Implement `llm_service.get_llm()` and connect `DecisionAgent` to LangChain + OpenAI.
- Implement `stock_service` + `DataAgent.build_context()` with caching and rate limits.
- Auth (API keys or OAuth) before exposing in production.
- Tests: `pytest` for backend, Vitest/RTL for frontend.
- CI: lint, type-check, and test on push.

---

## License

Add a `LICENSE` file when you publish (e.g. MIT).

---

*This project is for learning and portfolio use. It is not financial advice.*
