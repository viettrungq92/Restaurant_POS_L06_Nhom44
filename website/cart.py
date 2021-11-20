from operator import imod
from flask import Blueprint, redirect, render_template, url_for, request, abort, make_response
from flask_login import current_user
from website import db
from website.models import OrderForm, Order, OrderItem

cart = Blueprint("cart", __name__)


# @cart.route('/cart', methods=["GET"])
# def showCart():
#     form = OrderForm()
#     if form.validate_on_submit():
#         print( form.__jsonify__() )
#         return redirect( url_for("menu.display_menu", catagory="all"))
#     return render_template("cart.html", foods=carts, form = form, user = current_user)

"""Cart controller"""
@cart.route('/', methods=['GET'])
def getCartItems():
    try:
        resp = make_response()
        if current_user.is_anonymous:
            if not request.cookies.get('cart_id'):
                cart_id = Order.createCart()
                resp.set_cookie('cart_id', str(cart_id))
            else:
                cart_id = request.cookies.get('cart_id')
        else :
            if not current_user.cart_id:
                current_user.cart_id = Order.createCart(current_user.get_id() , current_user.phone, current_user.address)
                db.session.commit()
            cart_id = current_user.cart_id
        cart = Order.query.get( cart_id )
        if cart.status != 0:
            raise Exception("This is not cart.")
        form = OrderForm()
        resp.response = render_template('cart.html', foods=cart.items, total=cart.calTotal() ,form = form)
        return resp
    except Exception as e:
        print(e)
        abort(500)

@cart.route('/', methods=['POST'])
def checkout():
    phone = request.form.get('phoneNum')
    address = request.form.get('address')
    method = request.form.get('method')
    try:
        if current_user.is_authenticated:
            cart_id = current_user.cart_id
        else:
            cart_id = request.cookies.get('cart_id')

        order = Order.query.get(cart_id)
        order.checkout(
            phone = phone,
            address = address,
            method = method
        )
        resp = make_response( redirect( url_for(".getCartItems") ) )
        if current_user.is_authenticated:
            print("User loged in")
            current_user.cart_id = None
            db.session.commit()
        else:
            resp.set_cookie('cart_id', '')
        return resp
    except Exception as e:
        print(e)
        abort(428)

@cart.route('/delete')
def removeItem():
    d_id = request.args.get('dish_id')
    if current_user.is_authenticated:
        c_id = current_user.get_id()
    else:
        c_id = request.cookies.get('cart_id')

    try:
        item = OrderItem.query.get((c_id , d_id))
        OrderItem.removeItem(item)
        return redirect( url_for(".getCartItems"))
    except Exception as e:
        print(e)
        abort(428)
