"""
Embedding service for query vectorization
"""
import time
from typing import List

from core.config import get_settings
from core.logging import get_logger

logger = get_logger(__name__)
settings = get_settings()


class EmbeddingService:
    """Handles text embedding using SentenceTransformers"""

    def __init__(self):
        self.model = None
        self.initialized = False
        # NOTE: the actual model load (and the sentence-transformers/torch
        # import) is deferred to first use in _ensure_loaded(), not done here.
        # This means importing this module — and therefore the whole RAG
        # router, and therefore the whole FastAPI app — no longer requires
        # torch/sentence-transformers to be installed and working. Only the
        # RAG endpoints themselves need it, and they'll fail with a clear
        # error instead of preventing the entire backend from starting.

    def _ensure_loaded(self):
        """Load the embedding model on first use, not at import time."""
        if self.model is not None:
            return
        try:
            from sentence_transformers import SentenceTransformer  # heavy import, deferred on purpose
        except Exception as e:
            logger.error(f"sentence-transformers/torch is not available: {e}")
            raise RuntimeError(
                "The embedding model dependencies (torch / sentence-transformers) "
                "are not available in this environment. Install them (see "
                "requirements.txt) to use the RAG endpoints."
            ) from e

        try:
            logger.info(f"Loading embedding model: {settings.embedding_model_name}")
            self.model = SentenceTransformer(settings.embedding_model_name)
            self.initialized = True
            logger.info(f"Embedding model loaded successfully. Dimension: {self.model.get_sentence_embedding_dimension()}")
        except Exception as e:
            logger.error(f"Failed to initialize embedding model: {e}")
            self.model = None
            self.initialized = False
            raise

    def embed_query(self, query: str) -> tuple[List[float], float]:
        """
        Generate embeddings for a query string
        
        Args:
            query: Input query string
            
        Returns:
            Tuple of (embedding vector, latency in ms)
        """
        self._ensure_loaded()
        try:
            start_time = time.time()
            
            # Generate embeddings
            embeddings = self.model.encode([query])
            embedding_vector = embeddings[0].tolist()
            
            latency_ms = (time.time() - start_time) * 1000
            
            logger.log_node_execution(
                node_name="EmbedNode",
                latency_ms=latency_ms,
                metadata={"query_length": len(query), "embedding_dim": len(embedding_vector)}
            )
            
            return embedding_vector, latency_ms
            
        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            raise
    
    def get_dimension(self) -> int:
        """Get embedding dimension"""
        self._ensure_loaded()
        return self.model.get_sentence_embedding_dimension()


# Global embedding service instance — safe to construct even without
# torch/sentence-transformers installed; the heavy work happens lazily.
embedding_service = EmbeddingService()

