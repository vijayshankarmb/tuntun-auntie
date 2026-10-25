from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.deps.db import get_db
from app.schemas.user import AuthResponse, User

from app.services.user import (
    signup_service,
    signin_service
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/signup", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)   
def signup(user_data: User, db: Session = Depends(get_db)):
    user = signup_service(db, user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists."
        )
    return user

@router.post("/signin", response_model=AuthResponse)
def signin(user_data: User, db: Session = Depends(get_db)):
    user = signin_service(db, user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="email or password is incorrect"
        )
    return user

