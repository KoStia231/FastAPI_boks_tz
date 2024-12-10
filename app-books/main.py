import uvicorn
from fastapi import FastAPI

from api import router as api_router
from core.config import settings as se
from utils import lifespan

app = FastAPI(
    lifespan=lifespan
)
app.include_router(api_router, prefix=se.api.prefix)

app = FastAPI()
app.include_router(api_router, prefix=settings.api.prefix)

if __name__ == 'main':
    uvicorn.run(
        'main:app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )

