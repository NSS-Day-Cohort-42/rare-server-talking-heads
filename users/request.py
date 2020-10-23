import sqlite3
import json
from models import User

def create_user(new_user):
    with sqlite3.connect("./rare.db") as conn
    db_cursor = conn.cursor()

    db_cursor.execute("""
    INSERT INTO User
        ( user_name, email, password, first_name, last_name, bio )
    """)