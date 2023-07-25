from app.modules.devices_filter import filter_devices as filter_devices


async def filter_network_devices(network_id, filter, filter_param):
    devices = await filter_devices(network_id, filter, filter_param)
    return devices
