from flask import Blueprint, jsonify, request
from infrastructure import ProductsRepository
from math import ceil

products = Blueprint('products', __name__)

DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 20
DEFAULT_RATING = 0


@products.route("/", methods=["GET"])
def get_products():
    try:
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
    except Exception:
        return jsonify(message=f"Cannot fetch products"), 500


@products.route("/department/<department>", methods=["GET"])
def get_departement_products(department):
    try:
        filters = get_filters()
        products = ProductsRepository.get_department_products(
            filters, department)
        total_products = ProductsRepository.get_total_departments_products(
            filters, department)
        total_pages = ceil(total_products / filters['perPage'])
        return jsonify(products=products, total_products=total_products, total_pages=total_pages)
    except Exception:
        return jsonify(message=f"Cannot fetch {department} products."), 500


@products.route("/<id>", methods=["GET"])
def get_product(id):
    try:
        product = ProductsRepository.get_product(id)
        return jsonify(product=product)
    except Exception:
        return jsonify(message=f"Cannot fetch product {id}."), 500


@products.route("/<id>/reviews", methods=["GET"])
def get_product_reviews(id):
    try:
        filters = get_filters()
        product_reviews = ProductsRepository.get_product_reviews(id, filters)
        total_product_reviews = ProductsRepository.get_total_product_reviews(
            id)
        total_pages = ceil(total_product_reviews / filters['perPage'])
        return jsonify(product_reviews=product_reviews, total_product_reviews=total_product_reviews, total_pages=total_pages)
    except Exception:
        return jsonify(message=f"Cannot fetch reviews for product {id}."), 500


@products.route("/<productId>/reviews/<userId>", methods=["PUT"])
def add_product_review(productId, userId):
    try:
        review = get_review()
        ProductsRepository.add_product_review(productId, userId, review)
        return "", 201
    except RuntimeError:
        return jsonify(message=f"You already added a review for this product."), 400
    except Exception:
        return jsonify(message=f"Cannot add a review for product {productId}."), 500


def get_review():
    request_data = request.get_json()
    title = request_data['review']['title']
    comment = request_data['review']['comment']
    rating = request_data['review']['rating']
    review = {
        "title": title,
        "comment": comment,
        "rating": rating
    }
    return review


def get_filters():
    page = request.args.get('page') or DEFAULT_PAGE
    perPage = request.args.get('perPage') or DEFAULT_PER_PAGE
    rating = request.args.get('rating') or DEFAULT_RATING
    search = request.args.get('search') or None
    filters = {
        'page': int(page),
        'perPage': int(perPage),
        'rating': int(rating),
        'search': search
    }
    return filters
