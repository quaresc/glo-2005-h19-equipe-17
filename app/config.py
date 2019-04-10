import pymysql


def create_connection():
    return pymysql.connect(host='database',
                           user='administrator',
                           password='administrator1234',
                           db='glo_2005',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
