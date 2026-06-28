from fastapi import FastAPI
from app.account.routers import router as account_router


app = FastAPI(title="Fastapi E-Commerce Backend")


@app.get("/")
def root():
    return {"message":"Welcome to the E-Commerce API"}

app.include_router(account_router, prefix="/api/account", tags=["Account"])