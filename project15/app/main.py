from fastapi import FastAPI, Cookie
from typing import Annotated


app = FastAPI()


##  Cookie Parameter
@app.get("/products/recommendations")
async def get_recomandations(session_id: Annotated[str | None, Cookie()] = None):
    if session_id :
        return {"message": f"recommendations for session {session_id}", "session_id":session_id}
    return {"message": "No Seesion ID Provided, Showing default recommendation"}

# To check its working or not
# curl -H "Cookie: session_id=abc123" http://127.0.0.1:8000/products/recommendations






### Using Pydantic model
from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, Field


# app = FastAPI()


class ProductCookie(BaseModel):
    session_id: str
    preferred_category : str | None = None
    tracking_id : str | None = None
     


@app.get("/products/recommendations")
async def get_recommendations(cookies: Annotated[ProductCookie, Cookie]):
    response = {"session_id": cookies.session_id}
    if cookies.preferred_category: 
        response["message"] = f"Recommendations for {cookies.preferred_category} products"
    else:
        response["message"] = f"Default recommendations for session {cookies.session_id}"
    if cookies.tracking_id:
        response["message"] = cookies.tracking_id
    return response


# curl -H "Cookie: session_id=abc123; preferred_category=Electronics; tracking_id=xyz786" http://127.0.0.1:8000/products/recommendations



# Without Pydantic model

# @app.get("/products/recommendations")
# async def get_recommendations(
#     session_id: str = Cookie(...),  # Required
#     preferred_category: str | None = Cookie(default=None),
#     tracking_id: str | None = Cookie(default=None)
# ):
#     response = {"session_id": session_id}
#     if preferred_category:
#         response["message"] = f"Recommendations for {preferred_category} products"
#     else:
#         response["message"] = f"Default recommendations for session {session_id}"
#     if tracking_id:
#         response["tracking_id"] = tracking_id
#     return response