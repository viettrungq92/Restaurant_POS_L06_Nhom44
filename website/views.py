from os import write
from flask import Blueprint, render_template, jsonify
import json

views = Blueprint('views', __name__)

carts = [
    {
        'id': 1,
        'quantity': 2
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

@views.route('/cart')
def cart():
    return render_template("cart.html", foods=foods)

@views.route('/')
def table():
    # f = open('website/table.json').read()
    # table = json.loads(f)
    # tablestr = json.dumps(table, indent=2, sort_keys=True)
    with open('website/table.json', 'r') as f:
        data = json.load(f)
        json_mylist = json.dumps(data)
    return render_template("table.html", user = json_mylist)