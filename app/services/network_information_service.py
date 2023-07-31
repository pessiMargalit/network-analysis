from app.modules.devices_filter import filter_devices_by_network_id


def filter_network_devices(network_id, filter, filter_param):
    devices = filter_devices_by_network_id(network_id, filter, filter_param)
    return devices
