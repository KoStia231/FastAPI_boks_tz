from fastapi import APIRouter
from .api_v1 import api_v1_router
from core.config import settings as se

api_router = APIRouter()

api_router.include_router(api_v1_router, prefix=se.api.v1.prefix)
