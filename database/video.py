import sqlite3

conn = sqlite3.connect(
    "/home/ubuntu/python/tiktok/database.db", check_same_thread=False
)

cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    file_id TEXT,
    chec INTEGER DEFAULT 2
    );
"""
)
conn.commit()


def add_video(user_id, file_id):
    cursor.execute(
        "INSERT INTO videos(user_id, file_id) VALUES (?, ?)",
        (
            user_id,
            file_id,
        ),
    )
    conn.commit()


def send_video_limit(user_id):
    cursor.execute(
        "SELECT * FROM videos WHERE user_id = ? ORDER BY id DESC LIMIT 5", (user_id,)
    )
    rows = cursor.fetchall()
    return rows


def send_video_last():
    cursor.execute("SELECT * FROM videos ORDER BY id DESC LIMIT 5")
    rows = cursor.fetchall()
    return rows


def no_watch():
    cursor.execute("SELECT * FROM videos WHERE chec = ?", (2,))
    rows = cursor.fetchall()
    return rows


def send_video(user_id):
    cursor.execute("SELECT * FROM videos WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    return rows


def find_v(file_id):
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    a = 0
    for row in rows:
        if row[2][-27:] == file_id[-27:]:
            a += 1
    if a == 0:
        return False
    else:
        return True


def video_good(file_id):
    good = find_v(file_id=file_id)
    cursor.execute("UPDATE videos SET chec = ? WHERE file_id = ?", (1, good))
    conn.commit()


def video_bad(file_id):
    bad = find_v(file_id=file_id)
    cursor.execute("UPDATE videos SET chec = ? WHERE file_id = ?", (0, bad))
    conn.commit()
