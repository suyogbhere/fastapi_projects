from fastapi import APIRouter

router = APIRouter(prefix="/users")



@router.get("/", tags=["Users"])
async def get_all_users():
    return {"data": "All Users"}


@router.get("/me", tags=["Users"])
async def get_current_user():
    return {"data": "Current User"}


@router.get("/{user_id}", tags=["Custom"])
async def get_single_user(user_id: int):
    return {"data": "Single User"}




