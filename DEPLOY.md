# Deployment notes

This repo includes Dockerfiles for both backend and frontend plus a `docker-compose.yml` for local testing.

Quick local test:

```bash
# build and run
docker compose up --build

# backend: http://localhost:8000
# frontend: http://localhost:3000
```

Render deployment notes (backend):
- Create a new Web Service on Render and connect your repo.
- Set the build command: `docker build -t krishimitra-backend -f backend/Dockerfile .`
- Start command: the Dockerfile already starts Uvicorn on port 8000.
- Add env var `MONGO_URI` pointing to your MongoDB Atlas connection string.
- Note: Render free tier will sleep after inactivity.

Vercel deployment (frontend):
- Connect the `frontend` folder to Vercel, set framework to `Vite`.
- Set `VITE_API_BASE` env var in Vercel to your deployed backend URL.
