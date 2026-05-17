from sqlalchemy.ext.asyncio import (create_async_engine, AsyncSession, async_sessionmaker, AsyncAttrs)
import os
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends
from typing import Annotated, AsyncGenerator



BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))
            ))


db_path = os.path.join(BASE_DIR, "sqlite.db")

DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"

engine = create_async_engine(DATABASE_URL, echo=True)


class Declarative(DeclarativeBase):
    pass


class Base(AsyncAttrs, Declarative):
    __abstract__ = True


async_session = async_sessionmaker(
    engine,
    class_ = AsyncSession,
    expire_on_commit=False
)


async def create_tables():
    from app.account.models import User, RefreshToken
    from app.converter.models import UserCredits, APIKey, CreditRequest
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    print("Tables Created....")


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]


