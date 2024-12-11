from sqlalchemy import String, Date, ForeignKey
from sqlalchemy import event
from sqlalchemy.orm import relationship, Mapped, mapped_column

from core.models import Base


class Author(Base):
    __tablename__ = "authors"

    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    birth_date: Mapped[Date | None] = mapped_column(Date, nullable=True)

    books: Mapped[list["Book"]] = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books.py"

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=False)
    available_copies: Mapped[int] = mapped_column(nullable=False, default=1)
    initial_copies: Mapped[int] = mapped_column(nullable=False, default=1)

    author: Mapped["Author"] = relationship("Author", back_populates="books.py")
    borrows: Mapped[list["Borrow"]] = relationship("Borrow", back_populates="book")


@event.listens_for(Book, 'before_insert')
def set_initial_copies(mapper, connection, target):
    if target.available_copies is not None:
        target.initial_copies = target.available_copies


class Borrow(Base):
    __tablename__ = "borrows"

    book_id: Mapped[int] = mapped_column(ForeignKey("books.py.id"), nullable=False)
    reader_name: Mapped[str] = mapped_column(String, nullable=False)
    borrow_date: Mapped[Date] = mapped_column(Date, nullable=False)
    return_date: Mapped[Date | None] = mapped_column(Date, nullable=True)

    book: Mapped["Book"] = relationship("Book", back_populates="borrows")
