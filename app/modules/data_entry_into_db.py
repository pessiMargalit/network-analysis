import datetime
import json

from data.db_service import insert_to_network, insert_to_device, insert_to_device_connection, get_from_db


async def insert_data_to_db(devices: dict, connections: dict, client_id, premise_name):
    network_id = await insert_new_network(client_id, premise_name)
    is_devices_insertion_success = await insert_devices(devices, network_id)
    is_devices_connections_insertion_success = await insert_devices_connections(connections, network_id)
    return is_devices_insertion_success and is_devices_connections_insertion_success


async def insert_new_network(client_id, premise_name):
    # date_taken = datetime.date.today()
    # network_id = insert_to_network((client_id, premise_name, date_taken))
    network_id = 17
    return network_id


async def insert_devices(devices, network_id):
    # for device, device_info in devices.items():
    #     mac_address = device
    #     ip_address = device_info['ip_address']
    #     vendor = device_info['vendor']
    #     id = insert_to_device((mac_address, ip_address, vendor, network_id))
    #     if not id:
    #         return False
    return True


@get_from_db
def get_device_id_by_mac_address(mac_address):
    query = "SELECT id FROM device WHERE MAC_address = %s"
    return query, mac_address


async def insert_devices_connections(connections, network_id):
    for (src_mac, dst_mac), protocols in connections.items():
        source = get_device_id_by_mac_address(src_mac)[0]['id']
        destination = get_device_id_by_mac_address(dst_mac)
        if destination:
            destination = destination[0]['id']
            # TODO: insert protocols in JSON format
            # protocols = json.dumps(list(protocols))
            protocols = list(protocols)[0]
            print((network_id, source, destination, protocols))
            insert_to_device_connection((network_id, source, destination, protocols))
    return True
