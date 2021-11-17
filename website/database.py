from flask import Flask

# Tham khao: https://www.youtube.com/playlist?list=PL4iRawDSyRvVd1V7A45YtAGzDk6ljVPm1

from sqlalchemy import Column, ForeignKey, Integer, String
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

Base = declarative_base()

session = Session()

# Tao bang


class User(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True)
    fname = Column(String(30))
    lname = Column(String(30))
    phone = Column(String(10))
    address = Column(String(200))
    email = Column(String(30))
    password = Column(String(30))


class Table(Base):
    __tablename__ = 'Table'
    ID = Column(Integer, primary_key=True)
    type = Column(Integer)


class Dish(Base):
    __tablename__ = 'Dish'
    ID = Column(Integer, primary_key=True)
    name = Column(String(30))
    price = Column(Integer)
    available_qty = Column(Integer)
    img = Column(String(30))


class Order(Base):
    __tablename__ = 'Order'
    ID = Column(Integer, primary_key=True)
    status = Column(String(1))
    created_date = Column(datetime)
    phone = Column(String(10))
    User_ID = Column(Integer, ForeignKey('User.ID'))


class Booking(Base):
    __tablename__ = 'Booking'
    ID = Column(Integer, primary_key=True)
    comment = Column(String(500))
    booking_data = Column(datetime)
    booking_time = Column(Integer)
    cus_name = Column(String(50))
    phone = Column(String(10))
    Table_ID = Column(Integer, ForeignKey('Table.ID'))
    User_ID = Column(String(50), ForeignKey('User.ID'))


class Order_Item(Base):
    __tablename__ = 'Order_Item'
    Order_ID = Column(Integer, ForeignKey('Order.ID'), primary_key=True)
    Dish_ID = Column(Integer, ForeignKey('Dish.ID'), primary_key=True)
    quantity = Column(Integer)
    total_price = Column(Integer)


engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)

# Insert du lieu vao bang

User1 = User(ID=1, fname="Phuong", lname="Nguyen", phone="0123456789",
             address="HoocMon", email="phuongnguyen123@hcmut.edu.vn", password="phuong12345")
User2 = User(ID=2, fname="Hiep", lname="Ngo", phone="0123123123",
             address="ThuDuc", email="hiepngo456@hcmut.edu.vn", password="hiepngo567")
User3 = User(ID=3, fname="Vinh", lname="Dinh", phone="0456456456",
             address="TanBinh", email="vinhdinh789@hcmut.edu.vn", password="vinh456789")
User4 = User(ID=4, fname="Vinh", lname="Tran", phone="0789789789",
             address="Quan10", email="trungtran111@hcmut.edu.vn", password="trungtran")
User5 = User(ID=5, fname="Thinh", lname="Nguyen", phone="0987654321",
             address="BinhThanh", email="thinhnguyen999@hcmut.edu.vn", password="thinh9999")

session.add_all([User1, User2, User3, User4, User5])
session.commit()

Table1 = Table(ID=1, type=1)
Table2 = Table(ID=2, type=1)
Table3 = Table(ID=3, type=1)
Table4 = Table(ID=4, type=1)
Table5 = Table(ID=5, type=2)
Table6 = Table(ID=6, type=2)
Table7 = Table(ID=7, type=2)
Table8 = Table(ID=8, type=2)
Table9 = Table(ID=9, type=3)
Table10 = Table(ID=10, type=3)

session.add_all([Table1, Table2, Table3, Table4, Table5,
                Table6, Table7, Table8, Table9, Table10])
session.commit()

