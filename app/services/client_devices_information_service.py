from app.modules.devices_filter import filter_devices_by_client_id


def filter_network_devices_by_client_id(client_id, filter, filter_param):
    devices = filter_devices_by_client_id(client_id, filter, filter_param)
    return devices
