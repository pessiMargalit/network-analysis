from app.modules.device_information import get_device_protocols
from infrastructure.exceptions.exception_handler import basic_exception_handler


@basic_exception_handler
def get_device_information(device_id):
    device_protocols = get_device_protocols(device_id)
    set_device_protocols = {protocol["protocol_type"] for protocol in device_protocols}
    return set_device_protocols



