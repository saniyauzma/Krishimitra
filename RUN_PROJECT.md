# Run Krishi Mitra Locally

## Frontend

From the `frontend` folder:

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

Then open:

- `http://localhost:8080/`

## Backend

From the `backend` folder in the project root:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Then open:

- `http://127.0.0.1:8000/`
- API docs: `http://127.0.0.1:8000/docs`

## Notes

- Update `backend/.env` with your own `MONGO_URL` before starting the backend.
- If MongoDB is not available locally, the backend falls back to an in-memory store and data will not persist.
- Use `http://localhost:8080/` for the frontend app and `http://127.0.0.1:8000/` for the backend API.
