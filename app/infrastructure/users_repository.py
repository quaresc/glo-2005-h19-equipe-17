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
        sql_query = ("SELECT * FROM users WHERE id=%s")
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

    def get_invoice(id):
        sql_query = ("select t2.id as id_invoice , t2.transaction_date, sum(t3.price * t1.quantity) as montant from  invoice_products as t1 inner join invoices  as t2 on  t2.id = t1.invoice_id inner join  products  as t3 on  t3.id = t1.product_id  and t2.user_id= %s group by  t2.id, t2.transaction_date order by  t2.transaction_date DESC")
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (id))
            return cursor.fetchall()
        finally:
            connection.close()

    def get_invoiceById(id):
        sql_query = ("SELECT * FROM invoices WHERE id=%s")
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql_query, (id))
            invoice = cursor.fetchone()
            if not invoice:
                return None
            return {'id': invoice['id'],'at': invoice['transaction_date']}
        finally:
            connection.close()
