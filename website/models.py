from datetime import datetime
from sqlalchemy.log import Identified
from sqlalchemy.orm import backref, base, relationship
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from enum import unique
import json
from operator import imod
from sys import stderr
from flask import json
from flask_login import UserMixin
from flask_wtf import FlaskForm
from sqlalchemy.orm import backref
from wtforms import StringField, EmailField, RadioField
from wtforms.validators import InputRequired
from datetime import datetime

from website import db
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

    cart_id = db.Column(db.Integer,  db.ForeignKey('order.id'), default=None)
    cart = db.relationship('Order', primaryjoin="User.cart_id==Order.id", lazy=True)
    orders = db.relationship('Order',backref='user',primaryjoin="User.id==Order.user_id", lazy=True)
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def is_admin(self):
        return self.user_role and ("admin" in self.user_role)
            
        
    

class OrderForm(FlaskForm):
    fname = StringField('First Name', validators=[ InputRequired()])
    lname = StringField('Last Name', validators=[ InputRequired()])
    email = EmailField('Email', validators=[ InputRequired()])
    phoneNum = StringField('Phone number', validators=[ InputRequired()])
    address = StringField('Address', validators=[ InputRequired()])
    method = RadioField('Payment method', choices=[
        ("cash", "Cash"),
        ("online", "Online"),
    ], default="cash")


