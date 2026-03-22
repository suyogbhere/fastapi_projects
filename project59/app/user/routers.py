from fastapi import APIRouter

# router = APIRouter()


#2nd Tag method
# @router.get("/users", tags=["Users"])
# async def get_all_users():
#     return {"data": "All Users"}


# @router.get("/users/me", tags=["Users"])
# async def get_current_user():
#     return {"data": "Current User"}


# @router.get("/users/{user_id}", tags=["Custom"])
# async def get_single_user(user_id: int):
#     return {"data": "Single User"}





#3rd Tag method
router = APIRouter(tags=["users"])


@router.get("/users")
async def get_all_users():
    return {"data": "All Users"}


@router.get("/users/me")
async def get_current_user():
    return {"data": "Current User"}


@router.get("/users/{user_id}")
async def get_single_user(user_id: int):
    return {"data": "Single User"}




