from fastapi import FastAPI, Depends
from typing import Annotated


app = FastAPI()


class CommanQueryparams:
    def __init__(self, q: str|None= None, skip: int= 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit



## Using Dependancy in Endpoints
@app.get("/items")
async def read_items(commons: Annotated[CommanQueryparams, Depends(CommanQueryparams)]):
    return commons



@app.get("/users")
async def read_users(commons: Annotated[CommanQueryparams, Depends(CommanQueryparams)]):
    return commons



# ------------------------------------------------------------------------------------------------

##Create a type Alias
CommonsDep = Annotated[CommanQueryparams, Depends(CommanQueryparams)]


@app.get("/products", tags=["Type Alias"])
async def read_products(commons: CommonsDep):
    return commons


@app.get("/carts", tags=["Type Alias"])
async def read_carts(commons: CommonsDep):
    return commons

