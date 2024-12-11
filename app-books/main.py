import uvicorn
from fastapi import FastAPI

from api import api_router
from core import se
from utils import lifespan


app = FastAPI(
    lifespan=lifespan
)
app.include_router(api_router, prefix=se.api.prefix)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=se.run.host,
        port=se.run.port,
        reload=True
    )
