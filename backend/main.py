from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import QueryRequest
from ai_service import generate_sql

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def health():

    return {
        "status": "running"
    }


@app.post("/generate-sql")
def create_sql(
    request: QueryRequest
):

    sql = generate_sql(
        request.question
    )

    return {
        "generated_sql": sql
    }