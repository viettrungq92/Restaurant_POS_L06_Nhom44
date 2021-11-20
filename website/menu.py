from flask import Blueprint, render_template, request, abort, redirect, url_for
import json

from .models import OrderForm, Dish, DishType

menu = Blueprint('menu',__name__)

@menu.route('/')
def getAllDish():
    full_menu = [dish.toDict() for dish in Dish.query.order_by(Dish.type_id).all()]
    return render_template('menu.html', menu = full_menu, catagory='all')
        
@menu.route('/<catagory>')
def getDishByType(catagory):
    if catagory == 'all':
        return redirect( url_for('.getAllDish'))
    type = DishType.query.filter_by(name=catagory).first()
    if type:
        filtered_menu = [dish.toDict() for dish in type.dishes]
        return render_template('menu.html', menu = filtered_menu, catagory=catagory)
    else: 
        abort(404)








 