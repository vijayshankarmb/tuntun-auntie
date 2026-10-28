from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.schemas.user import User
from app.models.user import User as UserModel
from app.deps.auth import hash_password, verify_password

def signup_service(db: Session, user_data: User):
    existing_user = db.scalar(select(UserModel).where(UserModel.email == user_data.email))
    if not existing_user:
        hashed_password = hash_password(user_data.password)
        new_user = UserModel(
            email=user_data.email,
            password=hashed_password
        )
        try:
            db.add(new_user)
            db.flush()
            db.refresh(new_user)
            return new_user
        except IntegrityError:
            db.rollback()
            return None
    return None

def signin_service(db: Session, user_data: User):
    user = db.scalar(select(UserModel).where(UserModel.email == user_data.email))
    if user:
        is_valid = verify_password(user.password, user_data.password)
        if is_valid:
            return user
    return None
