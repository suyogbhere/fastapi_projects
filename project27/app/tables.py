#To Create Table 

from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey

metadata = MetaData()

# user Table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True),
)

## Relationaship  One to Many
posts = Table(
    "posts" , 
    metadata,
    Column("id", Integer, primary_key = True) ,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("title", String, nullable=False),
    Column("content",String, nullable=False),
)


## Relationaship  One to one
profile = Table(
    "profile" , 
    metadata,
    Column("id", Integer, primary_key = True) ,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True),
    Column("bio", String, nullable=False),
    Column("address",String, nullable=False),
)



# Relationship many to many
address = Table(
    "address" , 
    metadata,
    Column("id", Integer, primary_key = True) ,
    Column("street", String, nullable=False),
    Column("country",String, nullable=False),
)


#Userr address association
user_address_association = Table(
    "user_address_association",
    metadata,
    Column("user_id", Integer, ForeignKey("users.id",
    ondelete="CASCADE"), primary_key=True),
    Column("address_id", Integer, ForeignKey("address.id",
    ondelete="CASCADE"), primary_key=True)
)



## Create table in Database
def create_tables():
    metadata.create_all(engine)


