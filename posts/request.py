import sqlite3
import json

from models import Post

def get_all_posts():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        db_cursor.execute("""
        SELECT
            p.id,
            p.title,
            p.content,
            p.pubdate,
            p.header_img,
            p.user_id,
            p.category_id
        FROM Post p
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['title'], row['content'], row['pubdate'], row['header_img'], row['user_id'], row['category_id'])

            posts.append(post.__dict__)
        
    return json.dumps(posts)