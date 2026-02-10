from fastapi import FastAPI
from pydantic import BaseModel
from app.user import services as user_services



app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str



@app.post("/user")
def user_create(user: UserCreate):
    user_services.create_user(name=user.name, email=user.email)
    return {"status": "created"}