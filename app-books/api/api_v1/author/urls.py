from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_helper
from core.models import Author
from core.schemas.shemas import AuthorCreate, AuthorResponse, AuthorUpdate
from api.api_v1.base_views import (
    get_all_object, get_object_by_id,
    create_object, update_object,
    delete_object
)

router = APIRouter()


@router.get("/", response_model=list[AuthorResponse])  # Список авторов
async def get_authors(
        session: AsyncSession = Depends(db_helper.session_getter),
):
    authors = await get_all_object(Author, session=session)
    return authors


@router.get("/{author_id}", response_model=AuthorResponse)
async def get_author(
        author_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    author = await get_object_by_id(Author, session=session, object_id=author_id)
    return author


@router.post("/", response_model=AuthorResponse)
async def create_author_view(
        author: AuthorCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    new_author = await create_object(Author, session=session, data=author)
    return new_author


@router.put("/{author_id}", response_model=AuthorResponse)
async def update_author_view(
        author_id: int, author: AuthorUpdate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    updated_author = await update_object(Author, session=session, object_id=author_id, data=author)
    return updated_author


@router.delete("/{author_id}")
async def delete_author_view(
        author_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    await delete_object(Author, session=session, object_id=author_id)
    return {"message": "Author deleted successfully"}
