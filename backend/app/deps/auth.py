import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta, timezone
from fastapi import Cookie, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from jwt.exceptions import InvalidTokenError
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from app.deps.db import get_db
from app.models.user import User as UserModel

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

ph = PasswordHasher()

def create_access_token(user_id: int):
    expiration = datetime.now(timezone.utc) + timedelta(hours=1)
    payload = {
        "sub": str(user_id),
        "exp": expiration
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def get_current_user(
        access_token: str | None = Cookie(default=None),
        db: Session = Depends(get_db)
):
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token is missing"
        )
    try:
        payload = jwt.decode(
            access_token, 
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        user_id = int(payload.get("sub"))
    except (InvalidTokenError, KeyError, TypeError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    user = db.scalar(select(UserModel).where(UserModel.id == user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user

def hash_password(password: str):
    return ph.hash(password)

def verify_password(hashed_password: str, plain_password: str):
    try:
        return ph.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        return False

