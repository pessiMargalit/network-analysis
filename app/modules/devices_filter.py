from data.db_service import get_from_db


@get_from_db
def filter_devices_by_client_id(client_id, filter_name=None, filter_param=None):
    if not filter_name or not filter_param:
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
def filter_devices_by_network_id(network_id, filter_name=None, filter_param=None):
    if not filter_name or not filter_param:
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


