from db import engine
from tables import users, posts
from sqlalchemy import insert, select, update, delete


## Insert or Create User
def  create_user(name: str, email:str):
    with engine.connect() as conn:
        stmt = insert(users).values(name=name, email=email)
        conn.execute(stmt)
        conn.commit()


## Insert or Create Post
def  create_post(user_id: int, title: str, content:str):
    with engine.connect() as conn:
        stmt = insert(posts).values(user_id=user_id, title=title, content=content)
        conn.execute(stmt)
        conn.commit()



## Get single User by ID
def get_user_by_id(user_id: int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.id == user_id)
        result = conn.execute(stmt).first()
        return result 
    

## Get All Users
def get_all_users():
    with engine.connect() as conn:
        stmt = select(users)
        result = conn.execute(stmt).fetchall()
        return result 
    

## Get Post by User
def get_posts_by_user(user_id:int):
    with engine.connect() as conn:
        stmt = select(posts).where(posts.c.user_id == user_id)
        result = conn.execute(stmt).fetchall()
        return result 