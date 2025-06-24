"""
Question answering endpoints.
"""
from pathlib import Path
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.rag_engine.main import call_chatbot, stream_chatbot
import asyncio


router = APIRouter()

class Question(BaseModel):
    text: str

class Answer(BaseModel):
    answer: str

@router.post("/ask", response_model=Answer)
async def ask_question(question: Question):
    """
    Ask a medical question and get an answer using RAG.
    """
    try:
        # TODO: Implement RAG-based question answering
        result = asyncio.create_task(stream_chatbot(question=question.text))
        return Answer(
            answer="oke"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 