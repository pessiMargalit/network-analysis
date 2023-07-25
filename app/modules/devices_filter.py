import pymysql
from data.db_connection import connect_to_db
connection = connect_to_db()
async def filter_devices(network_id, filter, filter_param):
    pass


async def filter_devices_by_network_id(network_id, filter, filter_param):
        with connection.cursor() as cursor:
            sql_query = "SELECT * FROM device WHERE id = %s AND %s = %s;"
            params = (network_id, filter, filter_param)
            results = cursor.execute_query_with_params(sql_query,params)
        return results

async def filter_devices_by_client_id(client_id, filter, filter_param):
    pass
