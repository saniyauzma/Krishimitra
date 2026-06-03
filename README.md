# Krishi Mitra

Krishi Mitra is a fullstack agricultural assistant application with AI-powered RAG, crop prediction, disease detection, fertilizer recommendations, and weather insights.

## Project structure

- `backend/` — FastAPI backend with authentication, RAG, weather, crop prediction, fertilizer prediction, and crop disease endpoints.
- `frontend/` — Vite + React TypeScript frontend with UI components, routing, and localization.

## Run locally

### Backend

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Open: `http://127.0.0.1:8000`
API docs: `http://127.0.0.1:8000/docs`

### Frontend

```powershell
cd frontend
npm install
npm run dev
```

Open: `http://127.0.0.1:5173`

## Notes

- Keep your existing `.gitignore` files for root, backend, and frontend.
- Add any sensitive values to `.env` files only and do not commit them.

## License

This project is recommended to use the `MIT` License.
