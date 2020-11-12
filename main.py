from fastapi import FastAPI

from api.api_v1 import api_router
from api.globals import globals_router
from core.config import settings

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(globals_router)
