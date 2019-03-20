import os
import pymysql.cursors
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask("GLO-2005")
connection = pymysql.connect(host='database',
                             user='root',
                             password='root',
                             db='glo_2005',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

CORS(app)


@app.route("/", methods=["GET"])
def index():
    return "GLO-2005-Equipe-17 API"


@app.route("/users", methods=["GET"])
def get_users():
    sql_get_users = ("SELECT `*` FROM `users`")

    cursor = connection.cursor()
    cursor.execute(sql_get_users)

    users = cursor.fetchall()
    return jsonify(users)


@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    sql_get_user = ("SELECT `*` FROM `users` WHERE `id`=%s")

    cursor = connection.cursor()
    cursor.execute(sql_get_user, (id))

    user = cursor.fetchone()

    if not user:
        return jsonify(message=f"User '{id}' does not exist."), 400
    return jsonify(user)


app.run(host="0.0.0.0", port=os.environ['PORT'])
