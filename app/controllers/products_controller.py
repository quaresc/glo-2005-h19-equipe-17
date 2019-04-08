from flask import Blueprint, jsonify, request
from infrastructure import ProductsRepository
from math import ceil

products = Blueprint('products', __name__)

DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 20


@products.route("/", methods=["GET"])
def get_products():
    page, perPage = get_pagination()
    products = ProductsRepository.get_products(page, perPage)
    total_products = ProductsRepository.get_total_products()
    total_pages = ceil(total_products / perPage)
    return jsonify(products=products, total_products=total_products, total_pages=total_pages)


def get_pagination():
    page = request.args.get('page') or DEFAULT_PAGE
    perPage = request.args.get('perPage') or DEFAULT_PER_PAGE
    return int(page), int(perPage)
