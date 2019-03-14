from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.UserModel import UserModel

app = Flask("GLO-2005")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@database/glo_2005'
db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route("/", methods=["GET"])
def index():
    users = UserModel.get_users()
    if users is None:
        return jsonify(message='No users in database.')
    return jsonify(users)


app.run(host="0.0.0.0", port=3000)
