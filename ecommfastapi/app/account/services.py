from app.account.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from app.account.schemas import UserCreate, UserLogin, PasswordChangeRequest
from app.account.utils import hash_password, verify_password, create_email_verification_token,verify_email_token_and_get_user_id





async def create_user(session: AsyncSession, user: UserCreate ):
    stmt = select(User).where(User.email == user.email)
    result = await session.scalars(stmt)
    if result.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email Already registerd!!")
    
    new_user = User(
        email =  user.email ,
        hashed_password = hash_password(user.password)
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def authenticate_user(session: AsyncSession, user_login:UserLogin):
    stmt = select(User).where(User.email == user_login.email)
    result = await session.scalars(stmt)
    user = result.first()

    if not user or not verify_password(user_login.password, user.hashed_password):
        return None
    
    return user




async def email_verification_send(user:User):
    token = create_email_verification_token(user.id)
    link = f"http://127.0.0.1:8000/account/verify?token={token}"
    print(f"Verify your email: {link}")
    return {"msg": "Verification email sent!!"}


async def verify_email_token(session: AsyncSession, token: str):
    user_id = verify_email_token_and_get_user_id(token, "verify_email")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token")

    stmt = select(User).where(User.id == user_id)
    print("STMT:", stmt)
    result = await session.scalars(stmt)
    print("RESULT:",result)
    user = result.first()
    print("USER:", user)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not found")
    
    user.is_verified = True
    session.add(user)
    await session.commit()
    return {"message":"Email verified successfully!!!"}



async def change_password(session: AsyncSession, user: User, data: PasswordChangeRequest):
    if not verify_password(data.old_password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Old password is incorrect")
    user.hashed_password = hash_password(data.new_password)
    session.add(user)
    await session.commit()


