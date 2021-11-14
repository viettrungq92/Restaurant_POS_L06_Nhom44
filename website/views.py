from os import write
from flask import Blueprint, render_template, redirect, url_for
import json
from .model.order import OrderForm

views = Blueprint('views', __name__)

carts = [
    {
        'name': 'Burger phô mai',
        'price': 80000,
        'quantity': 5,
        'image': 'https://mcdonalds.vn/uploads/2018/food/burgers/cheese-burger-deluxe.png'
    },
    {
        'name': '6 Miếng Cánh Gà',
        'price': 125000,
        'quantity': 5,
        'image': 'https://mcdonalds.vn/uploads/2018/food/ga-ran/6-wings.png'
    },
    {
        'name': 'Coca Cola',
        'price': 20000,
        'quantity': 3,
        'image': 'https://mcdonalds.vn/uploads/2018/food/beverage/mcd-food-beverages-soft-drinks-coke.png'
    }
]

@views.route('/cart', methods=["GET", "POST"])
def cart():
    form = OrderForm()
    if form.validate_on_submit():
        print( form.__jsonify__() )
        return redirect( url_for("menu.display_menu", catagory="all"))

    return render_template("cart.html", foods=carts, form = form)

@views.route('/')
def table():
    # f = open('website/table.json').read()
    # table = json.loads(f)
    # tablestr = json.dumps(table, indent=2, sort_keys=True)
    with open('website/table.json', 'r') as f:
        data = json.load(f)
        json_mylist = json.dumps(data)
    return render_template("table.html", user = json_mylist)

@views.route("/temp")
def temp():
    return render_template("temp.html")