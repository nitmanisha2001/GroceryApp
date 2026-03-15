import mysql.connector

__cnx = None


def get_sql_connection():
    global __cnx
    __cnx = mysql.connector.connect(user='root',password='root',host='127.0.0.1',database='gs', use_pure=True)
    return __cnx