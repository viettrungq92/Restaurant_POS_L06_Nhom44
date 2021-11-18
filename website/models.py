from datetime import datetime
from sqlalchemy.log import Identified
from sqlalchemy.orm import backref, base, relationship
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from . import db

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


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

# ---------------------
# Create table: Dish_type, Dish, Order, Order_item


class Dish_type(db.Model):
    __tablename__ = 'dish_type'
    ID = db.Column(db.Integer, primary_key=True)
    Dish_type_name = db.Column(db.String(30))


class Dish(db.Model):
    __tablename__ = 'dish'
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    Dish_type_ID = db.column(db.Integer, db.ForeignKey('dish_type.ID'))  # new
    price = db.Column(db.Integer)
    # available_qty = db.Column(db.Integer) # delete
    img = db.Column(db.String(100))


class Order(db.Model):
    __tablename__ = 'order'
    ID = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)  # new
    status = db.Column(db.String(1))
    created_date = db.Column(datetime)
    phone = db.Column(db.String(10))
    User_ID = db.Column(db.Integer, db.ForeignKey('user.ID'))


class Order_item(db.Model):
    __tablename__ = 'order_item'
    Order_ID = db.Column(db.Integer, db.ForeignKey(
        'order.ID'), primary_key=True)
    Dish_ID = db.Column(db.Integer, db.ForeignKey('dish.ID'), primary_key=True)
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Integer)

# ---------------------
# Insert data into table: Dish_type, Dish, Order, Order_item


session = Session()

Dish_type1 = Dish_type(ID=1, Dish_type_name="burger")
Dish_type2 = Dish_type(ID=2, Dish_type_name="chicken")
Dish_type3 = Dish_type(ID=3, Dish_type_name="rice")
Dish_type4 = Dish_type(ID=4, Dish_type_name="drinks")

session.add_all([Dish_type1, Dish_type2, Dish_type3, Dish_type4])
session.commit()

