from sqlmodel import Field, SQLModel, Relationship

class UserAddressLink(SQLModel, table=True):
    user_id : int = Field(foreign_key="user.id", primary_key=True)
    address_id : int = Field(foreign_key="address.id", primary_key=True)


## Relationship Attribute it is used for bidirectional access
class User(SQLModel, table = True):
    id : int = Field(primary_key=True)
    name  : str
    email : str 

    profile : "Profile" | None = Relationship(back_populates="user")
    post : list["Post"] | None = Relationship(back_populates="user")
    address : list["Address"] | None = Relationship(back_populates="user", link_model=UserAddressLink) 


#relationship
# one to One 
class Profile(SQLModel, table=True):
    id : int = Field(primary_key=True)
    user_id : int = Field(foreign_key="user.id", unique=True)
    bio : str

    user : "User" | None = Relationship(back_populates="profile")

# One to Many
class Post(SQLModel, table=True):
    id : int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    title : str 
    content: str

    user : "User" | None = Relationship(back_populates="posts")

# user.posts


## Many to Many
class Address(SQLModel, table=True):
    id : int = Field(primary_key=True)

    street: str
    city: str

    user : list["User"] | None = Relationship(back_populates="address", link_model=UserAddressLink)