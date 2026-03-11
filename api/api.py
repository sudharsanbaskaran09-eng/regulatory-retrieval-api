from fastapi import FastAPI
from pydantic import BaseModel
from api.ask import ask_question

app = FastAPI(title="Regulatory Document Retrieval API")


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Regulatory Retrieval API Running"}


@app.post("/ask")
def ask_api(request: QuestionRequest):
    answer = ask_question(request.question)

    return {
        "question": request.question,
        "answer": answer
    }