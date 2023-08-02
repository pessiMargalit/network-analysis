from app.modules.devices_filter import filter_devices_by_client_id
from infrastructure.exceptions.exception_handler import basic_exception_handler


@basic_exception_handler
def filter_network_devices_by_client_id(client_id, filter, filter_param):
    devices = filter_devices_by_client_id(client_id, filter, filter_param)
    return devices
