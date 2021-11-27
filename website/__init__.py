from flask import Flask
from flask.blueprints import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'restaurantpos'
    uri = 'postgres://qebksjfwnxfqta:a7dc4725ed1576342d95906bdd69a574bea5b4e0c5c59df1b38d9d27a7ff35cf@ec2-52-204-72-14.compute-1.amazonaws.com:5432/d3s8ata3795je8'
    # uri = "postgresql+psycopg2://postgres:PosPassword@localhost:5432/Res_Pos"
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO=True']=True

    db.init_app(app)
    migrate = Migrate(app, db)
    from .models import dumpMenu
    with app.app_context():
        from .models import User, Table, Booking
        db.create_all()  # Create sql tables for our data models
        dumpMenu()

    from .models import User

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



    # Register Blueprint
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .menu import menu
    app.register_blueprint(menu, url_prefix='/menu')

    from .details import details
    app.register_blueprint(details, url_prefix='/details')

    from .cart import cart
    app.register_blueprint(cart,url_prefix='/cart')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .table_book import table_book 
    app.register_blueprint(table_book, url_prefix='/')
    return app
