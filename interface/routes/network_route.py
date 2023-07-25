from app.services.capture_file_service import create_network as create_network
from app.services.network_information_service import filter_network_devices as filter_network_devices
from app.services.device_connection_service import view_network_map as view_network_map
from app.services.client_devices_information_service import filter_network_devices as filter_network_devices

print("Hello")
from app_server import app

BASE_PATH = "/network/"


@app.post(f"{BASE_PATH}upload")
async def upload_capture_file(cap_file, client_id, date_taken, premise_name, technician_name):
    return await create_network(cap_file, client_id, date_taken, premise_name, technician_name)


@app.get(f"{BASE_PATH}view/:network_id")
async def view_device_connection(network_id):
    return await view_network_map(network_id)


@app.get(f"{BASE_PATH}view/:network_id")
async def view_network_devices_by_filter(network_id, filter: str = None, filter_param: str = None):
    return await filter_network_devices(network_id, filter, filter_param)


@app.get(f"/view/client/:client_id")
# TODO: Change the route
async def view_client_devices_by_filter(client_id, filter: str = None, filter_param: str = None):
    return await filter_network_devices(client_id, filter, filter_param)
