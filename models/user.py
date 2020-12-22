from common.database import Database
from models.blog import Blog
from flask import session
import uuid


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = _id or uuid.uuid4().hex

    def json(self):
        return {
            "email": self.email,
            "password": self.password,
            "_id": self._id
        }

    def save_to_mongo(self):
        Database.insert(collection="users", data=self.json())

    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def new_blog(self, title, description):
        blog = Blog(author=self.email,
                    title=title,
                    description=description,
                    author_id=self._id)
        blog.save_to_mongo()

    @classmethod
    def get_by_email(cls, email):
        email_data = Database.find_one(collection="users", query={"email": email})
        if email_data is not None:
            return cls(**email_data)

    @classmethod
    def get_by_id(cls, _id):
        _id_data = Database.find_one(collection="users", query={"_id": _id})
        if _id_data is not None:
            return cls(**_id_data)

    @staticmethod
    def login(user_email):
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password
        else:
            return False

    @classmethod
    def register(cls, email, password):
        user = User.get_by_email(email)
        if user is None:
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False
