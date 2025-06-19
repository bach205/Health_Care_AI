"""
Main FastAPI server for the medical RAG application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .endpoints import qa, health

app = FastAPI(
    title="Medical RAG API",
    description="API for medical question answering using RAG",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(qa.router, prefix="/api/v1", tags=["QA"])
app.include_router(health.router, prefix="/api/v1", tags=["Health"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 