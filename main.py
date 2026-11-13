# main.py

from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Policy Assistant"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Policy Assistant Running"
    }