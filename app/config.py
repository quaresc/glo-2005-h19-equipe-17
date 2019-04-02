import pymysql

connection = pymysql.connect(host='database',
                             user='root',
                             password='root',
                             db='glo_2005',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
