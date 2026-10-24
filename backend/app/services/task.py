from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas.task import TaskCreate, TaskTitleUpdate, TaskCompletedUpdate
from app.models.task import Task

def create_task_service(db: Session, task_data: TaskCreate):
    new_task = Task(
        title =  task_data.title
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_all_tasks_service(db: Session):
    statement = select(Task)
    tasks = db.scalars(statement).all()
    return tasks

def update_task_service(db: Session, task_id: int, task_data: TaskTitleUpdate):
    task = db.get(Task, task_id)
    if not task:
        return None
    task.title = task_data.title
    db.commit()
    db.refresh(task)
    return task

def update_task_completed_service(db: Session, task_id: int, task_data: TaskCompletedUpdate):
    task = db.get(Task, task_id)
    if not task:
        return None
    task.completed = task_data.completed
    db.commit()
    db.refresh(task)
    return task

def delete_task_service(db: Session, task_id: int):
    task = db.get(Task, task_id)
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task

