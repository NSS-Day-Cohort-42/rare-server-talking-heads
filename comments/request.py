import sqlite3
import json

from models import Comment, User

def get_comments_by_post(fromThePostId):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            com.id,
            com.subject,
            com.content,
            com.user_id,
            com.post_id as PostIdentifier,
            u.user_name as UserName
        FROM Comment com
        JOIN User u on u.id = com.user_id
        WHERE com.post_id = ?   
        """, (fromThePostId,))

        comments = []

        comments_by_post = db_cursor.fetchall()

        for row in comments_by_post:
            comment = Comment(row['id'], row['subject'], row['content'], row['user_id'], row['PostIdentifier'])

            user = User('', row['UserName'], '', '', '', '', '')

            comment.user = user.__dict__

            comments.append(comment.__dict__)
    
    return json.dumps(comments)


