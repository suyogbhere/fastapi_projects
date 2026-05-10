from pydantic import BaseModel, EmailStr



class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name : str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    name : str
    is_active: bool
    is_admin: bool
    is_verified: bool

    class config: 
        from_attributes = True
