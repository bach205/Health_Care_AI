"""
Question answering endpoints.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Question(BaseModel):
    text: str

class Answer(BaseModel):
    answer: str
    sources: list[str]

@router.post("/ask", response_model=Answer)
async def ask_question(question: Question):
    """
    Ask a medical question and get an answer using RAG.
    """
    try:
        # TODO: Implement RAG-based question answering
        return Answer(
            answer="This is a placeholder answer.",
            sources=["Source 1", "Source 2"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 