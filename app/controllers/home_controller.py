from flask import Blueprint

home = Blueprint('home', __name__)


@home.route("/", methods=["GET"])
def get_users():
    return "GLO-2005-Equipe-17 API"
