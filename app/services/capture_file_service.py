import asyncio

from app.modules.upload_capture_files import choose_file as choose_file
from app.modules.file_reader import read_file as read_file
from app.modules.data_entry_into_db import insert_data_to_db as insert_data_to_db


async def create_network(file_content, client_id, premise):
    devices, connections = await read_file(file_content)
    insert_result = await insert_data_to_db(devices, connections, client_id, premise)
    return insert_result


async def choose_file_to_upload():
    return await choose_file()
