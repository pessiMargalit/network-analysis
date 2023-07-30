import os
import sys
import uvicorn
from fastapi import FastAPI
from routes.network_route import router as network_router
from routes.technician_route import router as technician_router

curr_path = os.path.dirname(__file__)
root_path = os.path.join(curr_path, "..")
sys.path.append(root_path)
print(sys.path)
app = FastAPI()

app.include_router(network_router)
app.include_router(technician_router)


# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
