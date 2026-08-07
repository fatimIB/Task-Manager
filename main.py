from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

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


@app.get("/")
def hello():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }


@app.get("/health")
def health():
    return { "status": "ok" }


@app.get("/tasks")
def get_tasks():
    return memory

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
    new_id = len(memory) + 1
    new_task = {
        "id": new_id,
        "title": task.title,
        "done": False
    }
    memory.append(new_task)
    return new_task
