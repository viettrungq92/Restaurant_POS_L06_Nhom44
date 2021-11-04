from flask import Blueprint, render_template, request, abort
import json

details = Blueprint('details',__name__)

@details.route("/details")
def dish_details(id):
    pass