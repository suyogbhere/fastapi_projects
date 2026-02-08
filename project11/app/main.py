from fastapi import FastAPI, Query,Path
from typing import Annotated
from pydantic import AfterValidator


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
# @app.get("/products/")
# async def get_product(search: Annotated[ str | None, Query(min_length=3, pattern="^[a-z]+$")]=None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product['title'].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS




## Multiple Search Terms( List )
# @app.get("/products/")
# async def get_product(search: Annotated[list[str]|None, Query()]=None):
#     if search:
#         filtered_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS



## Alias parameter
# @app.get("/products/")
# async def get_product(search: Annotated[list[str]|None, Query(alias="q")]=None):
#     if search:
#         filtered_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS




## Adding Metadata
# @app.get("/products/")
# async def get_product(search: Annotated[
#     list[str]|None,
#       Query(alias="q", title = "Search Products",
#             description="Search by product title")]
#       =None):
#     if search:
#         filtered_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS



##Deprecated Parameters
# @app.get("/products/")
# async def get_product(search: Annotated[
#     list[str]|None,
#       Query(deprecated=True)]
#       =None):
#     if search:
#         filtered_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS




## Custom Validation
# def check_valid_id(id:str):
#     if not id.startswith("prod-"):
#         raise ValueError("ID must starts with prod-")
#     return id



# @app.get("/products/")
# async def get_products(id:Annotated[str|None, AfterValidator(check_valid_id)]=None):
#     if id:
#         return {"id":id, "messasge":"Valid product ID"}
#     return {"message": "No ID provided"}






#Basic Path parameter
# @app.get("/product/{product_id}")
# async def get_product(product_id: int):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return {"error": "product not Found!!"}




#Numeric Validation
# @app.get("/product/{product_id}")
# async def get_product(product_id: Annotated[int, Path(ge=1, le=3)]):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return {"error": "product not Found!!"}




## Combining path and Query Parameter
@app.get("/products/{product_id}")
async def get_product(
    product_id: Annotated[int , Path(ge=0, le=100)],
    search : Annotated[str | None, Query(max_length=20)]=None
):
    for product in PRODUCTS:
        if product["id"] == product_id:
            if search and search.lower() not in product['title'].lower():
                return {"error": "Product does not match search term"}
            return product

    return {"error":"product Not Found"}