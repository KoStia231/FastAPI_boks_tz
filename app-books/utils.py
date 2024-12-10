from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()
