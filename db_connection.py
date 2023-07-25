import pymysql


def connect_to_db():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="it4all",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )

    if connection.open:
        print("the connection is opened")
        return connection
