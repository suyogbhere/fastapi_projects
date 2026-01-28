from sqlalchemy import MetaData, Integer, String, Table, Column
from db import engine


metadata = MetaData()

users = Table(
    "users",
    metadata, 
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True)
)



