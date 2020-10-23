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
            u.user_name,
            p.user_id,
            c.name AS category_name,
            p.category_id
        FROM Post p
        JOIN User u ON u.id = p.user_id
        JOIN Category c ON c.id = p.category_id;
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['title'], row['content'], row['pubdate'], row['header_img'], row['user_name'], row['user_id'], row['category_name'], row['category_id'])

            posts.append(post.__dict__)
        
    return json.dumps(posts)