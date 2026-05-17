from fastapi import Depends, HTTPException, Request, APIRouter
from app.account.models import User
from app.db.config import SessionDep
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from app.account.services import create_user, authenticate_user
from app.account.utils import create_token, verify_refresh_token, revoke_refresh_token
from app.account.dependencies import get_current_user, require_admin
from app.account.services import (process_email_verification,
                                   verify_email_token, 
                                   change_password, 
                                   process_password_reset,
                                     reset_password_with_token)
from app.account.schemas import UserOut, UserCreate


router = APIRouter()



@router.post("/register", response_model=UserOut)
async def register(session:SessionDep, user:UserCreate):
    return await create_user(session, user)


@router.post("/login")
async def login(session:SessionDep, form_data:OAuth2PasswordRequestForm=Depends()):
    user =await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        return HTTPException(status_code=401, detail="Invalid Credentials!!!")
    tokens =create_token(session, user)
    response = JSONResponse(content={"access_token":tokens["access_token"]})
    response.set_cookie("refresh_token",tokens["refresh_token"], httponly=True, secure=True, samesite="lax", max_age=60 * 60 * 24 * 7)
    return response


@router.post("/refresh")
async def refresh_token(session:SessionDep, request:Request):
    token= request.cookies.get("refresh_token")
    if not token:
        raise HTTPException(status_code=401, detail="Missing refresh token!!")
    user = verify_refresh_token(session, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token!!")
    return create_token(session, user)



@router.get("/me", response_model=UserOut)
async def me(user= Depends(get_current_user)):
    return user


@router.post("/verify-request")
async def send_verification_email(user=Depends(get_current_user)):
    return await process_email_verification(user = user)


@router.get("/verify")
async def verify_email(session: SessionDep, token: str):
    return await verify_email_token(session, token)


@router.post("/change-password")
async def password_change(session: SessionDep, new_password: str, user=Depends(get_current_user)):
    await change_password(session, new_password, user)
    return {"msg":"Password change successfully!!"}


@router.post("/forgot-password")
async def forgot_password(session: SessionDep, email: str):
    return await process_password_reset(session, email)


@router.post("/reset-password")
async def reset_password(session: SessionDep, token: str, new_password: str):
    return await reset_password_with_token(session, token, new_password)


@router.get("/admin")
async def admin(user=Depends(require_admin)):
    return {"msg": f"Welcome admin {user.name}"}



@router.post("/logout")
async def logout(session: SessionDep, request: Request):
    token = request.cookies.get("refresh_token")
    if token:
         await revoke_refresh_token(session, token)
    response = JSONResponse(content={"detail":"Logged Out!!"})
    response.delete_cookie("refresh_token")
    return response



