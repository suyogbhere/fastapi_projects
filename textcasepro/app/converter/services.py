from sqlalchemy.ext.asyncio import AsyncSession
from app.account.models import User
from app.converter.models import UserCredits, APIKey, CreditRequest
from app.converter.utils import generate_api_key
from sqlalchemy import select, delete
from fastapi import HTTPException


async def generate_user_api_key(session: AsyncSession, user: User):
    await session.execute(delete(APIKey).where(APIKey.user_id== user.id))
    new_key = generate_api_key()
    key = APIKey(user_id = user.id, key = new_key)
    session.add(key)
    await session.commit()
    return new_key


async def get_user_api_key(session: AsyncSession, user:User):
    key_obj = await session.scalar(select(APIKey).where(APIKey.user_id == user.id))
    if not key_obj:
        raise HTTPException(status_code=404, detail="API key not found !!")
    return key_obj.key






