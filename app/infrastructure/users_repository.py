import pymysql.cursors
from config import create_connection


class UsersRepository:

    def get_users():
        sql_query = (
            "SELECT id, first_name, last_name, username, email, password, INET_NTOA(ip_address) as ip_address, registration_date, activated FROM users")
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query)
            return cursor.fetchall()
        finally:
            connection.close()

    def get_user(id):
        sql_query = ("SELECT `*` FROM `users` WHERE `id`=%s")
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (id))
            user = cursor.fetchone()
            if not user:
                return None
            return {'firstName': user['first_name'],
                    'lastName': user['last_name'],
                    'age': user['age']}
        finally:
            connection.close()
