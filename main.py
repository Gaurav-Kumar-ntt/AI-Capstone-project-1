from fastapi import FastAPI
from pydantic import BaseModel

from ai_pipeline import ai_pipeline

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AI Capstone API Running 🚀"}


@app.post("/ask")
def ask(request: QuestionRequest):
    answer = ai_pipeline(request.question)
    return {
        "question": request.question,
        "answer": answer
    }