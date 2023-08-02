import pymysql
import asyncio

from data.db_connection import connect_to_db
from data.db_service import get_from_db

connection = connect_to_db()

@get_from_db
def filter_devices(id, query_with_param, query_without_param, filter_name=None, filter_param=None):
    if not filter_name or not filter_param:
        values = id
        query_to_filter = query_without_param
    else:
        values = (id, filter_param)
        query_to_filter = query_with_param
    return query_to_filter, values


def filter_devices_by_client_id(client_id, filter_name=None, filter_param=None):
    query_to_filter_without_param = """
            SELECT *
            FROM device
            WHERE device.network_id IN (
                SELECT *
                FROM network AS n
                WHERE n.client_id = %s 
            )"""

    query_to_filter_with_param = """SELECT *
                        FROM device
                        WHERE device.network_id IN (
                            SELECT network_id
                            FROM network
                            WHERE client_id = %s 
                        )
                        AND {} = %s
                        ;""".format(filter_name)
    return filter_devices(client_id, query_to_filter_with_param, query_to_filter_without_param, filter_name, filter_param)


def filter_devices_by_network_id(network_id, filter_name=None, filter_param=None):
    query_to_filter_without_param = """
                SELECT *
                FROM device
                WHERE network_id = %s"""


    query_to_filter_with_param = """
        SELECT *
        FROM device
        WHERE network_id = %s
        AND {} = %s
        """.format(filter_name)
    return filter_devices(network_id, query_to_filter_with_param, query_to_filter_without_param, filter_name, filter_param)
