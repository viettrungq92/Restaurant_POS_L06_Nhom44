# from website import app
from flask import Blueprint, render_template, request, abort, redirect
# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms.validators import DataRequired
import json

from flask.helpers import url_for

from .model.order import OrderForm

menu = Blueprint('menu',__name__)

@menu.route("/menu/<catagory>")
def display_menu(catagory= "all"):
    with open("website/menu.json","r") as file:
        menu = json.load(file)
    
    if catagory == "all":
        all_menu = []
        for dishs in menu.values():
            all_menu.extend(dishs)
        return render_template("menu.html", menu = all_menu)
    elif catagory in menu.keys():
        return render_template("menu.html", menu = menu.get(catagory), catagory = catagory)
    else:
        abort(404)

@menu.route("/detail")
def details():
    (id, type) = request.args.values()
    print(id, type)
    with open("website/menu.json", "r") as f:
        menu = json.load(f)
    return render_template("details.html",id = id,type = type,menu = menu)
 