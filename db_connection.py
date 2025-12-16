import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='tema2_db',
        port=3307,
        cursorclass=pymysql.cursors.Cursor
    )
