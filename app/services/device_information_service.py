from app.modules.device_information import get_device_protocols
from infrastructure.exceptions.exception_handler import error_handler


@error_handler
async def get_device_information(device_id):
    device_protocols = get_device_protocols(device_id)
    set_device_protocols = {protocol["protocol_type"] for protocol in device_protocols}
    return set_device_protocols



