from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)

from core.config import settings as se


class DatabaseHelper:
    def __init__(
            self, url: str,
            echo: bool = False,
            echo_pool: bool = False,
            max_overflow: int = 10,
            pool_size: int = 5,
            expire_on_commit: bool = False,
            autoflush: bool = False,
            autocommit: bool = False,
    ) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=expire_on_commit,
            autoflush=autoflush,
            autocommit=autocommit
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(
    url=str(se.db.url),
    echo=bool(se.db.echo),
    max_overflow=se.db.max_overflow,
    pool_size=se.db.pool_size,
    expire_on_commit=se.db.expire_on_commit,
    autoflush=se.db.autoflush,
    autocommit=se.db.autocommit,
)
