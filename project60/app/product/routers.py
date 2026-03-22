from fastapi import APIRouter

router = APIRouter(prefix="/products")



@router.get("/")
async def get_all_products():
    return {"data": "all products"}


@router.get("/{user_id}")
async def get_single_product(user_id: int):
    return {"data": "Single Product"}



