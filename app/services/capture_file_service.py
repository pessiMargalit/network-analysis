from app.modules.file_reader import read_file as read_file
from app.modules.data_entry_into_db import insert_data_to_db as insert_data_to_db


async def create_network(cap_file, client_id, date_taken, premise_name, technician_name):
    data = await read_file(cap_file)
    insert_result = await insert_data_to_db(data, client_id, date_taken, premise_name, technician_name)
    return insert_result
