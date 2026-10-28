from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.task import router as task_router
from app.routers.user import router as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)
app.include_router(user_router)

@app.get("/health")
def read_health():
    return {"status": "healthy"}

