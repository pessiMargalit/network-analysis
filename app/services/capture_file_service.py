from app.modules.file_handler import read_file as read_file
from app.modules.data_entry_into_db import insert_capture_file_data_to_db as insert_data_to_db
from infrastructure.exceptions.exception_handler import error_handler


@error_handler
async def create_network(file_content, client_id, premise):
    result = read_file(file_content)
    devices, connections = await result
    insert_result = await insert_data_to_db(devices, connections, client_id, premise)
    return insert_result


