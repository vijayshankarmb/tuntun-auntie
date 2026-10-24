from fastapi import FastAPI
from app.routers.task import router

app = FastAPI()

app.include_router(router)

@app.get("/health")
def read_health():
    return {"status": "healthy"}

