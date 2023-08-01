from typing import Tuple

from data.db_connection import connect_to_db
from functools import wraps

connection = connect_to_db()


def get_from_db(func):
    @wraps(func)
    def filter_by_query(*args, **kwargs):
        with connection.cursor() as cursor:
            query_and_values = func(*args, **kwargs)
            cursor.execute(query_and_values[0], query_and_values[1])
            res = cursor.fetchall()

        return res

    return filter_by_query


def insert_to_db(func):
    @wraps(func)
    def insert_by_query(*args, **kwargs):
        with connection.cursor() as cursor:
            query_and_values = func(*args, **kwargs)
            cursor.execute(query_and_values[0], query_and_values[1])
            connection.commit()
            id = cursor.lastrowid
        return id

    return insert_by_query


@get_from_db
def get_all(table_name):
    query = f"SELECT * FROM {table_name}"
    return query, None


@get_from_db
def get(query):
    return query


@insert_to_db
def insert_to_technician(values):
    query = "INSERT INTO technician (name, email, password) VALUES (%s,%s,%s)"
    return query, values


@insert_to_db
def insert_to_client(values):
    query = "INSERT into client (name) values (%s)"
    return query, values


@insert_to_db
def insert_to_network(values):
    query = "INSERT INTO network (client_id, premise, date) values (%s, %s, %s)"
    return query, values


@insert_to_db
def insert_to_device(values):
    query = "INSERT INTO device (MAC_address, ip_address, vendor, network_id) values (%s, %s, %s, %s)"
    return query, values


@insert_to_db
def insert_to_device_connection(values: Tuple):
    query = "INSERT INTO device_connection (network_id, source, destination) values (%s, %s, %s)"
    return query, values


@insert_to_db
def insert_to_technician_clients(values):
    query = "INSERT INTO technician_clients (technician_id, client_id) values (%s, %s)"
    return query, values


@insert_to_db
def insert_to_protocol(values):
    query = "INSERT INTO protocol (connection_id, protocol_type) values (%s, %s)"
    return query, values
