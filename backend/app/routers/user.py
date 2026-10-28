import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.deps.db import get_db
from app.schemas.user import User
from app.deps.auth import create_access_token

from app.services.user import (
    signup_service,
    signin_service
)

load_dotenv()

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/signup", status_code=status.HTTP_201_CREATED)   
def signup(user_data: User, response: Response, db: Session = Depends(get_db)):
    user = signup_service(db, user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists."
        )
    token = create_access_token(user.id)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=True if os.getenv("ENVIRONMENT") == "production" else False,
        samesite="lax" if os.getenv("ENVIRONMENT") == "development" else "strict",
        max_age=3600,
        path="/"
    )
    db.commit()
    return {"detail": "Successfully signed in"}

@router.post("/signin", status_code=status.HTTP_200_OK)
def signin(user_data: User,response: Response, db: Session = Depends(get_db)):
    user = signin_service(db, user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="email or password is incorrect"
        )
    token = create_access_token(user.id)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=True if os.getenv("ENVIRONMENT") == "production" else False,
        samesite="lax" if os.getenv("ENVIRONMENT") == "development" else "strict",
        max_age=3600,
        path="/"
    )
    return {"detail": "Successfully signed in"}

@router.post("/signout", status_code=status.HTTP_200_OK)
def signout(response: Response):
    response.delete_cookie(
        key="access_token",
        path="/"
    )
    return {"detail": "Successfully signed out"}

