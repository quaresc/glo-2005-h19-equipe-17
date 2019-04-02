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
