from fastapi import FastAPI, HTTPException, Request 
from fastapi.responses import JSONResponse

app = FastAPI()

items = {"apple":"A juicy fruit", 
        "banana":"A yellow delight"}

## Using HTTPException        (Error Handlng &  exception Handling)
@app.get("/items/{itme_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="item not found")
    return items[item_id]



###Adding custom Header
# @app.get("/items/{itme_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="item not found", headers={"x-error-type": "items missing   "})
#     return items[item_id]



#====================Custom  Exception   =====================================

fruits = {"apple":"A juicy fruit", 
        "banana":"A yellow delight"}

class FruitException(Exception):
    def __init__(self, fruit_name:str):
        self.fruit_name = fruit_name


##Custom exception Handler
@app.exception_handler(FruitException)
async def fruit_exception_handler(request: Request, exc: FruitException):
    return JSONResponse(status_code=418,
                        content={"message": f"{exc.fruit_name} is not valid "})


@app.get("/fruits/{fruit_name}")
async def read_fruit(fruit_name: str):
    if fruit_name not in fruits:
        raise FruitException(fruit_name=fruit_name)
    return fruits[fruit_name]





###===================== Override default exception =========================================================

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse




fruits = {
    "apple": "A juicy fruit",
    "banana" : "A yellow delight"
}


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc: RequestValidationError):
#     return PlainTextResponse(str(exc), status_code=400)



@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return item_id



