import pymysql

active_connection = None


def get_connection():
    return active_connection if active_connection else connect_to_db()


def disconnect():
    get_connection().close()

# Create a connection object
def connect_to_db():
    dbServerName = "sql6.freesqldatabase.com"

    dbUser = "sql6635072"

    dbPassword = "tS6Z6mXSx1"

    dbName = "sql6635072"

    charSet = "utf8mb4"

    cusrorType = pymysql.cursors.DictCursor

    connectionObject = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,

                                       db=dbName, charset=charSet, cursorclass=cusrorType)
    active_connection = connectionObject
    return active_connection
