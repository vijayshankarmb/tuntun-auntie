from fastapi import APIRouter, HTTPException, status
from app.services.tasks import get_tasks_service, add_task_service, edit_task_service, delete_task_service, edit_task_complete_service
from app.schemas.tasks import TaskCreate

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.get("/")
async def get_tasks():
    return get_tasks_service()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_task(task_data: TaskCreate):
    new_task = add_task_service(task_data)
    return {"status": "success", "data": new_task}

@router.put("/{task_id}")
async def edit_task(task_id: int, task_data: TaskCreate):
    updated_task = edit_task_service(task_id, task_data)
    if updated_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return {"status": "success", "data": updated_task}

@router.put("/{task_id}/complete")
async def edit_task_complete(task_id: int, complete: bool):
    updated_task = edit_task_complete_service(task_id, complete)
    if updated_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return {"status": "success", "data": updated_task}

@router.delete("/{task_id}")
async def delete_task(task_id: int):
    deleted_task = delete_task_service(task_id)
    if not deleted_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return {"status": "success", "data": "task deleted"}
