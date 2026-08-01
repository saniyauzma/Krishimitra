---
title: Krishimitra Backend
emoji: 🌾
colorFrom: green
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
---

# Krishimitra Backend

FastAPI backend for Krishimitra — crop recommendation, fertilizer recommendation,
crop disease detection (CNN), and a RAG-based farming chatbot (Gemini + Pinecone).

## Required Space secrets (set in Space Settings → Repository secrets)

- `PINECONE_API_KEY`
- `PINECONE_ENVIRONMENT`
- `PINECONE_INDEX_NAME`
- `GEMINI_API_KEY`
- `JWT_SECRET_KEY`
- `MONGO_URL` (optional — falls back to an in-memory user store if unset)
- `ALLOWED_ORIGINS` — comma-separated list of extra allowed frontend origins,
  e.g. `https://krishimitra.vercel.app`

## API docs

Once running, visit `/docs` on this Space's URL for interactive API docs.
