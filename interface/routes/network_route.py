
import io
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from starlette import status
from starlette.responses import Response, StreamingResponse
from app.services.capture_file_service import create_network
from app.services.device_information_service import get_device_information
from app.services.network_information_service import filter_network_devices
from app.services.device_connection_service import view_network_map
from app.services.client_devices_information_service import filter_network_devices_by_client_id
from app.auth.auth import validate_user_authentication_by_network_id \
    , validate_user_authentication_by_client_id
from app.services.network_information_service import get_network_information
from infrastructure.exceptions.exception_handler import api_handler

router = APIRouter()

BASE_PATH = "/network/"


@api_handler
@router.post(BASE_PATH + "client/{client_id}/{premise}/upload")
async def upload_capture_file(client_id: int, premise: str, file: UploadFile = File(...),
                              is_authenticated: bool = Depends(validate_user_authentication_by_client_id)):
    if not is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    file_content = await file.read()
    is_success = await create_network(file_content, client_id, premise)
    return is_success


@api_handler
@router.get(BASE_PATH + "device-connections/view/{network_id}")
async def view_device_connection(network_id: int,
                                 is_authenticated: bool = Depends(validate_user_authentication_by_network_id)):
    if not is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    buffer =await view_network_map(network_id)
    buffer.seek(0)
    StreamingResponse(io.BytesIO(buffer.getvalue()), media_type="image/png")


@api_handler
@router.get(BASE_PATH + "devices/{network_id}")
def get_network_devices_by_filter(network_id: int, filter: str = None, filter_param: str = None,
                                  is_authenticated: bool = Depends(validate_user_authentication_by_network_id)):
    if not is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return filter_network_devices(network_id, filter, filter_param)


@api_handler
@router.get(BASE_PATH + "devices/client/{client_id}")
def get_client_devices_by_filter(client_id, filter: str = None, filter_param: str = None,
                                 is_authenticated: bool = Depends(validate_user_authentication_by_client_id)):
    if not is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return filter_network_devices_by_client_id(client_id, filter, filter_param)


@api_handler
@router.get(BASE_PATH + "information/{network_id}")
def get_network_statistics_information(network_id,
                                       is_authenticated: bool = Depends(validate_user_authentication_by_network_id)):
    if not is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return get_network_information(network_id)


@api_handler
@router.get(BASE_PATH + "information/device/{device_id}")
def get_network_statistics_information(device_id,
                                       # is_authenticated: bool = Depends(validate_user_authentication_by_network_id)
                                       ):
    # if not is_authenticated:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Not authenticated",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    return get_device_information(device_id)
