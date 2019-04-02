from controllers.home_controller import home
from controllers.users_controller import users


def register_controllers(app):
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(users, url_prefix='/users')
