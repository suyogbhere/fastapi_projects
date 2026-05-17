from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_tables
from app.account.router import router as account_router
from app.converter.models import UserCredits, APIKey, CreditRequest
from app.converter.router import router as converter_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield



app = FastAPI(lifespan=lifespan)



# Register router
app.include_router(account_router, prefix="/api/account", tags=["Account"])
app.include_router(converter_router, prefix="/api/convert", tags=["Converter"])





