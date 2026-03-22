from fastapi import FastAPI
from app.user.routers import router as user_routers 
from app.product.routers import router as product_routers

app  = FastAPI()


## 1st Tag Method
# app.include_router(user_routers, tags=["Users"])
# app.include_router(product_routers, tags=["Products"])


app.include_router(user_routers)
app.include_router(product_routers)


# For Root
@app.get("/")
async def root():
    return {"data": "Root"}
 




