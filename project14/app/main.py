from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated


app = FastAPI()

## Pydantic's Field ( Directly if you  want to add validation ) 
# class Product(BaseModel):
#     name : str =  Field(
#         title="Product Name",
#         description="The Name of the product",
#         max_length=100,
#         min_length=3,
#         pattern= "^[A-Za-z0-9]+$"
#     )
#     price : float = Field(
#         ge=0,
#         title = "Product Price",
#         description="The price of the product in USD, must be greter than zero"
#     )
#     stock : int |None = Field(
#         default= None,
#         ge=0,
#         title="Stock Quantity",
#         description= "The Number of items in stock, must be non-negative"        
#     )


# @app.post("/product")
# async def create_product(product: Product):
#     return product



## ===========================Nested Pydantic Model  ========================

##Nested Body Model
#Submodel
# class Category(BaseModel):
#     name: str = Field(
#         max_length=50,
#         min_length=1
#     )
#     description: str| None =Field(
#         default=None,
#         title="Category description",
#         description="A brief description of category",
#         max_length=200
#     )


# #Model witch will use submodel
# class Product(BaseModel):
#     name : str =  Field(
#         title="Product Name",
#         description="The Name of the product",
#         max_length=100,
#         min_length=3,
#     )
#     price : float = Field(
#         ge=0,
#         title = "Product Price",
#         description="The price of the product in USD, must be greter than zero"
#     )
#     stock : int |None = Field(
#         default= None,
#         ge=0,
#         title="Stock Quantity",
#         description= "The Number of items in stock, must be non-negative"        
#     )
#     category: Category| None= Field(
#         default= None,
#         title="Product Category",
#         description="The category to which the product belongs"
#     )



# @app.post("/product")
# async def create_product(product: Product):
#     return product

#===========================================+ =+=========================================


## Attribute with lists of submodels
class Category(BaseModel):
    name: str = Field(
        max_length=50,
        min_length=1
    )
    description: str| None =Field(
        default=None,
        title="Category description",
        description="A brief description of category",
        max_length=200
    )

#Model witch will use submodel
class Product(BaseModel):
    name : str =  Field(
        title="Product Name",
        description="The Name of the product",
        max_length=100,
        min_length=3,
    )
    price : float = Field(
        ge=0,
        title = "Product Price",
        description="The price of the product in USD, must be greter than zero"
    )
    stock : int |None = Field(
        default= None,
        ge=0,
        title="Stock Quantity",
        description= "The Number of items in stock, must be non-negative"        
    )
    category: list[Category] | None =Field(
        default= None,
        title = "Product Category",
        description=" The Category to which the product belongs"
    )



@app.post("/product")
async def create_product(product: Product):
    return product
