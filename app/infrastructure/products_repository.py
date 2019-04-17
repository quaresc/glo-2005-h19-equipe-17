import pymysql
from config import create_connection


class ProductsRepository:

    def get_products(filters):
        offset = (filters['page'] - 1) * filters['perPage']
        sql_query = (
            """
            SELECT p.id, p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM `products` AS p INNER JOIN `product_types` AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= %s
            ORDER BY p.id LIMIT %s, %s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(
                sql_query, (filters['rating'], offset, filters['perPage']))
            return cursor.fetchall()
        except pymysql.Error:
            raise Exception("Something went wrong")
        finally:
            connection.close()

    def get_department_products(filters, department):
        offset = (filters['page'] - 1) * filters['perPage']
        sql_query = (
            """
            SELECT p.id, p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM `products` AS p INNER JOIN `product_types` AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= %s
            AND pt.name = %s
            ORDER BY p.id LIMIT %s, %s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (
                filters['rating'], department, offset, filters['perPage']))
            return cursor.fetchall()
        except pymysql.Error:
            raise Exception("Something went wrong")
        finally:
            connection.close()

    def search_products(filters, search):
        offset = (filters['page'] - 1) * filters['perPage']
        sql_query = (
            """
            SELECT p.id, p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM `products` AS p INNER JOIN `product_types` AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= %s
            AND p.name LIKE %s
            ORDER BY p.id LIMIT %s, %s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(
                sql_query, (filters['rating'], "%" + search + "%", offset, filters['perPage']))
            return cursor.fetchall()
        except pymysql.Error:
            raise Exception("Something went wrong")
        finally:
            connection.close()

    def get_total_products(filters):
        sql_query = (
            """
            SELECT COUNT(p.id) AS total
            FROM `products` AS p
            WHERE p.rating >= %s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (filters['rating'],))
            return int(cursor.fetchone()["total"])
        except pymysql.Error:
            raise Exception("Something went wrong")
        finally:
            connection.close()

    def get_total_departments_products(filters, department):
        sql_query = (
            """
            SELECT COUNT(p.id) AS total
            FROM `products` AS p INNER JOIN `product_types` AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= %s
            AND pt.name = %s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (filters['rating'], department))
            return int(cursor.fetchone()["total"])
        except pymysql.Error:
            raise Exception("Something went wrong")
        finally:
            connection.close()

    def get_product(productId):
        sql_query = (
            """
            SELECT p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM `products` AS p INNER JOIN `product_types` AS pt
            ON p.product_type_id=pt.id
            WHERE p.id=%s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (productId,))
            return cursor.fetchone()
        except pymysql.Error:
            raise Exception("Something went wrong")
        finally:
            connection.close()

    def get_product_reviews(productId, filters):
        offset = (filters['page'] - 1) * filters['perPage']
        sql_query = (
            """
            SELECT u.username, r.id, r.title, r.comment, r.rating, r.timestamp
            FROM `products` p, `reviews` r, `users` u
            WHERE p.id=%s && r.user_id=u.id && r.product_id=p.id
            ORDER BY r.id DESC
            LIMIT %s, %s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (productId, offset, filters['perPage']))
            return cursor.fetchall()
        except pymysql.Error:
            raise Exception("Something went wrong")
        finally:
            connection.close()

    def get_total_searched_products(filters, search):
        sql_query = (
            """
            SELECT COUNT(p.id) AS total
            FROM `products` AS p INNER JOIN `product_types` AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= %s
            AND p.name LIKE %s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (filters['rating'], "%" + search + "%"))
            return int(cursor.fetchone()["total"])
        except pymysql.Error:
            raise Exception("Something went wrong")
        finally:
            connection.close()

    def get_total_product_reviews(productId):
        sql_query = (
            """
            SELECT COUNT(r.id) AS total
            FROM `reviews` AS r
            WHERE r.product_id=%s
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (productId, ))
            return int(cursor.fetchone()["total"])
        except pymysql.Error:
            raise Exception("Something went wrong")
        finally:
            connection.close()

    def add_product_review(productId, userId, review):
        sql_query = (
            """
            INSERT INTO `reviews` (user_id, product_id, title, comment, rating)
            VALUES(%s, %s, %s, %s, %s)
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (userId, productId,
                                       review['title'], review['comment'], review['rating']))
            connection.commit()
        except pymysql.err.IntegrityError:
            raise RuntimeError('Duplicate')
        finally:
            connection.close()
