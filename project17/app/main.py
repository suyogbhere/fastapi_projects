from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()

class Product(BaseModel):
    id : int 
    name : str
    price: float
    stock: int| None = None


class ProductOut(BaseModel):
    name : str
    price: float


# without return Type   --> To make your application secure and strict
# @app.get("/products/")
# async def get_product():
#     # return {"status": "Ok"}
#     return [
#         {"status": "Ok"},
#         {"status": 200}
#     ]



# Return Type annotation
# @app.get("/products/")
# async def get_products() -> Product:
#     return {"id":1, "name":"Moto E", "price":20.55, "stock":5}


# @app.get("/products/")
# async def get_products() -> Product:
#     return {"id":1, "name":"Moto E", "price":20.45}


# @app.get("/products/")
# async def get_products() -> Product:
#     return {"id":1, "name":"Moto E", "price":200, "stock":5, "description":"This is moto E"}



# To convert to List
# @app.get("/products/")
# async def get_products() -> List[Product]:
#     return [
#         {"id":1, "name":"Moto E", "price":20.55, "stock":5},
#         {"id":2, "name":"Redmi 10", "price":25.55, "stock":10}
#     ]


## Create product with return type
# @app.post("/products/")
# async def create_product(product: Product) -> ProductOut:
#     return product




# Using Inheritance   which field you to display use -> and show specific fields
class BaseUser(BaseModel):
    username: str
    full_name: str| None=None

class UserIn(BaseUser):
    password:str


@app.post("/users/")
async def create_user(user:UserIn) -> BaseUser:
    return user

