from sqlalchemy.future import select
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.base import Base


async def ensure_object_exists(model: Type[Base], session: AsyncSession, object_id: int) -> Base:
    """
    Проверяет, существует ли объект с указанным ID.
    Если объект не найден, выбрасывает HTTPException с кодом 404.
    Возвращает объект, если он найден.
    """
    stmt = select(model).filter(model.id == object_id)
    result = await session.scalars(stmt)
    obj = result.first()
    if not obj:
        raise HTTPException(
            status_code=404,
            detail=f"{model.__name__} with ID {object_id} not found."
        )
    return obj


async def get_all_object(model: Type[Base], session: AsyncSession):
    stmt = select(model).order_by(model.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_object_by_id(model: Type[Base], session: AsyncSession, object_id: int):
    return await ensure_object_exists(model, session, object_id)


async def create_object(model: Type[Base], session: AsyncSession, data: BaseModel):
    obj = model(**data.dict())
    session.add(obj)
    await session.commit()
    return obj


async def update_object(model: Type[Base], session: AsyncSession, object_id: int, data: BaseModel):
    obj = await ensure_object_exists(model, session, object_id)
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    await session.commit()
    return obj


async def delete_object(model: Type[Base], session: AsyncSession, object_id: int):
    obj = await ensure_object_exists(model, session, object_id)
    await session.delete(obj)
    await session.commit()
