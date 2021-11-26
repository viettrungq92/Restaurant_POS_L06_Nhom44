from os import write
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
import json
from .models import OrderForm

views = Blueprint('views', __name__)

@views.route('/')
def table():
    # f = open('website/table.json').read()
    # table = json.loads(f)
    # tablestr = json.dumps(table, indent=2, sort_keys=True)
    with open('website/table.json', 'r') as f:
        data = json.load(f)
        json_mylist = json.dumps(data)
    return render_template("table.html", user = json_mylist)
