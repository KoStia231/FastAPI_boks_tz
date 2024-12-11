from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.base_views import (
    get_all_object, get_object_by_id,
    create_object, update_object,
    delete_object
)
from core.database import db_helper
from core.models import Book
from core.schemas import (
    BookCreate, BookResponse,
    BookUpdate
)

router = APIRouter()


@router.get("/", response_model=list[BookResponse])
async def get_books(
        session: AsyncSession = Depends(db_helper.session_getter),
):
    books = await get_all_object(Book, session=session)
    return books


@router.get("/{book_id}", response_model=BookResponse)
async def get_book(
        book_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    book = await get_object_by_id(Book, session=session, object_id=book_id)
    return book


@router.post("/", response_model=BookResponse)
async def create_book_view(
        book: BookCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    new_book = await create_object(Book, session=session, data=book)
    return new_book


@router.put("/{book_id}", response_model=BookResponse)
async def update_book_view(
        book_id: int, book: BookUpdate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    updated_book = await update_object(Book, session=session, object_id=book_id, data=book)
    return updated_book


@router.delete("/{book_id}")
async def delete_book_view(
        book_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    await delete_object(Book, session=session, object_id=book_id)
    return {"message": "Book deleted successfully"}
