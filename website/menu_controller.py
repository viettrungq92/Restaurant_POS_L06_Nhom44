# from website import app
from flask import Blueprint, render_template
import json

menu = Blueprint('menu',__name__)

@menu.route("/menu/<catagory>")
def display_menu(catagory= "all"):
    with open("website/menu.json","r") as file:
        menu = json.load(file)
    
    return render_template("menu.html", menu = menu, catagory = catagory)