import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "attendance.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )"""
    )
    conn.commit()
    conn.close()


def add_attendance(student_id: str, timestamp: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO attendance (student_id, timestamp) VALUES (?, ?)",
        (student_id, timestamp),
    )
    conn.commit()
    conn.close()
