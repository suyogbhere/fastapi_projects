from fastapi import FastAPI,status

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
@app.get("/product", status_code=status.HTTP_200_OK)
async def all_product():
    return PRODUCTS


##GET Request
## Read or fetch single data
@app.get("/product/{product_id}", status_code=status.HTTP_200_OK)
async def single_product(product_id:int):
    for product in PRODUCTS:
        if product['id'] == product_id:
            return product 
        

#POST request
## Create or insert the data
@app.post("/product/create",  status_code=status.HTTP_201_CREATED)
async def create_product(new_product: dict):
    PRODUCTS.append(new_product)
    return {"status":"Created","new_proudct":new_product}



#PUT request
## update complete Data
@app.put("/product/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(product_id : int, new_updated_product: dict):
    for index, product in enumerate(PRODUCTS):
        if product['id'] == product_id:
            PRODUCTS[index] = new_updated_product
            return {"status":"Updated", "product_id" : product_id, "new_updated_product": new_updated_product}
        



#PATCH request
## update partial Data
@app.put("/product/{product_id}", status_code=status.HTTP_200_OK)
async def partial_product(product_id : int, new_updated_product: dict):
    for index, product in enumerate(PRODUCTS):
        if product['id'] == product_id:
            product.update(new_updated_product)
            return {"status":"Partial Updated", "product_id" : product_id, "new_updated_product": new_updated_product}
        


#DELETE Request
## Delete data
@app.delete("/product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS.pop(index)
            # return {"response":"Data Deleted..", "product_id": product_id}