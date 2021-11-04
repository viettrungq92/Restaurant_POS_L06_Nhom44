# from website import app
from flask import Blueprint, render_template, request, abort
import json

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
        return render_template("menu.html", menu = menu[catagory])
    else:
        abort(404)

@menu.route("/details")
def food_details():
    """
    Lấy data từ cái URL bằng request.args[<tên khóa>] rồi truyền vào cái file detail.html
    Vd URL: localhost/details?id=9&name=Spicy%20Chicken%20Rice&price=40000&thumbnail=/static/images/chicken-rice.jpg
    """
    # data = 
    # return render_template("detail.html", data = data)