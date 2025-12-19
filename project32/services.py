from models import *
from db import sessionlocal


## Insert or Create User
def create_user(name:str, email:str):
    with sessionlocal() as session:
        user = User(name=name,email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    


def create_post(user_id: int, title: str, content: str):
    with sessionlocal() as session:
        post = Post(user_id= user_id, title = title, content=content)
        session.add(post)
        session.commit()
    