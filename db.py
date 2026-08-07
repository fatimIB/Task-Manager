import sqlite3

DATABASE = "tasks.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def init_db():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def seed_db():
    connection = get_connection()

    cursor = connection.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    if count == 0:
        connection.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            [
                ("Task nbr1", True),
                ("Task nbr2", False),
                ("Task nbr3", False)
            ]
        )

    connection.commit()
    connection.close()


init_db()
seed_db()