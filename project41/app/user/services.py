from app.db.config import Sessionlocal
from app.user.models import User
from sqlalchemy import select

# Insert or create user
def create_user(name:str, email:str):
    with Sessionlocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()



## Real Alll Users
def get_all_user():
    with Sessionlocal() as session:
        stmt = select(User)
        users = session.scalars(stmt)
        return users.all()