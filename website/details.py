from operator import imod
from warnings import catch_warnings
from flask import Blueprint, render_template, request, abort, url_for, redirect, make_response
from flask_login import current_user
import json

from werkzeug.wrappers import response


from website import cart, db
from website.models import Dish, Order, OrderItem
from flask_login import current_user

details = Blueprint('details',__name__)

# @details.route("/product")
# def display_details():
    
#     # Load menu from database here
#     selected_food = getDishDetail(id)
#     return render_template("details.html", food = selected_food)

@details.route('/product')
def getDishDetail():
    dish_id = request.args.get('id')
    dish = Dish.query.get(dish_id)
    resp = make_response(render_template("details.html", food = dish))
    if current_user.is_anonymous and not request.cookies.get('cart_id'):
        cart_id = Order.createCart()
        resp.set_cookie('cart_id', str(cart_id))
    elif current_user.is_authenticated and not current_user.cart_id:
        current_user.cart_id = Order.createCart(current_user.get_id() , current_user.phone, current_user.address)
        db.session.commit()
    return resp

@details.route('/addToCart')
def createItem():
    """Adding item to given cart_id. If cart_id wasn't given, create a new Cart"""
    dish_id = request.args.get('id')
    quantity = int(request.args.get('quantity'))

    if current_user.is_authenticated:
        cart_id = current_user.cart_id
    else:
        cart_id = request.cookies.get('cart_id')

    try:
        item = OrderItem.query.get((cart_id,dish_id))
        if not item:
            OrderItem.createOrderItem(
                order_id= cart_id,
                dish_id= dish_id,
                quantity= quantity
            )
         # Increase existing item's quantity by amount given
        else:
            item.updateQuantity( item.quantity + quantity )
            
        return redirect( url_for('.getDishDetail', id=dish_id))
    except Exception as e:
        print(e)
        return {e}
