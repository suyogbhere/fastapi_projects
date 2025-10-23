#To Create Table 

from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime

metadata = MetaData()

# user Table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("phone", Integer, nullable=False, unique=True)
)

#Address table
address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("street", String(length=50), nullable=False),
    Column("dist", String, nullable=False, unique=True),
    Column("country", Integer, nullable=False, unique=True)
)


## Create table in Database
def create_tables():
    metadata.create_all(engine)


## Drop table from Database
# def drop_tables():
#     metadata.drop_all(engine)