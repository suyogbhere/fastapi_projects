from fastapi import FastAPI

app = FastAPI()


PRODUCTS = [
    {
        "id":1,
        "title":"abcd",
        "price": 100.99,
        "description": "xyz"
    },
    {
        "id":2,
        "title":"xyz",
        "price": 50.99,
        "description": "lmn"
    },
    {
        "id":3,
        "title":"pqrs",
        "price": 60.59,
        "description": "abcds"
    }
]




##GET Request
## Read or fetch all data
@app.get("/product")
async def all_product():
    return PRODUCTS


##GET Request
## Read or fetch single data
@app.get("/product/{product_id}")
async def single_product(product_id:int):
    for product in PRODUCTS:
        if product['id'] == product_id:
            return product 
        

#POST request
## Create or insert the data
@app.post("/product/create")
async def create_product(new_product: dict):
    PRODUCTS.append(new_product)
    return {"status":"Created","new_proudct":new_product}


