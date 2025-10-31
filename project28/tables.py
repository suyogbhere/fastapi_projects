from db import engine
from sqlalchemy import MetaData, Table,Column, Integer, String

metadata = MetaData()


## Users Table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key= True),
    Column("name", String(length=50),nullable=False),
    Column("email", String, nullable=False, unique=True)
)


## Create Table in Database
# metadata.create_all(engine)

def create_table():
    metadata.create_all(engine)
