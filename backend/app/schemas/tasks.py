from pydantic import BaseModel, Field

class Tasks(BaseModel):
    id: int
    title: str = Field(min_length=1)
    completed: bool = Field(default=False)

class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = Field(default=False)

