from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, Response, encoders
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from data.db_service import insert_to_technician, insert_to_technician_clients
from app.auth.auth import Token, authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.auth.user import RegistrationUser

router = APIRouter()
BASE_PATH = "/technician/"


@router.post(f"{BASE_PATH}login", response_model=Token)
def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password ",
            headers={"WWW-Authenticate": "Bearer"}, )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['email']}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="Authorization", value=f"Bearer {encoders.jsonable_encoder(access_token)}",
        httponly=True
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post(BASE_PATH + "register")
async def register(user: RegistrationUser, clients_list):
    technitian_id = insert_to_technician(**user)
    for client in clients_list:
        # maybe need to check the id if exists
        insert_to_technician_clients(technitian_id, client)
