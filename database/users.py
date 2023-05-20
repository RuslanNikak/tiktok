import sqlite3

conn = sqlite3.connect(
    "/home/ubuntu/python/tiktok/database.db", check_same_thread=False
)

cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   user_id INTEGER REFERENCES videos (user_id),
   username TEXT,
   first_name TEXT,
   last_name TEXT,
   language_code TEXT,
   date DATETIME DEFAULT CURRENT_TIMESTAMP
   );
"""
)
conn.commit()


def find_id(user_id):
    result = cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return bool(result.fetchall())


def add_users(user_id, username, first_name, last_name, language_code):
    cursor.execute(
        "INSERT INTO users (user_id, username, first_name, last_name, language_code) VALUES (?, ?, ?, ?, ?)",
        (
            user_id,
            username,
            first_name,
            last_name,
            language_code,
        ),
    )
    conn.commit()


def send_user(user_id):
    result = cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return result


def send_users():
    data = cursor.execute(
        "SELECT id, user_id, username, first_name, last_name, language_code FROM users;"
    )
    return data
