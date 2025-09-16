from fastapi import FastAPI, Query
from typing import Annotated


app = FastAPI()


PRODUCTS = [
    {"id":1, "title":"Hp backpack", "price":504.10,
     "description":"Perfect for everday use and forest walks"},

    {"id":2, "title":"laptop", "price":15000,
     "description":"For daily use and programming"},

     {"id":3, "title":"slim fit shirt", "price":700,
     "description":"Comfortable, slim-fitting casual shirt"},
]




# Basic Query Parameter
# @app.get("/products")
# async def get_product(search:str | None= None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product['title'].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS




# Validation without Annotated
# @app.get("/products")
# async def get_product(search:str | None= Query(default=None, max_length=5)):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product['title'].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS





# Validation with Annotated
# @app.get("/products")
# async def get_product(search: Annotated[ str | None , Query(max_length=5)]=None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product['title'].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS




# Required Parameter
# @app.get("/products/")
# async def get_product(search: Annotated[ str , Query(min_length=3)]):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product['title'].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS



## Add Regular expressions
@app.get("/products/")
async def get_product(search: Annotated[ str | None, Query(min_length=3, pattern="^[a-z]+$")]=None):
    if search:
        search_lower = search.lower()
        filtered_products = []
        for product in PRODUCTS:
            if search_lower in product['title'].lower():
                filtered_products.append(product)
        return filtered_products
    return PRODUCTS
