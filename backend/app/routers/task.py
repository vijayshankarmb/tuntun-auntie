from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from app.deps.db import get_db
from app.schemas.task import (
    TaskResponse,
    TaskCreate,
    TaskTitleUpdate,
    TaskCompletedUpdate,
)
from app.services.task import (
    create_task_service,
    get_all_tasks_service,
    update_task_service,
    update_task_completed_service,
    delete_task_service
)
from app.models.user import User as UserModel
from app.deps.auth import get_current_user

router = APIRouter(
    prefix="/task",
    tags=["task"]
)

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    new_task = create_task_service(db, task_data, current_user.id)
    db.commit()
    return new_task

@router.get("/", response_model=list[TaskResponse])
def get_all_tasks(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
    ):
    tasks = get_all_tasks_service(db, current_user.id)
    db.commit()
    return tasks

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskTitleUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    updated_task = update_task_service(db, task_id, task_data, current_user.id)
    if not updated_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db.commit()
    return updated_task

@router.put("/{task_id}/completed", response_model=TaskResponse)
def update_task_completed(task_id: int, task_data: TaskCompletedUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    updated_task = update_task_completed_service(db, task_id, task_data, current_user.id)
    if not updated_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db.commit()
    return updated_task

@router.delete("/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    deleted_task = delete_task_service(db, task_id, current_user.id)
    if not deleted_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db.commit()
    return deleted_task
