
from fastapi import APIRouter


router = APIRouter()
BASE_PATH = "/technician/"


@router.post(f"{BASE_PATH}login")
async def login(email, password):
    pass


# @router.post("/login", response_model=Token)
# def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fakeDB, form_data.username, form_data.password)
#     print(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     response.set_cookie(
#         key="Authorization", value=f"Bearer {encoders.jsonable_encoder(access_token)}",
#         httponly=True
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
#
#
# @app.post("/register", response_model=BaseUser)
# async def create_user(user: RegistrationUser):
#     new_user = DBUser(**dict(user), hashed_password=get_password_hash(user.password))
#     fakeDB[new_user.username] = dict(new_user)
#     return new_user

@router.get(f"{BASE_PATH}register")
async def register(user):
    pass
