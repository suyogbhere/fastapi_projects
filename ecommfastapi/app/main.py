from fastapi import FastAPI
from app.account.routers import router as account_router
from app.product.routers.category import router as category_router
from app.product.routers.product import router as product_router


app = FastAPI(title="Fastapi E-Commerce Backend")


@app.get("/")
def root():
    return {"message":"Welcome to the E-Commerce API"}

app.include_router(account_router, prefix="/api/account", tags=["Account"])

app.include_router(product_router, prefix="/api/products", tags=["Products"])

app.include_router(category_router, prefix="/api/product/category", tags=["Categories"])

