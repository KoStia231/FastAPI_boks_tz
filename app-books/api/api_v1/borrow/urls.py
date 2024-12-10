from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_helper
from core.schemas.shemas import BorrowCreate, BorrowResponse
from core.models import Borrow
from api.api_v1.base_views import get_all_object, get_object_by_id
from .views import create_borrow, delete_borrow, return_borrow

router = APIRouter()


@router.get("/", response_model=list[BorrowResponse])
async def get_borrows(
        session: AsyncSession = Depends(db_helper.session_getter),
):
    borrows = await get_all_object(Borrow, session=session)
    return borrows


@router.get("/{borrow_id}", response_model=BorrowResponse)
async def get_borrow(
        borrow_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    borrow = await get_object_by_id(Borrow, session=session, object_id=borrow_id)
    return borrow


@router.post("/", response_model=BorrowResponse)
async def create_borrow_view(
        borrow: BorrowCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    new_borrow = await create_borrow(session=session, borrow=borrow)
    return new_borrow


@router.delete("/{borrow_id}")
async def delete_borrow_view(
        borrow_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    await delete_borrow(session=session, borrow_id=borrow_id)
    return {"message": "Borrow record deleted successfully"}


@router.patch("/{borrow_id}/return", response_model=BorrowResponse)
async def return_borrow_view(
        borrow_id: int,
        return_date: str,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    """
    Завершение выдачи с указанием даты возврата.
    """
    returned_borrow = await return_borrow(session=session, borrow_id=borrow_id, return_date=return_date)
    return returned_borrow
