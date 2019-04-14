import pymysql
from config import create_connection


USERS_TABLE = "users"
CARTS_TABLE = "carts"


class UsersRepository:

    def get_users():
        sql_query = (
            f"""
            SELECT id, first_name, last_name, username, email, password, INET_NTOA(ip_address)
            as ip_address, registration_date, activated
            FROM {USERS_TABLE}
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query)
            return cursor.fetchall()
        finally:
            connection.close()

    def get_user(id):
        sql_query = (
            f"""
            SELECT * FROM {USERS_TABLE} WHERE id=%s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (id))
            user = cursor.fetchone()
            if not user:
                return None
            return {'firstName': user['first_name'],
                    'lastName': user['last_name']}
        finally:
            connection.close()

    def add_product_to_cart(userId, productId, cart):
        sql_query = (
            f"""
            INSERT INTO {CARTS_TABLE} (user_id, product_id, quantity)
            VALUES({userId}, {productId}, {cart['quantity']})
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query)
            connection.commit()
            return "Ok"
        except pymysql.err.IntegrityError:
            raise Exception('Duplicate')
        finally:
            connection.close()
