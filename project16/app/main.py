# from fastapi import FastAPI,Header
# from typing import Annotated


# app = FastAPI()


## Header Parameter
## Commanly use for Meta data or authorizations token
# @app.get("/products")
# async def get_products(user_agent: Annotated[str|None, Header()]=None):
#     return user_agent

# curl -H "User-Agent: Chrome" http://127.0.0.1:8000/products


# ------------------------------------------------------------------------------------------


## Handling Duplicate Headers
# @app.get("/products")
# async def get_product(x_product_token: Annotated[list[str]| None, Header()]= None):
#     return {
#         "x_product_token": x_product_token or []
#     }

# curl -H "X-Product-Token: token1" -H "X-Product-Token: token2" http://127.0.0.1:8000/products 


# ------------------------------------------------------------------------------------------


from fastapi import FastAPI , Header, Body
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

## Headers with a Pydantic Model
# class ProductHeaders(BaseModel):
#     authorization: str
#     accept_langauage: str | None = None
#     x_tracking_id  : list[str] = []


# @app.get("/products") 
# async def get_products(headers: Annotated[ProductHeaders, Header()]):
#     return {
#         "headers": headers
#     }

# curl -H "Authorization: Bearer token123" -H "Accept-Language:en-US" -H "X-Tracking-ID: track1" -H "X-Tracking-Id: track2" http://127.0.0.1:8000/products


# -------------------------------------------------------------------------------------------------------------------------------

##Forbidding Extra Headers
# class ProductHeaders(BaseModel):
#     model_config = {"extra":"forbid"}
#     authorization: str
#     accept_langauage: str | None = None
#     x_tracking_id  : list[str] = []


# @app.get("/products") 
# async def get_products(headers: Annotated[ProductHeaders, Header()]):
#     return {
#         "headers": headers
#     }


# curl -H "Authorization: Bearer token123" -H "Accept-Language:en-US" -H "X-Tracking-ID: track1" -H "X-Tracking-Id: track2" -H "extra-header:h123" http://127.0.0.1:8000/products


# -------------------------------------------------------------------------------------------------------------------------------





