import configparser
import os

import pymysql
from passlib.handlers import mysql

active_connection = None


def get_connection():
    return active_connection if active_connection else connect_to_db()


def disconnect():
    get_connection().close()


# Create a connection object
def connect_to_db():
    dbServerName = "sql6.freesqldatabase.com"

    dbUser = "sql6636743"

    dbPassword = "WXNh4lu6iq"

    dbName = "sql6636743"

    charSet = "utf8mb4"

    cusrorType = pymysql.cursors.DictCursor

    connectionObject = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,

                                       db=dbName, charset=charSet, cursorclass=cusrorType)
    active_connection = connectionObject
    return active_connection


# def connect_to_db():
#     config_data = configparser.ConfigParser()
#     root_dir = os.path.dirname(
#         os.path.abspath(__file__)
#     )
#     config_data.read(f"{root_dir}/db_config.ini")
#     database = config_data["database"]
#     active_connection = mysql.connector.connect(
#         user=database["user"],
#         database=database["database"],
#         password=database["password"])
#     return active_connection