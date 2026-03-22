from fastapi import FastAPI, Depends
from typing import Annotated

app  = FastAPI()


## Creating Dependancy Function
async def common_parameters(q: str | None=None, skip: int=0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}



## Using dependancy in endpoint
# @app.get("/items")
# async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons


# @app.get("/users")
# async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons


# -----------------------------------------------------------------------------------------------

# 2nd Method

## Create Type Alias
CommansDep = Annotated[dict, Depends(common_parameters)]


## Using dependancy in endpoint
@app.get("/products")
async def read_products(commons: CommansDep):
    return commons
