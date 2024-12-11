from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.api_v1.base_views import ensure_object_exists
from core.models.models import Borrow, Book
from core.schemas import BorrowCreate


async def create_borrow(session: AsyncSession, borrow: BorrowCreate):
    book_stmt = select(Book).filter(Book.id == borrow.book_id)
    result = await session.scalars(book_stmt)
    book = result.first()
    if book and book.available_copies > 0:
        new_borrow = Borrow(**borrow.dict())
        book.available_copies -= 1
        session.add(new_borrow)
        await session.commit()
        await session.refresh(new_borrow)
        await session.commit()
        return new_borrow
    else:
        raise ValueError("Book is not available for borrowing")


async def delete_borrow(session: AsyncSession, borrow_id: int):
    stmt = select(Borrow).filter(Borrow.id == borrow_id)
    result = await session.scalars(stmt)
    borrow_record = result.first()
    if borrow_record:
        book_stmt = select(Book).filter(Book.id == borrow_record.book_id)
        book_result = await session.scalars(book_stmt)
        book = book_result.first()
        if book:
            book.available_copies += 1
        await session.delete(borrow_record)
        await session.commit()


async def return_borrow(session: AsyncSession, borrow_id: int, return_date: str):
    try:
        parsed_date = datetime.strptime(return_date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid date format. Expected format: YYYY-MM-DD."
        )

    borrow_record = await ensure_object_exists(Borrow, session, borrow_id)

    # сущ книги по borrow_record.book_id
    book = await ensure_object_exists(Book, session, borrow_record.book_id)

    if book.available_copies + 1 > book.initial_copies:
        raise HTTPException(
            status_code=400,
            detail=f"Cannot exceed initial copies: {book.initial_copies}."
        )

    book.available_copies += 1
    borrow_record.return_date = parsed_date
    await session.commit()
    return borrow_record
