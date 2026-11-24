import sqlite3
from contextlib import closing

DB_NAME = "scores.db"


def init_db(db_path=DB_NAME):
    with closing(sqlite3.connect(db_path)) as conn:
        with conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS scores ("
                "user_id INTEGER PRIMARY KEY, "
                "correct INTEGER NOT NULL DEFAULT 0, "
                "total INTEGER NOT NULL DEFAULT 0)"
            )


def add_result(user_id, is_correct, db_path=DB_NAME):
    with closing(sqlite3.connect(db_path)) as conn:
        with conn:
            conn.execute(
                "INSERT OR IGNORE INTO scores (user_id) VALUES (?)",
                (user_id,),
            )
            conn.execute(
                "UPDATE scores SET total = total + 1, correct = correct + ? "
                "WHERE user_id = ?",
                (1 if is_correct else 0, user_id),
            )


def get_score(user_id, db_path=DB_NAME):
    with closing(sqlite3.connect(db_path)) as conn:
        row = conn.execute(
            "SELECT correct, total FROM scores WHERE user_id = ?",
            (user_id,),
        ).fetchone()
    return row if row else (0, 0)