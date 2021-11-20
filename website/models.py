from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    firstname = db.Column(db.String(1000))
    lastname = db.Column(db.String(1000))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(1000))
    user_role = db.Column(db.String(100))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def is_admin(self):
        return self.user_role and ("admin" in self.user_role)

