from flask import Blueprint, jsonify, request
from infrastructure import DepartmentsRepository

departments = Blueprint('departments', __name__)


@departments.route("/", methods=["GET"])
def get_departments():
    try:
        departments = DepartmentsRepository.get_departments()
        return jsonify(departments=departments)
    except Exception:
        return jsonify(message=f"An error has occured"), 500
