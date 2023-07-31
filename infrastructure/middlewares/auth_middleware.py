from fastapi import APIRouter, HTTPException, Request, status
from infrastructure.middlewares.auth import validate_user_authentication
router = APIRouter()


@router.middleware("http")
async def auth_middleware(request: Request, call_next):

    is_authentication = validate_user_authentication()
    if not is_authentication:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )