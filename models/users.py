from common.database import Database
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

    @staticmethod
    def login(user_email):
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None
