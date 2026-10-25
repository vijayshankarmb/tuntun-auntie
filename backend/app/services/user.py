from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas.user import User
from app.models.user import User as UserModel

def signup_service(db: Session, user_data: User):
    existing_user = db.scalar(select(UserModel).where(UserModel.email == user_data.email))
    if not existing_user:
        new_user = UserModel(
            email=user_data.email,
            password=user_data.password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    return None

def signin_service(db: Session, user_data: User):
    user = db.scalar(select(UserModel).where(UserModel.email == user_data.email))
    if user and user.password == user_data.password:
        return user
    return None