Dish1 = Dish(ID=1, name="Burger 2 lớp bò phô mai", price=59000, available_qty=10,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b1_2-lop-bo-pho-mai.PNG")
Dish2 = Dish(ID=2, name="Burger bò miếng lớn phô mai", price=69000, available_qty=10,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b2_bo-mieng-lon-pho-mai.PNG")
Dish3 = Dish(ID=3, name="Burger gà phô mai", price=69000, available_qty=10,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b3_ga-pho-mai.PNG")
Dish4 = Dish(ID=4, name="Burger Big Mac", price=69000, available_qty=10,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b4_big-mac.PNG")
Dish5 = Dish(ID=5, name="Burger bò miếng lớn đặc biệt", price=79000, available_qty=10,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b5_bo-mieng-lon-dac-biet.PNG")
Dish6 = Dish(ID=6, name="Burger phi lê gà cay", price=79000, available_qty=10,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b6_phi-le-ga-cay.PNG")
Dish7 = Dish(ID=7, name="Burger gà Mayo", price=59000, available_qty=10,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b7_ga-mayo.PNG")
Dish8 = Dish(ID=8, name="Burger heo", price=32000, available_qty=10,
             img="Restaurant_POS_L06_Nhom44/website/static/images/b8_heo.PNG")
Dish9 = Dish(ID=9, name="1 miếng gà rán", price=36000, available_qty=10,
             img="Restaurant_POS_L06_Nhom44/website/static/images/c1_1-mieng-ga-ran.PNG")
Dish10 = Dish(ID=10, name="3 miếng gà rán", price=99000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c2_3-mieng-ga-ran.PNG")
Dish11 = Dish(ID=11, name="5 miếng gà rán", price=169000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c3_5-mieng-ga-ran.PNG")
Dish12 = Dish(ID=12, name="3 miếng cánh gà McWings", price=69000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c4_3-mieng-canh-ga-McWings.PNG")
Dish13 = Dish(ID=13, name="4 miếng gà Nuggets", price=36000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c5_4-mieng-ga-Nuggets.PNG")
Dish14 = Dish(ID=14, name="6 miếng gà Nuggets", price=49000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c6_6-mieng-ga-Nuggets.PNG")
Dish15 = Dish(ID=15, name="6 miếng cánh gà", price=125000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c7_6-mieng-canh-ga.PNG")
Dish16 = Dish(ID=16, name="2 miếng gà rán + khoai tây chiên + nước ngọt", price=86000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/c8_2-mieng-ga-ran-khoai-tay-chien-nuoc.PNG")
Dish17 = Dish(ID=17, name="Cơm thịt nướng", price=39000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r1_com-thit-nuong.PNG")
Dish18 = Dish(ID=18, name="Cơm thịt gà chiên", price=39000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r2_com-thit-ga-chien.PNG")
Dish19 = Dish(ID=19, name="Cơm thịt nướng ốp la", price=49000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r3_com-thit-nuong-op-la.PNG")
Dish20 = Dish(ID=20, name="Cơm phi lê gà cay", price=76000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r4_com-phi-le-ga-cay.PNG")
Dish21 = Dish(ID=21, name="Cơm thịt nướng + nước ngọt", price=46000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r5_com-thit-nuong-nuoc-ngot.PNG")
Dish22 = Dish(ID=22, name="Cơm thịt gà chiên + nước ngọt", price=46000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r6_com-thit-ga-chien-nuoc-ngot.PNG")
Dish23 = Dish(ID=23, name="Cơm thịt nướng ốp la + nước ngọt", price=66000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r7_com-thit-nuong-op-la-nuoc-ngot.PNG")
Dish24 = Dish(ID=24, name="Cơm phi lê gà cay + nước ngọt", price=90000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/r8_com-phi-le-ga-cay-nuoc-ngot.PNG")
Dish25 = Dish(ID=25, name="Fanta", price=15000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d1_fanta.PNG")
Dish26 = Dish(ID=26, name="Nước cam", price=20000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d2_nuoc-cam.PNG")
Dish27 = Dish(ID=27, name="Nước suối", price=20000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d3_nuoc-suoi.PNG")
Dish28 = Dish(ID=28, name="Sprite", price=20000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d4_sprite.PNG")
Dish29 = Dish(ID=29, name="Coca", price=20000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d5_coca.PNG")
Dish30 = Dish(ID=30, name="Coca Light", price=25000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d6_coca-light.PNG")
Dish31 = Dish(ID=31, name="Tra den Lychee", price=45000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d7_tra-den-lychee.PNG")
Dish32 = Dish(ID=32, name="Milo", price=20000, available_qty=10,
              img="Restaurant_POS_L06_Nhom44/website/static/images/d8_milo.PNG")

session.add_all([Dish1, Dish2, Dish3, Dish4, Dish5, Dish6, Dish7, Dish8, Dish9, Dish10, Dish11, Dish12, Dish13, Dish14, Dish15, Dish16,
                Dish17, Dish18, Dish19, Dish20, Dish21, Dish22, Dish23, Dish24, Dish25, Dish26, Dish27, Dish28, Dish29, Dish30, Dish31, Dish32])
session.commit()

Booking1 = Booking(ID=1, comment="Bàn gần cửa sổ", booking_data=datetime(
    2021, 12, 1), booking_time=9, cus_name="Phuong", phone="0123456789", Table_ID=1, User_ID=1)
Booking2 = Booking(ID=2, comment="Bàn có ổ cắm điện", booking_data=datetime(
    2021, 12, 5), booking_time=12, cus_name="Phuong", phone="0123456789", Table_ID=2, User_ID=1)
Booking3 = Booking(ID=3, comment="Bàn ở trên sân thượng", booking_data=datetime(
    2021, 12, 10), booking_time=9, cus_name="Linh", phone="0111111111", Table_ID=10, User_ID=1)
Booking4 = Booking(ID=4, comment="Bàn có ổ cắm điện", booking_data=datetime(
    2021, 12, 31), booking_time=20, cus_name="Hiep", phone="0123123123", Table_ID=1, User_ID=2)
Booking5 = Booking(ID=5, comment="Bàn gần cửa sổ", booking_data=datetime(
    2021, 12, 20), booking_time=9, cus_name="Hiep", phone="0123123123", Table_ID=3, User_ID=2)
Booking6 = Booking(ID=6, comment="Bàn có ổ cắm điện", booking_data=datetime(
    2021, 12, 21), booking_time=20, cus_name="Hiep", phone="0123123123", Table_ID=7, User_ID=2)
Booking7 = Booking(ID=7, comment="Bàn ở trên sân thượng", booking_data=datetime(
    2021, 12, 6), booking_time=9, cus_name="Vinh", phone="0456456456", Table_ID=2, User_ID=3)
Booking8 = Booking(ID=8, comment="Bàn gần cửa sổ", booking_data=datetime(
    2021, 12, 15), booking_time=20, cus_name="Vinh", phone="0456456456", Table_ID=4, User_ID=3)
Booking9 = Booking(ID=9, comment="Bàn ở trên sân thượng", booking_data=datetime(
    2021, 12, 22), booking_time=12, cus_name="Hoang", phone="0222222222", Table_ID=8, User_ID=3)
Booking10 = Booking(ID=10, comment="Bàn có ổ cắm điện", booking_data=datetime(
    2021, 12, 29), booking_time=12, cus_name="Trung", phone="0789789789", Table_ID=1, User_ID=4)
Booking11 = Booking(ID=11, comment="Bàn gần cửa sổ", booking_data=datetime(
    2021, 12, 25), booking_time=20, cus_name="Trung", phone="0789789789", Table_ID=9, User_ID=4)
Booking12 = Booking(ID=12, comment="Bàn ở trên sân thượng", booking_data=datetime(
    2021, 12, 2), booking_time=9, cus_name="Thinh", phone="0987654321", Table_ID=1, User_ID=5)
Booking13 = Booking(ID=13, comment="Bàn có ổ cắm điện", booking_data=datetime(
    2021, 12, 11), booking_time=12, cus_name="Thinh", phone="0987654321", Table_ID=10, User_ID=5)

session.add_all([Booking1, Booking2, Booking3, Booking4, Booking5, Booking6,
                Booking7, Booking8, Booking9, Booking10, Booking11, Booking12, Booking13])
session.commit()

Order1 = Order(ID=1, status=0, created_date=datetime(2021, 11, 28), phone="0123456789", User_ID=1)
Order2 = Order(ID=2, status=0, created_date=datetime(2021, 11, 29), phone="0123123123", User_ID=2)
Order3 = Order(ID=3, status=0, created_date=datetime(2021, 11, 30), phone="0456456456", User_ID=3)
Order4 = Order(ID=4, status=0, created_date=datetime(2021, 11, 30), phone="0789789789", User_ID=4)
Order5 = Order(ID=5, status=0, created_date=datetime(2021, 11, 29), phone="0987654321", User_ID=5)
Order6 = Order(ID=6, status=1, created_date=datetime(2021, 12, 1), phone="0123456789", User_ID=1)
Order7 = Order(ID=7, status=1, created_date=datetime(2021, 12, 2), phone="0123123123", User_ID=2)
Order8 = Order(ID=8, status=1, created_date=datetime(2021, 12, 1), phone="0456456456", User_ID=3)
Order9 = Order(ID=9, status=1, created_date=datetime(2021, 12, 3), phone="0789789789", User_ID=4)
Order10 = Order(ID=10, status=1, created_date=datetime(2021, 12, 2), phone="0987654321", User_ID=5)

session.add_all([Order1 , Order2 , Order3 , Order4 , Order5 , Order6 , Order7 , Order8 , Order9, Order10])
session.commit()

Order_Item1 = Order_Item(Order_ID=1, Dish_ID=10, quantity=1, total_price=99000)
Order_Item2 = Order_Item(Order_ID=2, Dish_ID=2, quantity=2, total_price=138000)
Order_Item3 = Order_Item(Order_ID=3, Dish_ID=30, quantity=3, total_price=75000)
Order_Item4 = Order_Item(Order_ID=4, Dish_ID=25, quantity=3, total_price=45000)
Order_Item5 = Order_Item(Order_ID=5, Dish_ID=16, quantity=1, total_price=86000)
Order_Item6 = Order_Item(Order_ID=6, Dish_ID=31, quantity=2, total_price=90000)
Order_Item7 = Order_Item(Order_ID=7, Dish_ID=20, quantity=3, total_price=228000)
Order_Item8 = Order_Item(Order_ID=8, Dish_ID=10, quantity=1, total_price=99000)
Order_Item9 = Order_Item(Order_ID=9, Dish_ID=19, quantity=3, total_price=147000)
Order_Item10 = Order_Item(Order_ID=10, Dish_ID=7, quantity=2, total_price=118000)
Order_Item11 = Order_Item(Order_ID=11, Dish_ID=2, quantity=3, total_price=207000)
Order_Item12 = Order_Item(Order_ID=12, Dish_ID=2, quantity=1, total_price=69000)
Order_Item13 = Order_Item(Order_ID=13, Dish_ID=3, quantity=2, total_price=138000)
Order_Item14 = Order_Item(Order_ID=14, Dish_ID=25, quantity=1, total_price=15000)
Order_Item15 = Order_Item(Order_ID=15, Dish_ID=19, quantity=1, total_price=49000)
Order_Item16 = Order_Item(Order_ID=16, Dish_ID=2, quantity=2, total_price=138000)
Order_Item17 = Order_Item(Order_ID=17, Dish_ID=11, quantity=1, total_price=169000)
Order_Item18 = Order_Item(Order_ID=18, Dish_ID=20, quantity=3, total_price=228000)
Order_Item19 = Order_Item(Order_ID=19, Dish_ID=14, quantity=2, total_price=98000)
Order_Item20 = Order_Item(Order_ID=20, Dish_ID=5, quantity=1, total_price=79000)

session.add_all([Order_Item1 , Order_Item2 , Order_Item3 , Order_Item4 , Order_Item5 , Order_Item6 , Order_Item7 , Order_Item8 , Order_Item9 , Order_Item10 , Order_Item11 , Order_Item12 , Order_Item13 , Order_Item14 , Order_Item15 , Order_Item16 , Order_Item17 , Order_Item18 , Order_Item19 , Order_Item20])
session.commit()