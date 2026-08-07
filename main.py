from fastapi import FastAPI
from fastapi.responses import JSONResponse

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