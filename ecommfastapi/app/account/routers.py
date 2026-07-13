from fastapi import APIRouter, HTTPException, status, Depends, Request
from app.account.schemas import UserCreate, UserOut, UserLogin, PasswordChangeRequest
from app.account.services import create_user, authenticate_user, email_verification_send,verify_email_token, change_password
from app.db.config import SessionDep
from app.account.utils import create_tokens, verify_refresh_token
from fastapi.responses import JSONResponse
from app.account.deps import get_current_user
from app.account.models import User

router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register(session:SessionDep, user:UserCreate):
    return await create_user(session, user)


@router.post("/login")
async def login(session: SessionDep, user_login: UserLogin):
    user = await authenticate_user(session, user_login)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials!!")
    
    tokens = await create_tokens(session, user)
    response = JSONResponse(content={"message":"Login Successfull!!"})
    response.set_cookie(
        "access_token",
        value=tokens["access_token"],
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60*60*24*1
    )
    response.set_cookie(
        "refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60*60*24*7
    )
    return response
    


@router.get("/me", response_model=UserOut)
async def me(user: User = Depends(get_current_user)):
    return user



@router.post("/refresh")
async def refresh_token(session:SessionDep, request: Request):
    # print("Cookies:", request.cookies)
    token = request.cookies.get("refresh_token")
    # print("Refresh Token:", token)
    if not token:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Missing refresh token",
        )
    
    user = await verify_refresh_token(session, token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired refresh token")
    
    tokens = await create_tokens(session, user)
    
    response = JSONResponse(content={"message":"Token Refreshed Successfully!!"})
    response.set_cookie(
        "access_token",
        value=tokens["access_token"],
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60*60*24*1
    )
    response.set_cookie(
        "refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60*60*24*7
    )
    return response


@router.post("/send-verification-email")
async def send_verification_email(user : User = Depends(get_current_user)):
    return await email_verification_send(user)


@router.get("/verify-email")
async def verify_email(session: SessionDep, token:str):
    return await verify_email_token(session, token)



@router.post("/change-password")
async def password_change(session: SessionDep, data: PasswordChangeRequest, user: User=Depends(get_current_user)):
    await change_password(session, user, data)
    return {"msg": "Password changed successfully"}







