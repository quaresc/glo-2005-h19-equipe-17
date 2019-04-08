import pymysql.cursors
from config import connection

PRODUCTS_TABLE = "products"
PRODUCTS_TYPES_TABLE = "product_types"


class ProductsRepository:

    def get_products(page, perPage):
        offset = (page - 1) * perPage
        sql_query = (
            f"""
            SELECT p.ean, p.name, p.description, pt.name AS type, p.company, p.price, p.rating, p.weight, p.quantity, p.image_url
            FROM {PRODUCTS_TABLE} AS p INNER JOIN {PRODUCTS_TYPES_TABLE} AS pt ON
            p.product_type_id=pt.id ORDER BY p.id LIMIT {offset}, {perPage}
            """)
        cursor = connection.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()

    def get_total_products():
        sql_query = ("SELECT COUNT(id) AS total FROM products")
        cursor = connection.cursor()
        cursor.execute(sql_query)
        return int(cursor.fetchone()["total"])
