from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db
from .decorators import admin_required

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect('/')
    return render_template('login_page.html')

@auth.route('/admin-login')
def admin_login():
    if current_user.is_authenticated:
        return redirect('/')
    return render_template('admin_login_page.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('user')
    password = request.form.get('loginpassword')
    remember = True

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect('/')

@auth.route('/admin-login', methods=['POST'])
def admin_login_post():
    email = request.form.get('user')
    password = request.form.get('loginpassword')
    remember = True

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password) or not user.is_admin():
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.admin_login'))

    login_user(user, remember=remember)

    return redirect(url_for('auth.users_manager'))


@auth.route('/signup')
def signup():
    if current_user.is_authenticated:
        return redirect('/')
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
    return redirect('/')

@auth.route('/profile')
@login_required
def profile():
    return render_template('user_profile.html', user=current_user)



@auth.route('/users-manager')
@admin_required()
def users_manager():
   return render_template('admin-page.html')



@auth.route('/current-user')
def get_current_user():
    if current_user.is_authenticated:
        return current_user.as_dict()
    else:
        abort(401)



