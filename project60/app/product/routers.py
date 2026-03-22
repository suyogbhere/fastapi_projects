from fastapi import APIRouter

router = APIRouter()



@router.get("/products")
async def get_all_products():
    return {"data": "all products"}


@router.get("/product/{user_id}")
async def get_single_product(user_id: int):
    return {"data": "Single Product"}



