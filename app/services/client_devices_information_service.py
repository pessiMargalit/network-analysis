from app.modules.devices_filter import filter_devices_by_client_id


def filter_network_devices_by_clientid(network_id, filter_param, filter):
    devices = filter_devices_by_client_id(network_id, filter_param, filter)
    return devices
