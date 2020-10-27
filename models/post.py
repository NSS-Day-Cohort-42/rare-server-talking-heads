from datetime import datetime

class Post():
    def __init__(self, id, title, content, pubdate, header_img, user_name, user_id, category_name, category_id):
        self.id = id
        self.title = title
        self.content = content
        self.pubdate = datetime.fromtimestamp(pubdate/1000.0).strftime("%m/%d/%Y")
        self.header_img = header_img
        self.user_name = user_name
        self.user_id = user_id
        self.category_name = category_name
        self.category_id = category_id