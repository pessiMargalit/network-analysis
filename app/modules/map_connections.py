import asyncio
from data.db_service import get_from_db


@get_from_db
def get_network_devices_connections(network_id):
    print("--------------------get_network_devices_connections-----------------------------")
    query_to_filter = f"""
        SELECT
            src.MAC_address AS source_MAC,
            src.vendor AS source_vendor,
            dst.MAC_address AS destination_MAC,
            dst.vendor AS destination_vendor
        FROM
            device_connection AS con
        JOIN
            device AS src ON con.source = src.id
        JOIN
            device AS dst ON con.destination = dst.id
        WHERE
            con.network_id = %s;
        """
    return query_to_filter, network_id
