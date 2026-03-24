from fastapi import APIRouter, HTTPException, Depends, Header
from typing import Annotated


async def verfiy_token(x_token: Annotated[str,Header()]):
    if x_token != "my-secret-token":
        raise HTTPException(status_code=400, detail="X-Token Header Invalid")


# router = APIRouter(dependencies=[Depends(verfiy_token)])
router = APIRouter()


@router.get("/items")
async def read_items():
    return {"data": "All items"}
