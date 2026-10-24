from pydantic import BaseModel, Field, ConfigDict

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    completed: bool

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)

class TaskTitleUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=255)

class TaskCompletedUpdate(BaseModel):
    completed: bool
