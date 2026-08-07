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
def get_tasks():
    connection = db.get_connection()

    cursor = connection.execute(
        "SELECT id, title, done FROM tasks"
    )

    rows = cursor.fetchall()

    connection.close()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "done": bool(row[2])
        })

    return tasks

@app.get("/tasks/{id}")
def get_task_by_id(id: int):
    connection = db.get_connection()

    cursor = connection.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",
        (id,)
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {id} not found"}
        )

    return {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2])
    }

@app.post("/tasks", status_code=201)
def add_task(task: TaskCreate):

    if task.title is None or task.title.strip() == "":
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required"}
        )

    connection = db.get_connection()

    cursor = connection.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (task.title, False)
    )

    connection.commit()

    new_id = cursor.lastrowid

    connection.close()

    return {
        "id": new_id,
        "title": task.title,
        "done": False
    }
@app.put("/tasks/{id}")
def update_task(id: int, task: TaskUpdate):

    if task.title is None and task.done is None:
        return JSONResponse(
            status_code=400,
            content={"error": "No fields to update"}
        )

    if task.title is not None and not task.title.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required"}
        )

    connection = db.get_connection()

    existing_task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (id,)
    ).fetchone()

    if existing_task is None:
        connection.close()
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {id} not found"}
        )

    new_title = task.title if task.title is not None else existing_task["title"]
    new_done = task.done if task.done is not None else existing_task["done"]

    connection.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (new_title, new_done, id)
    )

    connection.commit()

    updated_task = {
        "id": id,
        "title": new_title,
        "done": new_done
    }

    connection.close()

    return updated_task

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