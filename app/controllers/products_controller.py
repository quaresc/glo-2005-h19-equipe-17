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
    if filters['search'] is None:
        products = ProductsRepository.get_products(filters)
        total_products = ProductsRepository.get_total_products(filters)
    else:
        products = ProductsRepository.search_products(
            filters, filters['search'])
        total_products = ProductsRepository.get_total_searched_products(
            filters, filters['search'])
    total_pages = ceil(total_products / filters['perPage'])
    return jsonify(products=products, total_products=total_products, total_pages=total_pages)


@products.route("/department/<department>", methods=["GET"])
def get_departement_products(department):
    filters = get_filters()
    products = ProductsRepository.get_department_products(filters, department)
    total_products = ProductsRepository.get_total_departments_products(
        filters, department)
    total_pages = ceil(total_products / filters['perPage'])
    return jsonify(products=products, total_products=total_products, total_pages=total_pages)


def get_filters():
    page = request.args.get('page') or DEFAULT_PAGE
    perPage = request.args.get('perPage') or DEFAULT_PER_PAGE
    rating = request.args.get('rating') or DEFAULT_RATING
    search = request.args.get('search') or None
    filters = {
        "page": int(page),
        "perPage": int(perPage),
        "rating": int(rating),
        "search": search
    }
    return filters
