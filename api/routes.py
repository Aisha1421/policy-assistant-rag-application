# api/routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from services.rag_service import ask_question

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/ask")
def query_policy(request: Query):
    return ask_question(
        request.question
    )
