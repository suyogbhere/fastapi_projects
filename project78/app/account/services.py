from app.account.models import User, UserCreate
from sqlmodel import Session, select
from fastapi import HTTPException


def create_user(session:Session, user:UserCreate):
    stmt = select(User).where(User.email== user.email)
    if session.exec(stmt).first():
        raise HTTPException(status_code=400, detail="Email alredy registered !!")
    new_user = User(
        email = user.email,
        name = user.name,
        hashed_password= user.password,
        is_verified=False
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user




