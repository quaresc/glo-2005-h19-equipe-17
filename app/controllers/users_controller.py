from flask import Blueprint, jsonify, request
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
    cart = get_cart_quantity()
    try:
        UsersRepository.add_product_to_cart(userId, productId, cart)
        return "Ok"
    except Exception:
        return "Duplicate"


def get_cart_quantity():
    request_data = request.get_json()
    quantity = request_data['cart']['quantity']
    cart = {
        "quantity": quantity,
    }
    return cart


@users.route("/<userId>/cart", methods=["GET"])
def get_cart(userId):
    products = UsersRepository.get_cart(userId)
    return jsonify(products=products)


@users.route("/<userId>/cart/<productId>", methods=["PATCH"])
def update_cart_quantity(userId, productId):
    request_data = request.get_json()
    quantity = request_data['quantity']
    if quantity is not None:
        UsersRepository.update_cart_quantity(userId, productId, quantity)
    return '', 204


@users.route("/<userId>/cart/<productId>", methods=["DELETE"])
def delete_product_from_cart(userId, productId):
    UsersRepository.delete_product_from_cart(userId, productId)
    return "Ok"


@users.route("/<userId>/cart", methods=["DELETE"])
def delete_cart(userId):
    UsersRepository.delete_cart(userId)
    return "Ok"


@users.route("/<userId>/purchase", methods=["POST"])
def submit_cart(userId):
    UsersRepository.create_invoice(userId)
    invoiceId = UsersRepository.get_invoice_id(userId)
    products = get_cart_info()
    UsersRepository.create_invoice_products(userId, products, invoiceId)
    return "Ok"

def get_cart_info():
    request_data = request.get_json()
    products = request_data['cart']['products']
    cart = {
        "products": products,
    }
    return cart
