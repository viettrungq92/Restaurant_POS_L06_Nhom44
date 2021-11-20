from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login_page.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('user')
    password = request.form.get('loginpassword')
    remember = True

    user = User.query.filter_by(email=email).first()
    # print(user.phone)
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect('/')

@auth.route('/signup')
def signup():
    return render_template('register_page.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    address = request.form.get('address')
    password = request.form.get('password')
    phone = request.form.get('phonenumber')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, firstname=firstname, lastname=lastname, phone=phone,
                    address=address,  password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.table'))