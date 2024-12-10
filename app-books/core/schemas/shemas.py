from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[date] = None


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[date] = None


class AuthorResponse(AuthorBase):
    id: int


class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    author_id: int
    available_copies: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    author_id: Optional[int] = None
    available_copies: Optional[int] = None


class BookResponse(BookBase):
    id: int


class BorrowBase(BaseModel):
    book_id: int
    reader_name: str
    borrow_date: date
    return_date: Optional[date] = None


class BorrowCreate(BorrowBase):
    pass


class BorrowResponse(BorrowBase):
    id: int
