from fastapi import APIRouter, HTTPException, status, Depends, Request
from app.account.schemas import UserCreate, UserOut, UserLogin, PasswordChangeRequest, PasswordResetEmailRequest,PasswordResetRequest
from app.account.services import create_user, authenticate_user, email_verification_send,verify_email_token, change_password,password_reset_email_send,verify_password_reset_token
from app.db.config import SessionDep
from app.account.utils import create_tokens, verify_refresh_token, revoke_refresh_token
from fastapi.responses import JSONResponse
from app.account.deps import get_current_user, require_admin
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



@router.post("/send-password-reset-email")
async def send_password_reset_email(session: SessionDep, data: PasswordResetEmailRequest):
    return await password_reset_email_send(session, data)



@router.post("/verify-password-reset-token")
async def verify_password_reset_email_token(session:SessionDep, data: PasswordResetRequest):
    return await verify_password_reset_token(session, data)



@router.get("/admin")
async def admin(user: User = Depends(require_admin)):
    return {"msg": f"Welcome Admin {user.email}"}



@router.post("/logout")
async def logout(session: SessionDep, request: Request, user: User= Depends(get_current_user)):
    refresh_token = request.cookies.get("refresh_token")
    if refresh_token:
        await revoke_refresh_token(session, refresh_token)
    response = JSONResponse(content={"detail":"Logged Out"})
    response.delete_cookie("refresh_token")
    response.delete_cookie("access_token")
    return response


