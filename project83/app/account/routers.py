from app.account.services import create_user
from app.db.config import SessionDep
from fastapi import APIRouter


router = APIRouter(prefix="/account", tags=["Account"])


@router.post("/register")
async def register(session:SessionDep, name:str, email:str):
    return await create_user(session, name, email)

