import pymysql.cursors
from config import connection

PRODUCTS_TABLE = "products"
PRODUCTS_TYPES_TABLE = "product_types"


class ProductsRepository:

    def get_products(filters):
        offset = (filters['page'] - 1) * filters['perPage']
        sql_query = (
            f"""
            SELECT p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            ORDER BY p.id LIMIT {offset}, {filters['perPage']}
            """)
        cursor = connection.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()

    def get_department_products(filters, department):
        offset = (filters['page'] - 1) * filters['perPage']
        sql_query = (
            f"""
            SELECT p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            AND pt.name = '{department}'
            ORDER BY p.id LIMIT {offset}, {filters['perPage']}
            """)
        cursor = connection.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()

    def get_total_products(filters):
        sql_query = (
            f"""
            SELECT COUNT(p.id) AS total
            FROM products AS p
            WHERE p.rating >= {filters['rating']}
            """)
        cursor = connection.cursor()
        cursor.execute(sql_query)
        return int(cursor.fetchone()["total"])

    def get_total_departments_products(filters, department):
        sql_query = (
            f"""
            SELECT COUNT(p.id) AS total
            FROM products AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id
            WHERE p.rating >= {filters['rating']}
            AND pt.name = '{department}'
            """)
        cursor = connection.cursor()
        cursor.execute(sql_query)
        return int(cursor.fetchone()["total"])
