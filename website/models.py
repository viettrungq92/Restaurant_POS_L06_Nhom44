from datetime import datetime
from sqlalchemy.log import Identified
from sqlalchemy.orm import backref, base, relationship
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
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

# booking = db.Table('booking',
#     db.Column('id', db.Integer, primary_key=True, nullable = False),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('table_id', db.Integer, db.ForeignKey('table.id')),
#     db.Column('comment', db.String(300)),
#     db.Column('date', db.Date, nullable = False),
#     db.Column('time', db.Integer, nullable = False),
#     db.Column('phone', db.String(10), nullable = False)
# )

class Booking(db.Model):
    __tablename__ = "booking"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable = False)
    time = db.Column(db.Integer, nullable = False)
    phone = db.Column(db.String(10), nullable = False)
    nop = db.Column(db.Integer, nullable = False)
    comment = db.Column(db.String(100), nullable= True)
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }



class Table(db.Model):
    __tablename__ = "table"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    # users = db.relationship("User", secondary = booking, backref = db.backref("books"))




