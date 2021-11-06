from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'restaurantpos'

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .menu_controller import menu
    app.register_blueprint(menu, url_prefix='/')

    # from .details import details
    # app.register_blueprint(details, url_prefix='/')
    
    return app
