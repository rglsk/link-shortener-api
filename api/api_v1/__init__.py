from fastapi import APIRouter

from api.api_v1 import links

api_router = APIRouter()
api_router.include_router(links.router, tags=["links"])
