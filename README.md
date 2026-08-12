# Krishi Mitra - Smart Agriculture Assistant

Krishi Mitra is a full-stack agricultural assistant application featuring artificial intelligence powered Retrieval-Augmented Generation (RAG), crop prediction, plant disease detection, fertilizer recommendation, weather forecasting, and multilingual interface support.

## Deployed Applications

* **Frontend Client (Vercel)**: https://krishimitra-agritech.vercel.app
* **Backend API (Render)**: https://krishimitra-server.onrender.com
* **API Documentation (Swagger)**: https://krishimitra-server.onrender.com/docs

## Technology Stack

### Frontend
* React (TypeScript)
* Vite (Build Tool)
* Tailwind CSS (Styling)
* Shadcn UI (Component Library)
* i18next (Internationalization)

### Backend
* FastAPI (Python web framework)
* MongoDB (User profile and session database)
* Pinecone (Vector database for RAG context)
* Google Gemini API (LLM for generation)
* TensorFlow / PyTorch (ML models for crop disease detection and classification)

## Project Structure

* `backend/` - Contains the Python FastAPI codebase, endpoints, routers, database schemas, and ML inference services.
* `frontend/` - Contains the React TypeScript single-page application and localization configurations.

## Prerequisites

* Python 3.11
* Node.js 18+ and npm
* MongoDB instance (Local or MongoDB Atlas)
* Pinecone database account
* Google Gemini API Key
* OpenWeatherMap API Key

## Local Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .\.venv\Scripts\Activate.ps1
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. Install required Python packages:
   ```bash
   python -m pip install --upgrade pip setuptools wheel
   python -m pip install -r requirements.txt
   ```

4. Create a `.env` file in the `backend/` directory using the configuration keys listed in the Configuration section below.

5. Run the development server:
   ```bash
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the Vite development server:
   ```bash
   npm run dev
   ```

## Configuration

The backend application requires the following environment variables. Create a `.env` file in the `/backend` folder with these keys:

```dotenv
# MongoDB Configuration
MONGO_URL=your_mongodb_connection_string

# Authentication Security
JWT_SECRET=your_jwt_secret_key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

# Vector Database (Pinecone)
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_region
PINECONE_INDEX_NAME=krishimitra-knowledge

# Embeddings Model Configuration
EMBEDDING_MODEL_NAME=sentence-transformers/all-mpnet-base-v2
EMBEDDING_DIMENSION=768

# Large Language Model Configuration
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.0-flash-exp

# Retrieval Parameters
DEFAULT_TOP_K=5
MAX_TOP_K=20
MAX_TOKENS=1000
TEMPERATURE=0.7

# Weather Integration
OPENWEATHER_API_KEY=your_openweather_api_key

# Execution Options
GRAPH_TIMEOUT=30
ENABLE_GRAPH_LOGGING=true
LOG_LEVEL=INFO
```

For frontend deployments, set the following environment variable to override the default local backend URL:

```dotenv
VITE_API_BASE=https://krishimitra-server.onrender.com
```

## License

This project is licensed under the MIT License.
