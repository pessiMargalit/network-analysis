from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from requests import Response
from starlette import status

from infrastructure.middlewares.auth import Token, authenticate_user
from infrastructure.middlewares.user import RegistrationUser

router = APIRouter()
BASE_PATH = "/technician/"


@router.post(f"{BASE_PATH}login", response_model=Token)
def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.email, form_data.password)
    print(form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password ",
            headers={"WWW-Authenticate": "Bearer"}, )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        response.set_cookie(
            key="Authorization", value=f"Bearer {encoders.jsonable_encoder(access_token)}",
            httponly=True
        )
        return {"access_token": access_token, "token_type": "bearer"}


@router.get(f"{BASE_PATH}register")
async def register(user: RegistrationUser):
    pass
#     new_user = DBUser(**dict(user), hashed_password=get_password_hash(user.password))
#     fakeDB[new_user.username] = dict(new_user)
#     return new_user
