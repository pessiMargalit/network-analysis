from datetime import datetime, timedelta
from typing import Union, Optional, Dict
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel, Response
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr

from data.db_service import get_from_db

SECRET_KEY = r"PE/9wcV31ayos6hpy/RV0uf9qC8FzJPZKPKVb4h2TJ0="
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
            self,
            tokenUrl: str,
            scheme_name: Optional[str] = None,
            scopes: Optional[Dict[str, str]] = None,
            auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.cookies.get("Authorization")  # changed to accept access token from httpOnly Cookie

        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_cookie_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


@get_from_db
def get_user(email: str):
    query = "SELECT * FROM technician WHERE email = %s"
    return query, email


def authenticate_user(email: str, password: str):
    user = get_user(email)[0]
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user


async def get_current_user(token: str = Depends(oauth2_cookie_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = get_user(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[EmailStr, None] = None


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    print("------------------------create_access_token-------------------------")
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_active_user(current_user=Depends(get_current_user)):
    if current_user and current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# TODO:Is admin middleware

# app.add_middleware(AuthMiddleware, verify_header=verify_authorization_header)
@get_from_db
def is_client_exist_by_network_id(network_id):
    query = "SELECT EXISTS(SELECT client_id FROM network WHERE id = %s) AS is_client_exist"
    return query, network_id


@get_from_db
def is_client_exist_by_client_id(client_id):
    query = "SELECT EXISTS(id FROM client WHERE id = %s) AS is_client_exist"
    return query, client_id

@get_from_db
def has_permission(network_id, user):
    query = f"""SELECT 
                 client_id AS has_permission_to_client_id
             FROM 
                 technician_clients
             WHERE 
                 technician_id = {user.id} AND client_id = (SELECT client_id FROM network WHERE id = %s)"""
    return query, network_id


def validate_user_authentication(is_network_id: bool, id: int, current_user=Depends(get_current_user)):
    if is_network_id:
        if not is_client_exist_by_network_id(id)[0]["is_client_exist"]:
            raise ValueError("No such client exists in the system")
    elif not is_client_exist_by_client_id(id)[0]["is_client_exist"]:
        raise ValueError("No such client exists in the system")
    # Check if the current user has permission to receive the client - network ,
    # by checking if the technician has the client_id that has the given network_id
    if has_permission(id, current_user) == ():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You do not have permission to perform this action",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return True

# app.add_middleware(AuthMiddleware, verify_header=validate_user_authentication)
# @app.middleware("http")
# @handle_app_exceptions
# async def apply_middleware(request: Request, call_next):
#     # Apply the authorization middleware only to specific endpoints
#     if request.url.path.startswith("/technician"):
#         return await auth_middleware(request, call_next)
# @app.get("/todos/{id}")
# async def auth_middleware(request:Request, call_next, is_authenticated: bool = Depends(validate_user_authentication)):
#     if not is_authenticated:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Not authenticated",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     if "client" in request.url.path:
#     return todo_dict[todo_id]
