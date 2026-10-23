
tasks = [
    {"id": 1, "title": "Task 1", "completed": False},
    {"id": 2, "title": "Task 2", "completed": True},
    {"id": 3, "title": "Task 3", "completed": False},
    {"id": 4, "title": "Task 4", "completed": True},
]

def get_tasks_service():
    return tasks

def add_task_service(task_data):
    new_task = {
        "id": len(tasks)+1,
        "title": task_data.title,
        "completed": task_data.completed
    }
    tasks.append(new_task)
    return new_task

def edit_task_service(task_id, task_data):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_data.title
            return task
    return None

def edit_task_complete_service(task_id, complete):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = complete
            return task
    return None

def delete_task_service(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False
        