Dish1 = Dish(ID=1, name="Burger 2 lớp bò phô mai", Dish_type_ID=1,  price=59000,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b1_2-lop-bo-pho-mai.PNG")
Dish2 = Dish(ID=2, name="Burger bò miếng lớn phô mai", Dish_type_ID=1, price=69000,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b2_bo-mieng-lon-pho-mai.PNG")
Dish3 = Dish(ID=3, name="Burger gà phô mai", Dish_type_ID=1, price=69000,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b3_ga-pho-mai.PNG")
Dish4 = Dish(ID=4, name="Burger Big Mac", Dish_type_ID=1, price=69000,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b4_big-mac.PNG")
Dish5 = Dish(ID=5, name="Burger bò miếng lớn đặc biệt", Dish_type_ID=1, price=79000,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b5_bo-mieng-lon-dac-biet.PNG")
Dish6 = Dish(ID=6, name="Burger phi lê gà cay", Dish_type_ID=1, price=79000,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b6_phi-le-ga-cay.PNG")
Dish7 = Dish(ID=7, name="Burger gà Mayo", Dish_type_ID=1, price=59000,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b7_ga-mayo.PNG")
Dish8 = Dish(ID=8, name="Burger heo", Dish_type_ID=1, price=32000,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b8_heo.PNG")
Dish9 = Dish(ID=9, name="1 miếng gà rán", Dish_type_ID=2, price=36000,
             img="Restaurant_POS_L06_Nhom44/website/static/images/c1_1-mieng-ga-ran.PNG")
Dish10 = Dish(ID=10, name="3 miếng gà rán", Dish_type_ID=2, price=99000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c2_3-mieng-ga-ran.PNG")
Dish11 = Dish(ID=11, name="5 miếng gà rán", Dish_type_ID=2, price=169000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c3_5-mieng-ga-ran.PNG")
Dish12 = Dish(ID=12, name="3 miếng cánh gà McWings", Dish_type_ID=2, price=69000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c4_3-mieng-canh-ga-McWings.PNG")
Dish13 = Dish(ID=13, name="4 miếng gà Nuggets", Dish_type_ID=2, price=36000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c5_4-mieng-ga-Nuggets.PNG")
Dish14 = Dish(ID=14, name="6 miếng gà Nuggets", Dish_type_ID=2, price=49000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c6_6-mieng-ga-Nuggets.PNG")
Dish15 = Dish(ID=15, name="6 miếng cánh gà", Dish_type_ID=2, price=125000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c7_6-mieng-canh-ga.PNG")
Dish16 = Dish(ID=16, name="2 miếng gà rán + khoai tây chiên + nước ngọt", Dish_type_ID=2, price=86000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c8_2-mieng-ga-ran-khoai-tay-chien-nuoc.PNG")
Dish17 = Dish(ID=17, name="Cơm thịt nướng", Dish_type_ID=3, price=39000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r1_com-thit-nuong.PNG")
Dish18 = Dish(ID=18, name="Cơm thịt gà chiên", Dish_type_ID=3, price=39000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r2_com-thit-ga-chien.PNG")
Dish19 = Dish(ID=19, name="Cơm thịt nướng ốp la", Dish_type_ID=3, price=49000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r3_com-thit-nuong-op-la.PNG")
Dish20 = Dish(ID=20, name="Cơm phi lê gà cay", Dish_type_ID=3, price=76000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r4_com-phi-le-ga-cay.PNG")
Dish21 = Dish(ID=21, name="Cơm thịt nướng + nước ngọt", Dish_type_ID=3, price=46000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r5_com-thit-nuong-nuoc-ngot.PNG")
Dish22 = Dish(ID=22, name="Cơm thịt gà chiên + nước ngọt", Dish_type_ID=3, price=46000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r6_com-thit-ga-chien-nuoc-ngot.PNG")
Dish23 = Dish(ID=23, name="Cơm thịt nướng ốp la + nước ngọt", Dish_type_ID=3, price=66000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r7_com-thit-nuong-op-la-nuoc-ngot.PNG")
Dish24 = Dish(ID=24, name="Cơm phi lê gà cay + nước ngọt", Dish_type_ID=3, price=90000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r8_com-phi-le-ga-cay-nuoc-ngot.PNG")
Dish25 = Dish(ID=25, name="Fanta", Dish_type_ID=4, price=15000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d1_fanta.PNG")
Dish26 = Dish(ID=26, name="Nước cam", Dish_type_ID=4, price=20000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d2_nuoc-cam.PNG")
Dish27 = Dish(ID=27, name="Nước suối", Dish_type_ID=4, price=20000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d3_nuoc-suoi.PNG")
Dish28 = Dish(ID=28, name="Sprite", Dish_type_ID=4, price=20000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d4_sprite.PNG")
Dish29 = Dish(ID=29, name="Coca", Dish_type_ID=4, price=20000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d5_coca.PNG")
Dish30 = Dish(ID=30, name="Coca Light", Dish_type_ID=4, price=25000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d6_coca-light.PNG")
Dish31 = Dish(ID=31, name="Tra den Lychee", Dish_type_ID=4, price=45000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d7_tra-den-lychee.PNG")
Dish32 = Dish(ID=32, name="Milo", Dish_type_ID=4, price=20000,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d8_milo.PNG")

session.add_all([Dish1, Dish2, Dish3, Dish4, Dish5, Dish6, Dish7, Dish8, Dish9, Dish10, Dish11, Dish12, Dish13, Dish14, Dish15, Dish16,
                Dish17, Dish18, Dish19, Dish20, Dish21, Dish22, Dish23, Dish24, Dish25, Dish26, Dish27, Dish28, Dish29, Dish30, Dish31, Dish32])
session.commit()

Order_item1 = Order_item(Order_ID=1, Dish_ID=10, quantity=1, total_price=99000)
Order_item2 = Order_item(Order_ID=2, Dish_ID=2, quantity=2, total_price=138000)
Order_item3 = Order_item(Order_ID=3, Dish_ID=30, quantity=3, total_price=75000)
Order_item4 = Order_item(Order_ID=4, Dish_ID=25, quantity=3, total_price=45000)
Order_item5 = Order_item(Order_ID=5, Dish_ID=16, quantity=1, total_price=86000)
Order_item6 = Order_item(Order_ID=6, Dish_ID=31, quantity=2, total_price=90000)
Order_item7 = Order_item(Order_ID=7, Dish_ID=20, quantity=3, total_price=228000)
Order_item8 = Order_item(Order_ID=8, Dish_ID=10, quantity=1, total_price=99000)
Order_item9 = Order_item(Order_ID=9, Dish_ID=19, quantity=3, total_price=147000)
Order_item10 = Order_item(Order_ID=10, Dish_ID=7, quantity=2, total_price=118000)
Order_item11 = Order_item(Order_ID=11, Dish_ID=2, quantity=3, total_price=207000)
Order_item12 = Order_item(Order_ID=12, Dish_ID=2, quantity=1, total_price=69000)
Order_item13 = Order_item(Order_ID=13, Dish_ID=3, quantity=2, total_price=138000)
Order_item14 = Order_item(Order_ID=14, Dish_ID=25, quantity=1, total_price=15000)
Order_item15 = Order_item(Order_ID=15, Dish_ID=19, quantity=1, total_price=49000)
Order_item16 = Order_item(Order_ID=16, Dish_ID=2, quantity=2, total_price=138000)
Order_item17 = Order_item(Order_ID=17, Dish_ID=11, quantity=1, total_price=169000)
Order_item18 = Order_item(Order_ID=18, Dish_ID=20, quantity=3, total_price=228000)
Order_item19 = Order_item(Order_ID=19, Dish_ID=14, quantity=2, total_price=98000)
Order_item20 = Order_item(Order_ID=20, Dish_ID=5, quantity=1, total_price=79000)

session.add_all([Order_item1 , Order_item2 , Order_item3 , Order_item4 , Order_item5 , Order_item6 , Order_item7 , Order_item8 , Order_item9 , Order_item10 , Order_item11 , Order_item12 , Order_item13 , Order_item14 , Order_item15 , Order_item16 , Order_item17 , Order_item18 , Order_item19 , Order_item20])
session.commit()

