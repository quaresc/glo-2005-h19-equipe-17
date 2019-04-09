from flask import Blueprint, jsonify, request
from infrastructure import ProductsRepository
from math import ceil

products = Blueprint('products', __name__)

DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 20
DEFAULT_RATING = 0


@products.route("/", methods=["GET"])
def get_products():
    filters = get_filters()
    products = ProductsRepository.get_products(filters)
    total_products = ProductsRepository.get_total_products()
    total_pages = ceil(total_products / filters['perPage'])
    return jsonify(products=products, total_products=total_products, total_pages=total_pages)


def get_filters():
    page = request.args.get('page') or DEFAULT_PAGE
    perPage = request.args.get('perPage') or DEFAULT_PER_PAGE
    rating = request.args.get('rating') or DEFAULT_RATING
    filters = {
        "page": int(page),
        "perPage": int(perPage),
        "rating": int(rating)
    }
    return filters
