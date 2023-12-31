import os
import sys
import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from app.auth.auth_middleware import auth_middleware
from routes.network_route import router as network_router
from routes.technician_route import router as technician_router
from data.db_connection import get_connection, disconnect

curr_path = os.path.dirname(__file__)
root_path = os.path.join(curr_path, "..")
sys.path.append(root_path)

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.middleware("http")
# async def authentication_middleware(request: Request, call_next):
#     if request.url.path.startswith("/network"):
#         return await auth_middleware(request, call_next)
#     return await call_next(request)


app.include_router(network_router)
app.include_router(technician_router)


@app.on_event("startup")
def startup():
    get_connection()


@app.on_event("shutdown")
def shutdown():
    disconnect()


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
