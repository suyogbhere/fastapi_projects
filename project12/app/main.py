from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



## ===========     Without Pydantic   =========================== 
## Create or Insert Data
# @app.post("/product")
# async def create_product(new_product: dict):
#     return new_product




## ===========     With Pydantic   =========================== 
## Define the product model
class Product(BaseModel):
    id: int
    name : str
    price : float
    stock : int | None = None


# @app.post("/product")
# async def create_product(new_product: Product):
#     return new_product



## Access Attribute inside function
# @app.post("/product")
# async def create_product(new_product: Product):
#     print("ID:",new_product.id)
#     print("Name:",new_product.name)
#     print("Price:",new_product.price)
#     print("Stock:",new_product.stock)
#     return new_product



##Add New Calculated attribute
# @app.post("/product")
# async def create_product(new_product: Product):
#     print("New_product_User_enter:",new_product)
#     product_dict = new_product.model_dump()                               #(To convert the Pydantic data to dictionary)
#     print("After Converting to Dictionary:", product_dict)
#     price_with_tax = new_product.price + (new_product.price * 18/100)
#     print(price_with_tax)
#     product_dict.update({"price_with_tax":price_with_tax})
#     return product_dict



## Combining request Body with Path parameter
@app.put("/products/{product_id}")
async def update_product(product_id : int, new_updated_product: Product, discount: float|None = None):
    return {"product_id":product_id,
    "New_updated_product": new_updated_product, "Discount": discount}





