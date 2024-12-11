from datetime import date
from typing import Optional

from pydantic import BaseModel


class BorrowBase(BaseModel):
    book_id: int
    reader_name: str
    borrow_date: date
    return_date: Optional[date] = None


class BorrowCreate(BorrowBase):
    pass


class BorrowResponse(BorrowBase):
    id: int
