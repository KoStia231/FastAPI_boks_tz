from datetime import date
from typing import Optional

from pydantic import BaseModel


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
