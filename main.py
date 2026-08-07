from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import db

app = FastAPI()



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

    cursor = connection.cursor()
    cursor.execute(
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
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, title, done FROM tasks WHERE id = %s",
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
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, done) VALUES (%s, %s) RETURNING *",
        (task.title, False)
    )

    row = cursor.fetchone()

    connection.commit()
    connection.close()

    return {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2])
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
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, title, done FROM tasks WHERE id = %s",
        (id,)
    )

    existing_task = cursor.fetchone()

    if existing_task is None:
        connection.close()
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {id} not found"}
        )

    new_title = task.title if task.title is not None else existing_task[1]
    new_done = task.done if task.done is not None else existing_task[2]

    cursor.execute(
        """
        UPDATE tasks
        SET title = %s, done = %s
        WHERE id = %s
        RETURNING *
        """,
        (new_title, new_done, id)
    )

    row = cursor.fetchone()

    connection.commit()
    connection.close()

    return {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2])
    }

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):

    connection = db.get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id FROM tasks WHERE id = %s",
        (id,)
    )

    existing_task = cursor.fetchone()

    if existing_task is None:
        connection.close()
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {id} not found"}
        )

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (id,)
    )

    connection.commit()
    connection.close()

    return