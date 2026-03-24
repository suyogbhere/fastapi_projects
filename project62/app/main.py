from fastapi import FastAPI, Depends
from typing import Annotated


app  = FastAPI()


#Sync Dependancy 
def sync_dep():
    return {"message": "I am sync"}




# Async Dependancy
async def async_dep():
    return {"message": "I am Async"}


@app.get("/test/")
async def test(
    sync_result : Annotated[dict, Depends(sync_dep)],
    async_result : Annotated[dict, Depends(async_dep)]
    ):
    return {"sync": sync_result, "Async": async_result}



##---------------------------------------------------------------------------------


## Hirarchical Dependancy

async def user_auth():
    return {"user_id": "123"}


async def user_role(user: Annotated[dict, Depends(user_auth)]):
    return {"user_id": user["user_id"], "role":"admin"}


@app.get("/admin")
async def admin_only(role: Annotated[dict, Depends(user_role)]):
    return role


    