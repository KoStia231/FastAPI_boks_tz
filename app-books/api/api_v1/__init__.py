from fastapi import APIRouter
from .author.urls import router as author_router
from .book.urls import router as book_router
from .borrow.urls import router as borrow_router
from core.config import settings as se

api_v1_router = APIRouter()

api_v1_router.include_router(author_router, prefix=se.api.v1.author, tags=["author"])
api_v1_router.include_router(book_router, prefix=se.api.v1.book, tags=["book"])
api_v1_router.include_router(borrow_router, prefix=se.api.v1.borrow, tags=["borrow"])
