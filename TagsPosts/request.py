import sqlite3
import json
from models import TagPost

def get_tagPosts():
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            tp.id,
            tp.tag_id,
            tp.post_id,
            t.name
        FROM TagPost tp
        JOIN Tag t ON t.id = tp.tag_id;
        """)

        tagPosts = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            tagPost = TagPost(row['id'], row['tag_id'], row['post_id'], row['name'])
            tagPosts.append(tagPost.__dict__)
        
    return json.dumps(tagPosts)

def create_tagPost(new_tagPost):
    with sqlite3.connect("./rare.db") as conn:

        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO TagPost
            ( tag_id, post_id )
        VALUES
            ( ?, ? );
        """, (new_tagPost['tag_id'], new_tagPost['post_id'], ))
        
        id = db_cursor.lastrowid

        new_tagPost['id'] = id
    
    return json.dumps(new_tagPost)
