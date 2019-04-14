import pymysql
from config import create_connection


USERS_TABLE = "users"
CARTS_TABLE = "carts"
PRODUCTS_TABLE = "products"


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

    def get_cart(userId):
        sql_query = (
            f"""
            SELECT p.id, p.name, p.company, p.rating, p.image_url, p.price, c.quantity AS quantity
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {CARTS_TABLE} AS c ON
            p.id=c.product_id
            WHERE c.user_id={userId}
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query)
            return cursor.fetchall()
        finally:
            connection.close()

    def update_cart_quantity(userId, productId, quantity):
        sql_query = (
            f"""
            UPDATE {CARTS_TABLE}
            SET quantity = {quantity}
            WHERE user_id = {userId} AND product_id = {productId};
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query)
            connection.commit()
            return "Ok"
        finally:
            connection.close()
