import datetime


async def insert_data_to_db(devices: dict, connections: dict, client_id, premise_name):
    is_network_insertion_success = await insert_new_network(client_id, premise_name)
    is_devices_insertion_success = await insert_devices(devices)
    is_devices_connections_insertion_success = await insert_devices_connections(connections)
    return True or False


async def insert_new_network(client_id, premise_name):
    date_taken = datetime.date.today()


async def insert_devices(devices):
    pass


async def insert_devices_connections(connections):
    pass


async def insert_client_id_into_technician_clients(client_id):
    pass
