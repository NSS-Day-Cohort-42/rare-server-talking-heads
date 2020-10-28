import sqlite3
import json

from models import Comment

def update_comment(id, subject, content):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comment
        SET
        subject = ?,
        content = ?,
        WHERE id = ?
        """, (subject, content, id))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True