class Order(db.Model):
    CART = 0
    PENDING = 1
    PAYED = 2
    CANCEL = -1

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.Integer, nullable=False, default=CART)
    phone = db.Column(db.String(10), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    method = db.Column(db.String(20), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    items = db.relationship('OrderItem', primaryjoin='Order.id==OrderItem.order_id', lazy=True)

    @classmethod
    def createCart(cls, user_id = None, phone = None, address = None):
        """Create a cart and return its id"""
        try:
            newCart = cls(
                user_id = user_id,
                phone = phone,
                address = address
            )
            db.session.add(newCart)
            db.session.commit()
            return newCart.id
        except Exception as e:
            print(e)   

    def toDict(self):
        return { k.name : getattr(self, k.name) for k in self.__table__.columns }
    
    def calTotal(self):
        total = 0
        for item in self.items:
            total += item.calPrice()
        return total

    def isCart(self):
        return self.status == 0

    def isPending(self):
        return self.status == 1
    
    def isPayed(self):
        return self.status == 2
    
    def isCanceled(self):
        return self.status == -1

    def getItems(self):
        return self.items
    
    def checkout(self, phone, address, method):
        try:
            if self.status == 0:
                self.phone = phone
                self.address = address
                self.method = method
                self.status = 1
                db.session.commit()
            else: raise Exception("This is not a cart or cart has already been checkout.")
        except Exception as e:
            print(e)

    def fullfill(self):
        try:
            if self.status == 0:
                raise Exception("Error: Order has not yet been checkout")
            elif self.status != 1:
                raise Exception("Error: Order has been proccessed")
            else:
                self.status = 2
                db.session.commit()
        except Exception as e:
            print(e)

    def cancel(self):
        try:
            if self.status == 0:
                raise Exception("Error: Order has not yet been checkout")
            elif self.status == 2:
                raise Exception("Error: Order has already been fullfilled")
            else:
                self.status == -1
                db.session.commit()
        except Exception as e:
            print(e)
    
    @classmethod
    def getAllOrder(cls):
        return (cls.query.all())

    @classmethod
    def getAllPending(cls):
        return cls.query.filter_by(status = cls.PENDING)

    def getCartItems(self):
        try:
            if not self.isCart():
                raise Exception("This is not a cart")
            else:
                self.getOrderItems()
        except Exception as e:
            print(e)
    
    def getOrderItems(self):
        return self.items

class OrderItem(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), primary_key=True)
    dish = db.relationship('Dish', foreign_keys=dish_id)
    quantity = db.Column(db.Integer, default=0)

    @classmethod
    def createOrderItem(cls, order_id, dish_id, quantity = 1):
        try:
            newItem = cls(
                order_id = order_id,
                dish_id = dish_id,
                quantity = quantity
            )
            db.session.add(newItem)
            db.session.commit()
        except Exception as e:
            print(e)
    
    @staticmethod
    def removeItem(item):
        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            print(e)

    def calPrice(self):
        return self.quantity*self.dish.price

    def updateQuantity(self, quantity):
        try:
            self.quantity = quantity
            db.session.commit()
        except Exception as e:
            print(e)

class DishType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    dishes = db.relationship('Dish', backref='type', lazy=True)

    def toDict(self):
        return { k.name : getattr(self, k.name) for k in self.__table__.columns }

    
class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    price = db.Column(db.Integer, nullable=False)
    thumbnail = db.Column(db.String(100))
    type_id = db.Column(db.Integer, db.ForeignKey('dish_type.id'))

    def toDict(self):
        return { k.name : getattr(self, k.name) for k in self.__table__.columns }

def dumpMenu():
    try:
        db.engine.execute("""
INSERT INTO public.dish_type(
	id, name)
	VALUES (1, 'burger'), (2, 'chicken'), (3, 'rice'), (4, 'drinks');
    """)
        db.engine.execute("""
INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (1, 'Burger 2 lớp bò phô mai', 59000, '/static/images/b1_2-lop-bo-pho-mai.png', 1);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (2, 'Burger bò miếng lớn phô mai', 69000, '/static/images/b2_bo-mieng-lon-pho-mai.png', 1);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (3, 'Burger gà phô mai', 69000, '/static/images/b3_ga-pho-mai.png', 1);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (4, 'Burger Big Mac', 69000, '/static/images/b4_big-mac.png', 1);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (5, 'Burger bò miếng lớn đặc biệt', 79000, '/static/images/b5_bo-mieng-lon-dac-biet.png', 1);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (6, 'Burger phi lê gà cay', 79000, '/static/images/b6_phi-le-ga-cay.png', 1);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (7, 'Burger gà Mayo', 59000, '/static/images/b7_ga-mayo.png', 1);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (8, 'Burger heo', 32000, '/static/images/b8_heo.png', 1);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (9, '1 miếng gà rán', 36000, '/static/images/c1_1-mieng-ga-ran.png', 2);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (10, '3 miếng gà rán', 99000, '/static/images/c2_3-mieng-ga-ran.png', 2);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (11, '5 miếng gà rán', 169000, '/static/images/c3_5-mieng-ga-ran.png', 2);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (12, '3 miếng cánh gà McWings', 69000, '/static/images/c4_3-mieng-canh-ga-McWings.png', 2);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (13, '4 miếng gà Nuggets', 36000, '/static/images/c5_4-mieng-ga-Nuggets.png', 2);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (14, '6 miếng gà Nuggets', 49000, '/static/images/c6_6-mieng-ga-Nuggets.png', 2);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (15, '6 miếng cánh gà', 125000, '/static/images/c7_6-mieng-canh-ga.png', 2);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (16, '2 miếng gà rán + khoai tây chiên + nước ngọt', 86000, '/static/images/c8_2-mieng-ga-ran-khoai-tay-chien-nuoc.png', 2);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (17, 'Cơm thịt nướng', 39000, '/static/images/r1_com-thit-nuong.png', 3);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (18, 'Cơm thịt gà chiên', 39000, '/static/images/r2_com-thit-ga-chien.png', 3);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (19, 'Cơm thịt nướng ốp la', 49000, '/static/images/r3_com-thit-nuong-op-la.png', 3);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (20, 'Cơm phi lê gà cay', 76000, '/static/images/r4_com-phi-le-ga-cay.png', 3);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (21, 'Cơm thịt nướng + nước ngọt', 46000, '/static/images/r5_com-thit-nuong-nuoc-ngot.png', 3);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (22, 'Cơm thịt gà chiên + nước ngọt', 46000, '/static/images/r6_com-thit-ga-chien-nuoc-ngot.png', 3);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (23, 'Cơm thịt nướng ốp la + nước ngọt', 66000, '/static/images/r7_com-thit-nuong-op-la-nuoc-ngot.png', 3);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (24, 'Cơm phi lê gà cay + nước ngọt', 90000, '/static/images/r8_com-phi-le-ga-cay-nuoc-ngot.png', 3);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (25, 'Fanta', 15000, '/static/images/d1_fanta.png', 4);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (26, 'Nước cam', 20000, '/static/images/d2_nuoc-cam.png', 4);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (27, 'Nước suối', 20000, '/static/images/d3_nuoc-suoi.png', 4);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (28, 'Sprite', 20000, '/static/images/d4_sprite.png', 4);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (29, 'Coca', 20000, '/static/images/d5_coca.png', 4);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (30, 'Coca Light', 25000, '/static/images/d6_coca-light.png', 4);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (31, 'Tra den Lychee', 45000, '/static/images/d7_tra-den-lychee.png', 4);

INSERT INTO public.dish(
    id, name, price, thumbnail, type_id)
    VALUES (32, 'Milo', 20000, '/static/images/d8_milo.png', 4);
        """)
    except:
        pass


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
    name = db.Column(db.String(20), nullable = False)
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




