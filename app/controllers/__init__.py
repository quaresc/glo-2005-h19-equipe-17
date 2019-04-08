from controllers.home_controller import home
from controllers.users_controller import users
from controllers.products_controller import products


def register_controllers(app):
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(products, url_prefix='/products')
