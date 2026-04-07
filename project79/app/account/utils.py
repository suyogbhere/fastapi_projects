from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
from sqlmodel import Session
import uuid
from app.account.models import RefreshToken,User


SECRET_KEY = "dshfdusfhidjdchwbwubcjdvcjsiadsjjbdsnsireeejwdjdid"
ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")


def hash_password(password: str):
    return pwd_context.hash(password)



def verify_password(plain_password:str, hash_password:str):
    return pwd_context.verify(plain_password, hash_password)



def create_access_token(data: dict, expires_delta:timedelta=None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)



def create_token(session:Session,  user=User):
    access_token = create_access_token(data={"sub":str(user.id)})
    refresh_token_str = str(uuid.uuid4())
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)
    refresh_token = RefreshToken(
        user_id = user.id,
        token = refresh_token_str,
        expires_at=expires_at
    )
    session.add(refresh_token)
    session.commit()
    return {
        "access_token": access_token,
        "refresh_token": refresh_token_str,
        "token_type": "bearer"
    }