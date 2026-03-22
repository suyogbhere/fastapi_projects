from fastapi import FastAPI, Request
from .middlewares import *

app  = FastAPI()


app.middleware("http")(users_only_middleware)
app.middleware("http")(product_only_middleware)
app.middleware("http")(my_middleware)



@app.get("/users")
async def get_users():
    print("Endpoint: Inside get_users endpoint")
    return {"data": "All Users Data"}


@app.get("/products")
async def get_products():
    print("Endpoint: Inside get products")
    return {"data": "Get all products"}

