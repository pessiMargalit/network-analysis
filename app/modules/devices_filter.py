import pymysql
import asyncio
from data.db_connection_server import connect_to_db
from data.db_creation import get_from_db

connection = connect_to_db()
# async def filter_devices(network_id, filter1, filter_param):
#     pass


@get_from_db
def filter_devices_by_client_id(client_id, filter_param=None, filter_name=None):
    if filter_name == None or filter_param == None:
        values = client_id
        query_to_filter = """
                SELECT *
            FROM device
            WHERE device.network_id IN (
                SELECT *
                FROM network AS n
                WHERE n.client_id = %s 
            )"""
    else:
        values = (client_id, filter_param)
        query_to_filter = """SELECT *
                FROM device
                WHERE device.network_id IN (
                    SELECT *
                    FROM network AS n
                    WHERE n.client_id = %s 
                )
                AND {} = %s
                ;""".format(filter_name)
    return query_to_filter, values


@get_from_db
def filter_devices_by_network_id(network_id, filter_param=None, filter_name=None):
    if filter_name == None or filter_param == None:
        values = network_id
        query_to_filter = """
                SELECT *
                FROM device
                WHERE network_id = %s"""
    else:
        values = (network_id, filter_param)
        query_to_filter = """
            SELECT *
            FROM device
            WHERE network_id = %s
            AND {} = %s
            """.format(filter_name)
    return query_to_filter, values


# print(filter_devices_by_network_id(1, "Hewlett Packard", "vendor"))
# print(filter_devices_by_client_id(1, "vendor"))
