from pydantic import BaseModel
from fastapi import FastAPI
from typing import List, Any

app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock : int | None = None


class ProductOut(BaseModel):
    name : str
    price: float


## Without response Model
# @app.get("/products/")
# async def get_products():
#     return {"id":1, "name":"redmi note 10", "price":15000, "stock":5}


# With Response Model parameter ( When it is use that time getting an any datatyping data pass it not giving an error)
# @app.get("/products/", response_model=Product)
# async def get_products():
#     return {"id":1, "name":"redmi note 10", "price":15000, "stock":5}


# @app.get("/products/", response_model=List[Product])
# async def get_products():
#     return [
#         {"id":1, "name":"redmi note 10", "price":15000, "stock":5},
#         {"id":2, "name":"realme", "price":25000, "stock":4}
#         ]


# @app.post("/products/", response_model=Product)
# async def create_products(product: Product):
#     return product




#Inheritance
# class BaseUser(BaseModel):
#     username: str
#     full_name: str| None=None

# class UserIn(BaseUser):
#     password:str


# @app.post("/users/", response_model=BaseUser)
# async def create_user(user:UserIn):
#     return user



@app.post("/products/", response_model=Product)
async def create_products(product: Product) -> Any:
    return product


## If you want to disable response model
@app.post("/products/", response_model=None)
async def create_products(product: Product) -> Any:
    return product


