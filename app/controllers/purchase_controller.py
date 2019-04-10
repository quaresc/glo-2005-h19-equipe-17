from flask import Blueprint, jsonify, request


@products.route("/users/<id>/history", methods=["GET"])
def get_purchase():
    return jsonify(products=products, total_products=total_products, total_pages=total_pages)
