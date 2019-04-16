import pymysql.cursors
from config import create_connection


class DepartmentsRepository:

    def get_departments():
        sql_query = (
            """
            SELECT name FROM `product_types`
            """)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query)
            return cursor.fetchall()
        finally:
            connection.close()
