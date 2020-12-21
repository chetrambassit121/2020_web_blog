from common.database import Database
from models.posts import Post
import uuid
import datetime


class Blog(object):
    def __init__(self, author, title, description, author_id, _id=None):
        self.author = author
        self.title = title
        self.description = description
        self.author_id = author_id
        self._id = _id or uuid.uuid4().hex

    def json(self):
        return {
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "author_id": self.author_id,
            "_id": self._id
        }

    def save_to_mongo(self):
        Database.insert(collection="blogs", data=self.json())

