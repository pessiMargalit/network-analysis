import asyncio

from data.db_connection_server import connect_to_db

connection = connect_to_db()


async def get_network_devices_connections(network_id):
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
            con.network_id = {network_id};
        """
    async with connection.cursor() as cursor:
        await cursor.execute(query_to_filter)
        devices = await cursor.fetchall()
        return devices
    # print(devices)


async def main():
    data = await get_network_devices_connections(2)
    print(data)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())

# get_all(table_name)
# get(guery)
# insert(query)
# update(query)