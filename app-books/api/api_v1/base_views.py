from sqlalchemy.future import select
from pydantic import BaseModel
from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.base import Base


async def get_all_object(model: Type[Base], session: AsyncSession):
    stmt = select(model).order_by(model.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_object_by_id(model: Type[Base], session: AsyncSession, object_id: int):
    stmt = select(model).filter(model.id == object_id)
    result = await session.scalars(stmt)
    return result.first()


async def create_object(model: Type[Base], session: AsyncSession, data: BaseModel):
    obj = model(**data.dict())
    session.add(obj)
    await session.commit()
    return obj


async def update_object(model: Type[Base], session: AsyncSession, object_id: int, data: BaseModel):
    stmt = select(model).filter(model.id == object_id)
    result = await session.scalars(stmt)
    obj = result.first()
    if obj:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(obj, key, value)
        await session.commit()
    return obj


async def delete_object(model: Type[Base], session: AsyncSession, object_id: int):
    stmt = select(model).filter(model.id == object_id)
    result = await session.scalars(stmt)
    object_record = result.first()
    if object_record:
        await session.delete(object_record)
        await session.commit()
