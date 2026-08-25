from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

from constants import PG_DATABASE_URL


engine = create_async_engine(
    PG_DATABASE_URL,
    pool_pre_ping=True,
    echo=True,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with SessionLocal() as db:
        yield db
