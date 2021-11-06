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

# @menu.route("/menu")
# def display_menu():
#     with open("website/menu.json","r") as file:
#         menu = json.load(file)
    
#     selected = []
#     try:
#         catagory = request.args["catagory"]
#     except:
#         for dishs in menu.values():
#             selected.extend(dishs)
#         return render_template("menu.html", menu = selected)

#     if catagory in menu.keys():
#         selected.extend(menu[catagory])
#         return render_template("menu.html", menu = selected)
#     else:
#         abort(404)
    
@menu.route("/detail")
def details():
    (id, type) = request.args
    with open("website/menu.json", "r") as f:
        menu = json.load(f)
    return render_template("details.html",id = id,type = type,menu = menu)
