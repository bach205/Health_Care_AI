"""
Configuration settings for the RAG engine.
"""

from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
VECTOR_STORE_DIR = BASE_DIR / "vector_store"

# Model settings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "gpt2"  # Replace with your preferred model

# Vector store settings
VECTOR_STORE_TYPE = "faiss"
VECTOR_STORE_PATH = VECTOR_STORE_DIR / "faiss_index"

# RAG settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K_RESULTS = 3 