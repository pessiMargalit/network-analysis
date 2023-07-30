import pymysql
import asyncio
from data.db_connection_server import connect_to_db
from data.db_creation import get_from_db

connection = connect_to_db()


# async def filter_devices(network_id, filter1, filter_param):
#     pass
#
#
# def filter_devices_by_network_id(network_id, filter1, filter_param):
#         with connection.cursor() as cursor:
#             sql_query = "SELECT * FROM device WHERE id = %s AND %s = %s;"
#             params = (network_id, filter1, filter_param)
#             results = cursor.execute_query_with_params(sql_query,params)
#         return results
#
#
# def filter_devices_by_client_id(client_id, filter1, filter_param):
#     async with connection.cursor() as cursor:
#         sql_query = """SELECT *
#             FROM device
#             WHERE device.network_id IN (
#                 SELECT *
#                 FROM network AS n
#                 WHERE n.client_id = {client_id} -- Replace {client_id} with the desired client_id value
#             );"""
#         params = (client_id, filter1, filter_param)
#         results = cursor.execute_query_with_params(sql_query, params)
#     return results
#
#
#

#
#
@get_from_db
def filter_devices_by_network_id(network_id,filter_name, filter_param):
    values = (network_id, filter_param)
    query_to_filter = """
        SELECT *
        FROM device
        WHERE network_id = %s
        AND {} = %s;
        """.format(filter_name)
    with connection.cursor() as cursor:
        cursor.execute(query_to_filter,values)
        devices = cursor.fetchall()
        return devices




def execute_queries(query_to_filter):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(query_to_filter)
        devices = cursor.fetchall()
        return devices

print(filter_devices_by_network_id(1,"vendor", "Hewlett Packard"))
# async def fun():
#     data = await filter_devices_by_network_id(2, "vendor", "Hewlett Packard")
#     print(data)
#
#
# asyncio.run(fun())

# import asyncio
# import aiomysql
# from data.db_connection_server import connect_to_db
#
# async def filter_devices_by_network_id(network_id, filter_name, filter_param):
#     query_to_filter = f"""
#         SELECT *
#         FROM device
#         WHERE id = {network_id}
#         AND {filter_name} = '{filter_param}';
#         """
#     result = await execute_queries(query_to_filter)
#     return result
#
# async def execute_queries(query_to_filter):
#     async with aiomysql.create_pool(connect_to_db()) as pool:
#         async with pool.acquire() as connection:
#             async with connection.cursor(aiomysql.DictCursor) as cursor:
#                 await cursor.execute(query_to_filter)
#                 devices = await cursor.fetchall()
#                 return devices
#
# async def fun():
#     data = await filter_devices_by_network_id(2, 'vendor', 'COMPAL INFORMATION (KUNSHAN) CO., LTD.')
#     print(data)
#
# asyncio.run(fun())
