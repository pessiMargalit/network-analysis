from app.modules.devices_filter import filter_devices_by_network_id


async def filter_network_devices(network_id, filter, filter_param):
    devices = await filter_devices_by_network_id(network_id, filter, filter_param)
    return devices
