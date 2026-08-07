from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import db

app = FastAPI()


memory=[
    {
        "id": 1,
        "title": "Task nbr1",
        "done": True
    },
    {
        "id": 2,
        "title": "Task nbr2",
        "done": False
    },
    {
        "id": 3,
        "title": "Task nbr3",
        "done": False
    }
]


class TaskCreate(BaseModel):
    title: str | None = None
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


@app.get("/")
def hello():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }


@app.get("/health")
def health():
    return { "status": "ok" }


@app.get("/tasks")
def get_tasks(done: bool | None = None):
    if done is None:
        return memory

    return [task for task in memory if task["done"] == done]

@app.get("/tasks/{id}")
def get_tasks_by_id(id: int):
    for task in memory :
        if task["id"]==id :
            return task

    return JSONResponse(
        status_code=404,
        content={"error": f"Task {id} not found"}
    )

@app.post("/tasks", status_code=201)
def add_task(task: TaskCreate):
    
    if task.title is None or task.title.strip() == "":
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required"}
        )
    new_id = max(task["id"] for task in memory) + 1
    new_task = {
        "id": new_id,
        "title": task.title,
        "done": False
    }
    memory.append(new_task)
    return new_task

@app.put("/tasks/{id}")
def update(id: int, task_update : TaskUpdate):
    for task in memory :
        if task["id"]==id :
            if task_update.title is None and task_update.done is None:
                return JSONResponse(
                    status_code=400,
                    content={"error": "No fields to update"}
                )

            if task_update.title is not None:
                if not task_update.title.strip():
                    return JSONResponse(
                        status_code=400,
                        content={"error": "Title is required"}
                    )

                task["title"] = task_update.title

            if task_update.done is not None:
                task["done"] = task_update.done

            return task
    return JSONResponse(
        status_code=404,
        content={"error": f"Task {id} not found"}
    )

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):

    for i, task in enumerate(memory):
        if task["id"] == id:
            memory.pop(i)
            return

    return JSONResponse(
        status_code=404,
        content={"error": f"Task {id} not found"}
    )