from typing import Optional

from pydantic import BaseModel


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
