from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from sqlalchemy.orm import session
from sqlalchemy.orm.session import sessionmaker
from .models import User, Table, Booking
from sqlalchemy import create_engine, MetaData, engine
from sqlalchemy.orm import Session
from . import db
import json


table_book = Blueprint('table_book', __name__)

@table_book.route('/all', methods=['GET'])
def get_all_booking():
    
    all_book = Booking.query.all()
    # bookjson = json.dumps(all_book)
    contactsArr = []
    for contact in all_book:
        contactsArr.append(contact.toDict()) 
    return jsonify(contactsArr)


@table_book.route("/add", methods=['POST'])
def add_table():
    # date = request.get_json('date')
    content = request.get_json()
    date = content['date']
    time = content['time']
    name = content['name']
    phone = content['phone']
    nop = content['nop']
    comment = content['comment']
    print(date, " ", time, " ", phone, " ", nop)
    # time = request.json('time')
    # phone = request.json('phone')
    # table_id = request.json('table_id')
    new_booking = Booking(date = date, time = time, name = name, phone = phone, nop = nop, comment = comment)

    db.session.add(new_booking)
    db.session.commit()
    return "Success"
    
@table_book.route("/table/<string:phonenum>", methods=['GET'])
def get_table(phonenum):
    booked = Booking.query.filter_by(phone=phonenum)
    contactsArr = []
    for contact in booked:
        contactsArr.append(contact.toDict()) 
    print(contactsArr)
    return jsonify(contactsArr)
