import pymysql
from config import create_connection


class UsersRepository:

    def get_users():
        sql_query = (
            """
            SELECT id, first_name, last_name, username, email, password, INET_NTOA(ip_address)
            as ip_address, registration_date, activated
            FROM `users`
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
            """
            SELECT * FROM `users` WHERE id=%s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (id,))
            user = cursor.fetchone()
            if not user:
                return None
            return {'firstName': user['first_name'],
                    'lastName': user['last_name'], 'username': user['username']}
        finally:
            connection.close()

    def get_invoice(id):
        sql_query = (
            """
            SELECT t2.id AS id_invoice, t2.transaction_date, SUM(t3.price * t1.quantity) AS montant
            FROM `invoice_products` AS t1 INNER JOIN `invoices` AS
            t2 on t2.id = t1.invoice_id INNER JOIN `products` AS
            t3 on t3.id = t1.product_id AND t2.user_id=%s
            GROUP BY t2.id, t2.transaction_date ORDER BY t2.transaction_date DESC
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (id,))
            return cursor.fetchall()
        finally:
            connection.close()

    def get_invoiceById(id):
        sql_query = (
            """
            SELECT i.transaction_date, ip.invoice_id, p.name, ip.quantity, p.price
            FROM `invoice_products` AS ip, products AS p, `invoices` AS i
            WHERE invoice_id=%s AND ip.product_id=p.id AND ip.invoice_id=i.id
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (id,))
            return cursor.fetchall()
        finally:
            connection.close()

    def add_product_to_cart(userId, productId, cart):
        sql_query = (
            """
            INSERT INTO `carts` (user_id, product_id, quantity)
            VALUES(%s, %s, %s)
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (userId, productId, cart['quantity']))
            connection.commit()
            return "Ok"
        except pymysql.err.IntegrityError:
            raise Exception('Duplicate')
        finally:
            connection.close()

    def get_cart(userId):
        sql_query = (
            """
            SELECT p.id, p.name, p.company, p.rating, p.image_url, p.price, c.quantity AS quantity
            FROM `products` AS p INNER JOIN `carts` AS c ON
            p.id=c.product_id
            WHERE c.user_id=%s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (userId,))
            return cursor.fetchall()
        finally:
            connection.close()

    def delete_product_from_cart(userId, productId):
        sql_query = (
            """
            DELETE FROM `carts`
            WHERE user_id=%s && product_id=%s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (userId, productId))
            connection.commit()
            return "Ok"
        finally:
            connection.close()

    def delete_cart(userId):
        sql_query = (
            """
            DELETE FROM `carts`
            WHERE user_id=%s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (userId,))
            connection.commit()
            return "Ok"
        finally:
            connection.close()

    def create_invoice(userId):
        sql_query = (
            """
            INSERT INTO `invoices` (user_id)
            VALUES (%s)
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (userId,))
            connection.commit()
            return "Ok"
        finally:
            connection.close()

    def get_invoice_id(userId):
        sql_query = (
            """
            SELECT id FROM `invoices`
            WHERE user_id=%s
            ORDER BY transaction_date DESC
            LIMIT 1
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (userId,))
            return cursor.fetchone()
        finally:
            connection.close()

    def update_cart_quantity(userId, productId, quantity):
        sql_query = (
            """
            UPDATE `carts`
            SET quantity=%s
            WHERE user_id=%s AND product_id=%s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(
                sql_query, (quantity, userId, productId))
            connection.commit()
            return "Ok"
        finally:
            connection.close()

    def create_invoice_products_values_query(invoiceId, products):
        invoice_products_values = ""
        for product in products["products"]:
            invoice_products_values += "("
            invoice_products_values += str(invoiceId['id'])
            invoice_products_values += ","
            invoice_products_values += str(product['product']['productId'])
            invoice_products_values += ","
            invoice_products_values += str(product['product']['quantity'])
            invoice_products_values += "),"
        invoice_products_values = invoice_products_values[:-1]
        return invoice_products_values

    def create_invoice_products(userId, products, invoiceId):
        invoice_products_values = UsersRepository.create_invoice_products_values_query(
            invoiceId, products)
        sql_query = (
            f"""
            INSERT INTO `invoice_products` (invoice_id, product_id, quantity)
            VALUES {invoice_products_values}
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query)
            connection.commit()
            return "Ok"
        finally:
            connection.close()
