from flask import Blueprint, render_template

views = Blueprint('views', __name__)

foods = [
    {
        'name': 'Burger Đặc biệt',
        'price': 80000,
        'quantity': 2,
        'image': 'https://mcdonalds.vn/uploads/2018/food/burgers/mcchicken-deluxe.png'
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

@views.route('/table')
def table():
    return render_template("table.html")