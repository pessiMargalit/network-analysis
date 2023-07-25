from app.modules.devices_filter import filter_devices as filter_devices


# TODO: Check if to merge this file and client_devices_information_service to one
async def filter_network_devices(network_id, filter, filter_param):
    devices = await filter_devices(network_id, filter, filter_param)
    return devices
