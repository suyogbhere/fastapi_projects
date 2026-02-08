from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any, Optional

app = FastAPI()

## Excluding  Unset Default Values

product_db ={
    "1":{"id":"1", "name": "laptop","price":245.67, "stock":10, "is_active":True},
    "2":{"id":"2", "name": "Smartphone","price":299.67, "stock":15, "is_active":False},
}

class Product(BaseModel):
    id: str
    name: str
    price: float
    description: Optional[str] = None
    tax:float=15.0      # Default tax rate


## Excluding  Unset Default Values
# @app.get("/products/{product_id}", response_model = Product, response_model_exclude_unset=True)
# async def get_product(product_id:str):
#     return product_db.get(product_id, {})

    
## Including  specific Fields
# @app.get("/products/{product_id}", response_model = Product, response_model_include={"name","price"})
# async def get_product(product_id:str):
#     return product_db.get(product_id, {})


## Excluding  specific Fields
@app.get("/products/{product_id}", response_model = Product, response_model_exclude={"price"})
async def get_product(product_id:str):
    return product_db.get(product_id, {})