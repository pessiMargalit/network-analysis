
import pymysql


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

    return connectionObject
# try:
#
#     # Create a cursor object
#     cursorObject = connectionObject.cursor()
#
#     # SQL query string
#     sqlQuery = "CREATE TABLE Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"
#
#     # Execute the sqlQuery
#     cursorObject.execute(sqlQuery)
#
#     # SQL query string
#     sqlQuery = "show tables"
#
#     # Execute the sqlQuery
#     cursorObject.execute(sqlQuery)
#
#     # Fetch all the rows
#     rows = cursorObject.fetchall()
#
#     for row in rows:
#         print(row)
#
# except Exception as e:
#
#     print("Exeception occured:{}".format(e))
#
# finally:
#
#     connectionObject.close()