from fastapi import APIRouter, UploadFile, File, Form
from app.services.capture_file_service import create_network, choose_file
from app.services.network_information_service import filter_network_devices as filter_network_devices
from app.services.device_connection_service import view_network_map as view_network_map
from app.services.client_devices_information_service import filter_network_devices_by_clientid as filter_network_devices_by_clientid

router = APIRouter()

BASE_PATH = "/network/"


@router.post(f"{BASE_PATH}new-network-analysis")
async def choose_capture_file():
    return await choose_file()


@router.post(f"{BASE_PATH}upload")
async def upload_capture_file(client_id: int = Form(...), premise: str = Form(...), file: UploadFile = File(...)):
    file_content = await file.read()
    is_success = await create_network(file_content, client_id, premise)
    return is_success


# get the connections

# @router.get(f"{BASE_PATH}view/:network_id")
# async def view_device_connection(network_id):
#     return await view_network_map(network_id)
#

@router.get(BASE_PATH + "view/{network_id}")
async def view_network_devices_by_filter(network_id, filter_param: str = None, filter: str = None):
    return await filter_network_devices(network_id, filter_param, filter)

@router.get("/view/client/{client_id}")
# TODO: Change the route
async def view_client_devices_by_filter(client_id, filter_param: str = None, filter: str = None):
    return await filter_network_devices_by_clientid(client_id, filter_param, filter)
