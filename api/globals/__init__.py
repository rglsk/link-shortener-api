from fastapi import APIRouter

from api.globals import links

globals_router = APIRouter()
globals_router.include_router(links.router, tags=["globals"])
