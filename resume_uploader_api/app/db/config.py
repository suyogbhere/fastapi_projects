from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_session, AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends
from typing import AsyncGenerator, Annotated
from decouple import config
import os


DB_USER = config("DB_USER")
DB_PASS = config("DB_PASS")
DB_NAME = config("DB_NAME")
DB_PORT = config("DB_PORT", cast=int)
DB_HOST = config("DB_HOST")


DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# db_path = os.path.join(BASE_DIR, "sqlite.db")

# DATABASE_URL = f"sqlite:///{db_path}" 

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_= AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    pass

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]

