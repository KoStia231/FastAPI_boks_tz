from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from core import se


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=se.db.naming_convention,
    )

    id: Mapped[int] = mapped_column(primary_key=True)
