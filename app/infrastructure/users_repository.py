import pymysql.cursors
from config import connection


class UsersRepository:

    def get_users():
        sql_get_users = ("SELECT `*` FROM `users`")

        cursor = connection.cursor()
        cursor.execute(sql_get_users)
        return [{
            'id': user['id'],
            'firstName': user['first_name'],
            'lastName': user['last_name'],
            'age': user['age']}
            for user in cursor]

    def get_user(id):
        sql_get_user = ("SELECT `*` FROM `users` WHERE `id`=%s")

        cursor = connection.cursor()
        cursor.execute(sql_get_user, (id))
        user = cursor.fetchone()
        if not user:
            return None
        return {'firstName': user['first_name'],
                'lastName': user['last_name'],
                'age': user['age']}
