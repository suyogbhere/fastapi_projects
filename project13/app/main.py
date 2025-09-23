from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app  = FastAPI()



# Multiple Body Parameters
class Product(BaseModel):
    name : str
    price : int
    stock: int| None = None


class Seller(BaseModel):
    username : str
    full_name: str |None = None


# @app.post("/product")
# async def create_product(product: Product, seller:Seller):
#     return {"Product": product, "Seller": seller}



## Make Body Optional
# @app.post("/product")
# async def create_product(product: Product, seller: Seller|None=None):
#     return {"product": product, "Seller": seller}


##Singular values in body
# @app.post("/product")
# async def create_product(
#     product: Product,
#     seller:Seller,
#     sec_key:Annotated[str, Body()]
#     ):
#     return {"product": product, "Seller": seller, "Sec Keys": sec_key}


##Embed a single body parameter
## without embed
# @app.get("/products")
# async def create_product(product: Product):
#     return {"product": Product}


## witho embed
@app.get("/products")
async def create_product(product: Annotated[Product, Body(embed=True)]):
    return {"product": Product}





