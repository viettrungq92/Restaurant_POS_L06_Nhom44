from operator import imod
from flask import Blueprint, redirect, render_template, url_for, request, abort, make_response, jsonify
from flask_login import current_user
from website import db, auth
from website.models import OrderForm, Order, OrderItem, Dish

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
        resp = make_response( redirect("/menu/all") )
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

@cart.route('/order-all', methods=['GET'])
def getAllOrder():
    all_order = Order.getAllPending()
    contactsArr = []
    for contact in all_order:
        contactsArr.append(contact.toDict()) 
    return jsonify(contactsArr)
    
@cart.route('/order-item/<int:id>', methods=['GET'])
def getDishByOrderId(id):
    orderItem = OrderItem.query.filter_by(order_id=id)
    dishArr = []
    for item in orderItem:
        dish = getDishById(item.dish_id)
        dish['quantity'] = item.quantity
        dishArr.append(dish)
    return jsonify(dishArr)

@cart.route('/order-remove/<int:id>', methods=['GET'])
def canelOrder(id):
    order = Order.query.get(id)
    print(order.status)
    order.cancel()
    return redirect( url_for('auth.orders_manager'))


@cart.route('/order-fullfill/<int:id>', methods=['GET'])
def fullfillOrder(id):
    order = Order.query.get(id)
    order.fullfill()
    return redirect( url_for('auth.orders_manager'))

@cart.route('/dish/<int:id>', methods=['GET'])
def getDishById(id):
    dish = Dish.query.get(id)
    return dish.toDict()

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

@cart.route('/update-quantity', methods=['PUT'])
def updateQuantity():
    data = request.json
    print(data)
    try:
        try:
            if current_user.is_authenticated:
                cartID = current_user.cart_id
            else:
                cartID = request.cookies.get('cart_id')
            if cartID == None or cartID == '':
                raise Exception("Cannot find user cart")
        except Exception as e:
            print("Error")
            return e
        for item in data.get('data'):
            print(item)
            cartItem = OrderItem.query.get( (cartID, item['id']) )
            cartItem.updateQuantity(item['quantity'])

        return jsonify({'message' : 'Updated cart'})
    except Exception as e:
        print(e)
        return "Error 500"