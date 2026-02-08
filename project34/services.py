from models import *
from db import sessionlocal
from sqlalchemy import select, asc


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
    


## Read user by ID
def get_user_by_id(user_id: int):
    with sessionlocal() as session:
        user = session.get_one(User, user_id)
        return user
    


## Read post by ID
def get_post_by_id(post_id: int):
    with sessionlocal() as session:
        stmt = select(Post).where(Post.id == post_id)
        post = session.scalars(stmt).one()
        return post



## Read All User data
def get_all_users():
    with sessionlocal() as session:
        stmt = select(User)
        users = session.scalars(stmt).all()
        return users
    


## Read all posts for an users 
def get_posts_by_user(user_id:int):
    with sessionlocal() as session:
        user = session.get(User, user_id)
        posts = user.posts if user else []
        return posts


 
## Update User email
def update_user_email(user_id:int, new_email: str):
    with sessionlocal() as session:
        user = session.get(User, user_id)
        if user:
            user.email = new_email
            session.commit()
            return user
        


## Delete POST
def delete_post(post_id: int):
    with sessionlocal() as session:
        post = session.get(Post, post_id)
        if post:
            session.delete(post)
            session.commit()


## Order by 
def get_users_ordered_by_name():
    with sessionlocal() as session:
        stmt = select(User).order_by(asc(User.name))
        users = session.scalars(stmt).all()
        return users
    

