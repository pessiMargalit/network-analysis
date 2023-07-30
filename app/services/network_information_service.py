import asyncio

from app.modules.devices_filter import filter_devices_by_network_id


# TODO: Check if to merge this file and client_devices_information_service to one
async def filter_network_devices(network_id, filter_param, filter):
    await asyncio.sleep(0.01)
    devices = filter_devices_by_network_id(network_id, filter_param, filter)
    return devices
