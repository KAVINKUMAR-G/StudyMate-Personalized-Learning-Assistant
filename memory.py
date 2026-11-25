
from contextlib import contextmanager
import sqlite3
from datetime import datetime, timezone


class StudyMemory:
    def __init__(self, db_path="studymate.db"):
        self.db_path = db_path
        self._initialize()

    @contextmanager
    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _initialize(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS profile (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at TEXT NOT NULL,
                    activity_type TEXT NOT NULL,
                    topic TEXT NOT NULL,
                    details TEXT NOT NULL,
                    score REAL NOT NULL
                )
            """)

    def save_profile(self, key, value):
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO profile(key, value) VALUES(?, ?) "
                "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                (str(key), str(value))
            )

    def get_profile(self, key, default=""):
        with self._connect() as conn:
            row = conn.execute(
                "SELECT value FROM profile WHERE key=?", (str(key),)
            ).fetchone()
        return row[0] if row else default

    def add_activity(self, activity_type, topic, details, score=0.0):
        stamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO activities(created_at, activity_type, topic, details, score) "
                "VALUES(?, ?, ?, ?, ?)",
                (stamp, str(activity_type), str(topic), str(details), float(score))
            )

    def get_activities(self, limit=100):
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT created_at, activity_type, topic, details, score "
                "FROM activities ORDER BY id DESC LIMIT ?", (int(limit),)
            ).fetchall()
        return [
            {"created_at": r[0], "activity_type": r[1], "topic": r[2],
             "details": r[3], "score": round(r[4], 3)}
            for r in rows
        ]

    def get_topic_stats(self):
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT topic, COUNT(*) FROM activities GROUP BY topic ORDER BY COUNT(*) DESC"
            ).fetchall()
        return {topic: count for topic, count in rows}

    def clear_all(self):
        with self._connect() as conn:
            conn.execute("DELETE FROM profile")
            conn.execute("DELETE FROM activities")
