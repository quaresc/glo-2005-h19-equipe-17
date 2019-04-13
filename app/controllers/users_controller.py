from flask import Blueprint, jsonify
from infrastructure import UsersRepository

users = Blueprint('users', __name__)


@users.route("/", methods=["GET"])
def get_users():
    users = UsersRepository.get_users()
    return jsonify(users)


@users.route("/<id>", methods=["GET"])
def get_user(id):
    user = UsersRepository.get_user(id)
    if not user:
        return jsonify(message=f"User '{id}' does not exist."), 400
    return jsonify(user)


@users.route("/<userId>/cart/<productId>", methods=["POST"])
def add_product_to_cart(userId, productId):
    try:
        UsersRepository.add_product_to_cart(userId, productId)
        return "Ok"
    except Exception:
        return "Duplicate"
