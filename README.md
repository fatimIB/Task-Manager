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

![DB update](screenshots/db-delete.png)


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
---

## 🔎 SQL Queries

SQL queries were also executed directly against the database.

### List all tasks

```sql
SELECT * FROM tasks;
```

![DB browser](screenshots/db-bros-tasks.png)

### Show completed tasks

```sql
SELECT * FROM tasks WHERE done = 1;
```
![DB browser](screenshots/db-com-tsks.png)


### Count tasks

```sql
SELECT COUNT(*) FROM tasks;
```

![DB browser](screenshots/db-counts.png)

### Mark as complete

```sql
UPDATE tasks SET done = 1;
```

![DB browser](screenshots/db-ascomp.png)

### Delete completed tasks

```sql
DELETE FROM tasks WHERE done = 1;    
```

![DB browser](screenshots/db-delall.png)


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


# Week 3 — Assignment A3: Containerize Your Stack

**FlyRank Internship · Backend Track · Week 3 · Assignment A3**

In A2, the API used SQLite, where the database was stored in a local `tasks.db` file.

In A3, the storage is being migrated to **PostgreSQL running inside Docker**. The database uses a Docker volume so that its data can persist independently from the container.

### 1. Verify Docker

```cmd
docker --version
```

**Screenshot:**

![verify docker](screenshots/verif-docker.png)


### 2. Start PostgreSQL in Docker

```cmd
docker run --name taskdb -e POSTGRES_PASSWORD=dev -e POSTGRES_DB=tasks -p 5432:5432 -v taskdata:/var/lib/postgresql -d postgres
```

This starts PostgreSQL with:

- Database: `tasks`
- Container: `taskdb`
- Port: `5432`
- Persistent volume: `taskdata`

> The assignment uses `/var/lib/postgresql/data`, but the current PostgreSQL 18+ Docker image requires `/var/lib/postgresql`.

**Screenshot:**

![Postges](screenshots/postg.png)


### 3. Check the Running Container

```cmd
docker ps
```

**Screenshot:**
![Postges run](screenshots/post-run.png)



### 4. Connect to the Database

```cmd
docker exec -it taskdb psql -U postgres -d tasks
```

**Screenshot:**

![Postges run](screenshots/postg-connect.png)


### 5. Install the PostgreSQL Driver

The Python PostgreSQL driver and environment-variable loader were installed:

```cmd
pip install "psycopg[binary]" python-dotenv
```

### 6. Configure the Database Connection

A `.env` file was created to store the PostgreSQL connection string:

```env
DATABASE_URL=postgresql://postgres:dev@localhost:5432/tasks
```

The `.env` file is ignored by Git so that the database credentials are not committed.

A `.env.example` file was also created with a placeholder password:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/tasks
```

### 7. Connect the Application to PostgreSQL

The database module was changed from SQLite to PostgreSQL using `psycopg`.

The application now reads the `DATABASE_URL` from `.env` and connects to the PostgreSQL container.

The `tasks` table is created automatically if it does not already exist.

```text
A2:
FastAPI → SQLite → tasks.db

A3:
FastAPI → PostgreSQL → Docker
```


### 8. Start the FastAPI Application

The API was started with:

```cmd
uvicorn main:app --reload
```

The application successfully starts and connects to the PostgreSQL database.

```cmd
PS C:\Users\hp\Desktop\FlyRank assignment\Task Manager> uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['C:\\Users\\hp\\Desktop\\FlyRank assignment\\Task Manager']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [17932] using WatchFiles
INFO:     Started server process [34080]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 9. Check the Database Table

The PostgreSQL database was opened from inside the Docker container:

```cmd
docker exec -it taskdb psql -U postgres -d tasks
```

Then the tables were checked with:

```sql
\dt
```

The `tasks` table is created automatically by the application.

The application inserts three example tasks when the `tasks` table is empty.

They can be checked directly from PostgreSQL:

```cmd
docker exec -it taskdb psql -U postgres -d tasks -c "SELECT * FROM tasks;"
```

The database contains the three initial tasks.

**Screenshot:**

![Postges](screenshots/post-ins.png)

