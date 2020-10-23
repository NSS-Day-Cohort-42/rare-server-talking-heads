import sqlite3
import json
from models import User

def create_user(new_user):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO User
            ( user_name, email, password, first_name, last_name, bio )
        VALUES
            ( ?, ?, ?, ?, ?, ? );
        """, ( new_user['user_name'], new_user['email'],
                new_user['password'], new_user['first_name'],
                new_user['last_name'], new_user['bio'], ))

        # The `lastrowid` property on the cursor will return the 
        # primary key of the last thing added to the db
        id = db_cursor.lastrowid

        # Add the id property to the new user that was created
        new_user['id'] = id
    return json.dumps(new_user)