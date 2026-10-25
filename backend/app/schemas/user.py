from pydantic import BaseModel

class AuthResponse(BaseModel):
    id: int
    email: str
    password: str

class User(BaseModel):
    email: str
    password: str