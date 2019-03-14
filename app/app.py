from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.UserModel import UserModel

app = Flask("GLO-2005")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@database/glo_2005'
db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)


@app.route("/", methods=["GET"])
def index():
    return "GLO-2005-Equipe-17 API"


@app.route("/users", methods=["GET"])
def get_users():
    users = UserModel.get_users()
    return jsonify(users)


@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = UserModel.get_user(id)
    if not user:
        return jsonify(message=f"User '{id}' does not exist."), 400
    return jsonify(user)


app.run(host="0.0.0.0", port=3000)
