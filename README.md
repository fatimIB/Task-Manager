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

# 🗄️ Week 3 — SQLite Database

This version extends the CRUD API from Assignment A1 by replacing the in-memory task list with a **SQLite database**.

The API endpoints and request/response behavior remain the same. The main change is the storage layer:

```text
A1:
Client → FastAPI → In-memory list

A2:
Client → FastAPI → SQLite database
```

Tasks are now stored in `tasks.db`, so they **persist when the server restarts**.

---

## 🛠️ Additional Technology

- SQLite
- Python `sqlite3`

SQLite is built into Python, so no additional database server or installation is required.

---

## 💾 Database

The application automatically creates:

```text
tasks.db
```

if the database file does not already exist.

It also automatically creates the `tasks` table:

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Primary key |
| `title` | TEXT | Task title |
| `done` | BOOLEAN | Completion status |

The application inserts the three example tasks **only if the table is empty**, preventing duplicate seed data when the server restarts.

---

## 📁 Updated Project Structure

```text
Task-Manager/
│
├── main.py
├── db.py
├── tasks.db
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

> `tasks.db` is created automatically when the application runs.

---

## 🔄 What Changed from A1?

The API itself did not change.

The same endpoints are still available:

```text
GET    /tasks
GET    /tasks/{id}
POST   /tasks
PUT    /tasks/{id}
DELETE /tasks/{id}
```

The difference is where the data is stored.

| A1 | A2 |
|---|---|
| Python list | SQLite database |
| Data stored in memory | Data stored in `tasks.db` |
| Data lost after restart | Data survives restart |
| Python operations | SQL queries |

This demonstrates the separation between the **API layer** and the **storage layer**.

---

# 🧪 Database CRUD

The existing cURL tests from A1 were reused to verify that the API still behaves the same with SQLite.

### Read

```bash
curl.exe -i "http://localhost:8000/tasks"
```

Returns the tasks stored in the database.

**Screenshot:**

![DB Tasks](screenshots/db-tasks.png)



### Create

```bash
curl.exe -i -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d "{\"title\":\"Buy milk\"}"
```

The new task is inserted into the SQLite database.

**Screenshot:**

![DB add](screenshots/db-add.png)

### Update

```bash
curl.exe -i -X PUT "http://localhost:8000/tasks/2" -H "Content-Type: application/json" -d "{\"title\":\"Task nbr2\",\"done\":true}"
```

The corresponding database row is updated.

**Screenshot:**

![DB update](screenshots/db-upd.png)



### Delete

```bash
curl.exe -i -X DELETE "http://localhost:8000/tasks/2"
```

The corresponding database row is deleted.

**Screenshot:**



---

# 🔁 Persistence Test

The main improvement over A1 is **persistence**.

A task can be created:

```text
POST /tasks
      ↓
Task saved in tasks.db
      ↓
Server stopped
      ↓
Server restarted
      ↓
GET /tasks
      ↓
Task still exists
```

This proves that the data is no longer stored only in application memory.

**Persistence test screenshot:**



---

# 🗃️ SQLite Database

The database was opened using **DB Browser for SQLite** to inspect the `tasks` table and its data.

**Database screenshot:**



---

# 🔎 SQL Queries

SQL queries were also executed directly against the database.

### List all tasks

```sql
SELECT * FROM tasks;
```

### Show completed tasks

```sql
SELECT * FROM tasks WHERE done = 1;
```

### Count tasks

```sql
SELECT COUNT(*) FROM tasks;
```

**SQL query screenshot:**



---

# 🔐 Parameterized Queries

Database operations use **parameterized SQL queries** instead of inserting user input directly into SQL strings.

For example:

```python
cursor.execute(
    "SELECT * FROM tasks WHERE id = ?",
    (id,)
)
```

The `?` is a parameter placeholder, and the value is supplied separately.

This helps prevent SQL injection and keeps database queries safe.

---

# 📚 What I Practiced in A2

- SQLite
- SQL queries
- Database tables and rows
- Primary keys
- Database persistence
- Parameterized queries
- Database-backed CRUD
- `sqlite3`
- DB Browser for SQLite
- Separating API and storage layers

---

## 📌 Assignment

**FlyRank Internship — Backend Track — Week 3 — Assignment A2**

**Connecting your CRUD to the database**

The original A1 CRUD API was migrated from in-memory storage to SQLite while keeping the same API endpoints and behavior.