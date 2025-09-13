from fastapi import FastAPI
from enum import Enum

app = FastAPI()


## Predefined Values
class ProductCategory(str, Enum):
    books= "books"
    clothing = "clothing"
    electronic = "electronic"


## Working with enum as a path parameter
# @app.get("/product/{category}")
# async def get_product(category:ProductCategory):
#     return {"response":"Products Fetched", "category":category}



##Working with Python enumerations
@app.get("/product/{category}")
async def get_product(category:ProductCategory):
    if category == ProductCategory.books:
        return {"category":category, "message":"Books are awesome!!"}
    elif category.value == 'clothing':
        return {'category':category, "message":"Fashion Trends!!"}
    elif category.value == 'electronic':
        return {'category':category, "message":"latest Gadgets available!!"}
    else:
        return {"category":category, "message":"Unknown Category!!"}





