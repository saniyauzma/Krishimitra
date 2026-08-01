# Krishi Mitra

Krishi Mitra is a fullstack agricultural assistant application with AI-powered RAG, crop prediction, disease detection, fertilizer recommendations, weather insights, and multilingual UI support.

## Project structure

- `backend/` — FastAPI backend with authentication, RAG, weather, crop prediction, fertilizer prediction, and crop disease endpoints.
- `frontend/` — Vite + React TypeScript frontend with UI components, routing, and localization.

## Prerequisites

- Python 3.11+ or compatible Python 3.x
- Node.js 18+ and npm
- MongoDB running locally or a valid `MONGO_URL`
- Optional: Pinecone and Gemini credentials for full RAG functionality

## Setup

### Backend

1. Open a terminal and go to the backend folder:

```powershell
cd backend
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install Python dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

4. Create or update `backend/.env` with your local configuration.

Example `backend/.env`:

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

### Frontend

1. Open a second terminal and go to the frontend folder:

```powershell
cd frontend
```

2. Install frontend dependencies:

```powershell
npm install
```

## Run locally

### Start backend

In the backend terminal:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`

### Start frontend

In the frontend terminal:

```powershell
cd frontend
npm run dev -- --host 0.0.0.0
```

Open:

- `http://localhost:8080`

## Notes

- `node_modules/` and `.venv/` are generated and should not be committed.
- Do not commit `.env` files or other secrets.
- `package-lock.json` is useful and can stay in the repo to lock dependency versions.
- If MongoDB is unavailable, the backend may fall back to an in-memory user store, but auth data will not persist.

## Common issues

- If the frontend cannot reach the backend, verify the backend is running on `http://127.0.0.1:8000` and the frontend is configured to use that URL.
- If translation language changes do not apply, make sure text is wrapped with `t('...')` keys and the locale files are present under `frontend/src/locales/`.

## Useful URLs

- Frontend app: `http://localhost:8080`
- Backend API: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`

## License

This project is recommended to use the `MIT` License.
