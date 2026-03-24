from fastapi import FastAPI, Depends
from app.routers import router, verfiy_token


app =  FastAPI()


#Depenndacy for Group of path Operations
# app.include_router(router)


app.include_router(router, dependencies=[Depends(verfiy_token)])


