from fastapi import HTTPException, Request, status
from app.auth.auth import validate_user_authentication_by_client_id, \
    validate_user_authentication_by_network_id


# def auth_middleware(request: Request, call_next):
#     token = oauth2_cookie_scheme(request)
#     user = get_user_from_token(token)
#     request.state.user = user
#     response = call_next(request)
#     return response


def get_client_id_from_url(url):
    url = url.split["/"]["client":]
    return url[1]


def get_network_id_from_url(url):
    return url.split('/')[-1]


async def auth_middleware(request: Request, call_next):
    is_authentication = False
    if "client" in request.url.path:
        client_id = int(get_client_id_from_url(request.url.path))
        is_authentication = validate_user_authentication_by_client_id(client_id)
    elif "network" in request.url.path:
        network_id = int(get_network_id_from_url(request.url.path))
        is_authentication = validate_user_authentication_by_network_id(network_id)
    if not is_authentication:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return await call_next(request)
