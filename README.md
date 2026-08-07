# Task Manager API

A simple **REST API** built with **Python and FastAPI** to manage a to-do list.

This project was developed for the **FlyRank Internship — Backend Track — Week 2 — Assignment A1: Build Your First CRUD API**.

The API implements the four CRUD operations:

- **Create** — POST
- **Read** — GET
- **Update** — PUT
- **Delete** — DELETE

Tasks are stored **in memory**, so they are reset when the server restarts.

---

## 🛠️ Technologies

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI / OpenAPI
- cURL
- Git & GitHub

---

## 📁 Project Structure

```text
Task-Manager/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

---

## ⚙️ Installation & Running

### 1. Clone the repository

```bash
git clone https://github.com/fatimIB/Task-Manager
cd Task-Manager
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the server

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://localhost:8000
```

---

# 🔌 API Endpoints

| Method | Endpoint | Description | Status |
|---|---|---|---|
| GET | `/` | API information | 200 |
| GET | `/health` | Health check | 200 |
| GET | `/tasks` | Get all tasks | 200 |
| GET | `/tasks/{id}` | Get one task | 200 / 404 |
| POST | `/tasks` | Create a task | 201 / 400 |
| PUT | `/tasks/{id}` | Update a task | 200 / 400 / 404 |
| DELETE | `/tasks/{id}` | Delete a task | 204 / 404 |

### Optional feature

```text
GET /tasks?done=true
GET /tasks?done=false
```

These endpoints filter tasks by their completion status.

---

# 🧪 cURL Testing

The API was tested using **cURL** with the required HTTP status codes.

## GET all tasks

```bash
curl.exe -i "http://localhost:8000/tasks"
```

**Screenshot:**

![GET all tasks](screenshots/get-tasks.png)

---

## GET task by ID

```bash
curl.exe -i "http://localhost:8000/tasks/1"
```

**Screenshot:**

![GET task](screenshots/get-id.png)

### Task not found

```bash
curl.exe -i "http://localhost:8000/tasks/99"
```

Returns `404 Not Found`.

![GET 404](screenshots/notfound.png)

---

## POST create task

```bash
curl.exe -i -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d "{\"title\":\"Buy milk\"}"
```

Returns `201 Created`.

![POST task](screenshots/add.png)

### Invalid task

```bash
curl.exe -i -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d "{}"
```

Returns `400 Bad Request`.

![POST validation](screenshots/bad_req.png)

---

## PUT update task

```bash
curl.exe -i -X PUT "http://localhost:8000/tasks/2" -H "Content-Type: application/json" -d "{\"title\":\"Task nbr2\",\"done\":true}"
```

Returns `200 OK`.

![PUT task](screenshots/curl-put-task.png)

---

## DELETE task

```bash
curl.exe -i -X DELETE "http://localhost:8000/tasks/2"
```

Returns `204 No Content`.

![DELETE task](screenshots/curl-delete-task.png)

### Task not found

```bash
curl.exe -i -X DELETE "http://localhost:8000/tasks/44"
```

Returns `404 Not Found`.

![DELETE task not found](screenshots/curl-delete-notfound.png)

---

# 📚 Swagger UI Testing

FastAPI automatically generates interactive API documentation using **Swagger UI**.

Open:

```text
http://localhost:8000/docs
```

Swagger UI allows the complete CRUD cycle to be tested using **Try it out** without cURL.

### Swagger UI

![Swagger UI](screenshots/swagger.png)

### Create task

![Swagger POST](screenshots/swagger-post.png)

### Read tasks

![Swagger GET](screenshots/swagger-get.png)

### Update task

![Swagger PUT](screenshots/swagger-put.png)

### Delete task

![Swagger DELETE](screenshots/swagger-delete.png)

---

# 📊 HTTP Status Codes

| Code | Meaning | Usage |
|---|---|---|
| `200` | OK | Successful GET / PUT |
| `201` | Created | Task successfully created |
| `204` | No Content | Task successfully deleted |
| `400` | Bad Request | Invalid task data |
| `404` | Not Found | Task does not exist |

---

# 💾 Data Storage

Tasks are stored in an **in-memory Python list**.

Therefore, all tasks are lost when the server is restarted.

No database is used in this assignment.

---

# 🎯 What I Practiced

- REST APIs
- HTTP methods
- CRUD operations
- FastAPI routing
- Path parameters
- Query parameters
- Pydantic validation
- HTTP status codes
- Error handling
- Swagger UI / OpenAPI
- cURL
- Git & GitHub

---

## 📌 Assignment

**FlyRank Internship — Backend Track — Week 2 — Assignment A1**

**Build Your First CRUD API**