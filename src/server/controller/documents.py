"""
Health check endpoints.
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/upload")
async def document_processing():
    """
    Health check endpoint.
    """
    return {"status": "healthy"} 