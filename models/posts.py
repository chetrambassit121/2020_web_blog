from common.database import Database
import uuid
import datetime

class Post(object):
    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = _id or uuid.uuid4().hex

    def json(self):
        return {
            "blog_id": self.blog_id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "created_date": self.created_date,
            "_id": self._id
        }

    def save_to_mongo(self):
        Database.insert(collection="posts", data=self.json())

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection="posts", query={"_id": id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection="posts", query={"blog_id": id})]