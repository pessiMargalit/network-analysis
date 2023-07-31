from fastapi import APIRouter

router = APIRouter()

@app.middleware("http")
async def 