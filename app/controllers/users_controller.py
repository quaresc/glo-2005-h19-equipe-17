from flask import Blueprint, jsonify, request
from infrastructure import UsersRepository

users = Blueprint('users', __name__)


@users.route("/", methods=["GET"])
def get_users():
    try:
        users = UsersRepository.get_users()
        return jsonify(users)
    except Exception:
        return jsonify(message=f"An error has occured"), 500


@users.route("/<id>", methods=["GET"])
def get_user(id):
    try:
        user = UsersRepository.get_user(id)
        if not user:
            return jsonify(message=f"User '{id}' does not exist."), 400
        return jsonify(user)
    except Exception:
        return jsonify(message=f"An error has occured"), 500


@users.route("/<id>/invoices", methods=["GET"])
def get_invoice(id):
    try:
        invoice = UsersRepository.get_invoice(id)
        if not invoice:
            return jsonify(message=f"Invoice  with user '{id}' does not exist."), 400
        return jsonify(invoice)
    except Exception:
        return jsonify(message=f"An error has occured"), 500


@users.route("/invoice/<id>", methods=["GET"])
def get_invoiceById(id):
    try:
        invoice = UsersRepository.get_invoiceById(id)
        if not invoice:
            return jsonify(message=f"Invoice '{id}' does not exist."), 400
        return jsonify(invoice)
    except Exception:
        return jsonify(message=f"An error has occured"), 500


@users.route("/<userId>/cart/<productId>", methods=["POST"])
def add_product_to_cart(userId, productId):
    cart = get_cart_quantity()
    try:
        UsersRepository.add_product_to_cart(userId, productId, cart)
        return "", 201
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
    try:
        products = UsersRepository.get_cart(userId)
        return jsonify(products=products)
    except Exception:
        return jsonify(message=f"An error has occured"), 500


@users.route("/<userId>/cart/<productId>", methods=["PATCH"])
def update_cart_quantity(userId, productId):
    try:
        request_data = request.get_json()
        quantity = request_data['quantity']
        if quantity is not None:
            UsersRepository.update_cart_quantity(userId, productId, quantity)
        return '', 204
    except Exception:
        return jsonify(message=f"An error has occured"), 500


@users.route("/<userId>/cart/<productId>", methods=["DELETE"])
def delete_product_from_cart(userId, productId):
    try:
        UsersRepository.delete_product_from_cart(userId, productId)
        return "", 200
    except Exception:
        return jsonify(message=f"An error has occured"), 500


@users.route("/<userId>/cart", methods=["DELETE"])
def delete_cart(userId):
    try:
        UsersRepository.delete_cart(userId)
        return "", 200
    except Exception:
        return jsonify(message=f"An error has occured"), 500


@users.route("/<userId>/purchase", methods=["POST"])
def submit_cart(userId):
    try:
        UsersRepository.create_invoice(userId)
        invoiceId = UsersRepository.get_invoice_id(userId)
        products = get_cart_info()
        UsersRepository.create_invoice_products(userId, products, invoiceId)
        UsersRepository.delete_cart(userId)
        return "", 200
    except Exception:
        return jsonify(message=f"An error has occured"), 500


def get_cart_info():
    request_data = request.get_json()
    products = request_data['products']
    products = {
        "products": products,
    }
    return products
