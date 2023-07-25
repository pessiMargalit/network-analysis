from data.db_connection import connect_to_db

connection = connect_to_db()


def get_network_devices_connections(network_id):
    query_to_filter = """
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
            con.network_id = %d;
        """
    with connection.cursor() as cursor:
        cursor.execute(query_to_filter, 1)
        # Fetch all the results
        devices = cursor.fetchall()
    # Print the results
    print(devices)


get_network_devices_connections(1)
