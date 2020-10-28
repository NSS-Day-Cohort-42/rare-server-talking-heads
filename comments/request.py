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


def create_comment(new_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO comment
            (subject, content, user_id, post_id)
        VALUES
            (?,?,?,?)
        """,(new_comment['subject'], new_comment['content'], new_comment['user_id'], new_comment['post_id']))

        id = db_cursor.lastrowid

        new_comment['id'] = id

    return json.dumps(new_comment)


def delete_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM comment
        WHERE id = ?
        """, (id,))


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

def get_single_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
        SELECT
        c.id,
        c.subject,
        c.content,
        c.user_id,
        u.user_name,
        c.post_id,
        p.title
        FROM Comment C
        JOIN User u ON u.id = c.user_id
        JOIN Post p ON p.id = c.post_id
        WHERE c.id = ?
        """, (id,))

        data = db_cursor.fetchone()

        comment = Comment(data['id'], data['subject'], data['content'], data['user_id'], data['user_name'], data['post_id'], data['title'])

    return json.dumps(comment.__dict__)