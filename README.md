# Krishi Mitra

Krishi Mitra is a fullstack agricultural assistant application with AI-powered RAG, crop prediction, disease detection, fertilizer recommendations, weather insights, and multilingual support.

## Project structure

- `backend/` — FastAPI backend with authentication, RAG, weather, crop prediction, fertilizer prediction, and crop disease endpoints.
- `frontend/` — Vite + React TypeScript frontend with UI components, routing, localization, and dashboard pages.

## Prerequisites

- Python 3.11+ (or compatible Python 3.x)
- Node.js 18+ / npm
- MongoDB running locally or a valid `MONGO_URL`
- Optional: Pinecone and Gemini credentials for full RAG support

## Setup

### 1. Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create or update `backend/.env` with your local configuration. Example values:

```dotenv
MONGO_URL=mongodb://localhost:27017/
JWT_SECRET=YOUR_SECRET
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

PINECONE_API_KEY=your_pinecone_key
PINECONE_ENVIRONMENT=us-east-1
PINECONE_INDEX_NAME=krishimitra-knowledge

EMBEDDING_MODEL_NAME=sentence-transformers/all-mpnet-base-v2
EMBEDDING_DIMENSION=768

LLM_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_key
GEMINI_MODEL=gemini-2.0-flash-exp

DEFAULT_TOP_K=5
MAX_TOP_K=20

MAX_TOKENS=1000
TEMPERATURE=0.7

OPENWEATHER_API_KEY=your_openweather_key

GRAPH_TIMEOUT=30
ENABLE_GRAPH_LOGGING=true

LOG_LEVEL=INFO
```

### 2. Frontend

```powershell
cd frontend
npm install
```

## Run locally

### Start backend

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Then open:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`

### Start frontend

```powershell
cd frontend
npm run dev -- --host 0.0.0.0
```

Then open:

- `http://localhost:8080`

## Notes

- The backend will fall back to an in-memory user store if MongoDB is unreachable, so auth may still work locally but data will not persist.
- Keep `.env` and other secret files out of git. The repository `.gitignore` already excludes `.env`, `.venv/`, and other generated files.
- `node_modules/` and `.venv/` are generated dependencies and should not be committed.
- `package-lock.json` is optional for npm dependency locking.

## Known fixes and debugging notes

- `backend/requirements.txt` should be UTF-8 encoded to avoid install errors.
- The backend may require a valid `MONGO_URL` in `backend/.env` for persistent auth data.
- Local network access works when frontend runs with `--host 0.0.0.0` and backend binds to `0.0.0.0` or `127.0.0.1`.

## Useful URLs

- Frontend: `http://localhost:8080`
- Backend: `http://127.0.0.1:8000`
- API docs: `http://127.0.0.1:8000/docs`

## License

This project is recommended to use the `MIT` License.
