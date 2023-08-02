import asyncio

from app.modules.devices_filter import filter_devices_by_network_id
from app.modules.network_information import get_most_frequent_protocols
from infrastructure.exceptions.exception_handler import error_handler


@error_handler
async def filter_network_devices(network_id, filter, filter_param):
    devices = filter_devices_by_network_id(network_id, filter, filter_param)
    return devices


@error_handler
async def get_network_information(network_id):
    most_frequent_protocols = get_most_frequent_protocols(network_id)
    return most_frequent_protocols
