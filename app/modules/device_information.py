from data.db_service import get_from_db


@get_from_db
def get_device_protocols(device_id):
    query = """SELECT protocol.protocol_type
                FROM device
                JOIN device_connection ON device_connection.source = device.id OR device_connection.destination = device.id
                JOIN protocol ON protocol.connection_id = device_connection.id
                WHERE device.id = %s;"""
    return query, device_id
