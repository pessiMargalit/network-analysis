from data.db_service import get_from_db


@get_from_db
def get_most_frequent_protocols(network_id):
    query = """SELECT protocol.protocol_type, COUNT(*) AS protocol_count
                FROM device_connection
                JOIN protocol ON protocol.connection_id = device_connection.id
                WHERE device_connection.network_id = %s
                GROUP BY protocol.protocol_type
                ORDER BY protocol_count DESC
                LIMIT 1;"""
    return query, network_id

# @get_from_db
# def get_when_last_packet_received_or_sent(network_id):
#     query = """SELECT protocol.protocol_type, COUNT(*) AS protocol_count
#                 FROM device_connection
#                 JOIN protocol ON protocol.connection_id = device_connection.id
#                 WHERE device_connection.network_id = %s
#                 GROUP BY protocol.protocol_type
#                 ORDER BY protocol_count DESC
#                 LIMIT 1;"""
#     return query, network_id
