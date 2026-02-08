# from fastapi import FastAPI, Cookie
# from typing import Annotated


# app = FastAPI()


##  Cookie Parameter
# @app.get("/products/recommendations")
# async def get_recomandations(session_id: Annotated[str | None, Cookie()] = None):
#     if session_id :
#         return {"message": f"recommendations for session {session_id}", "session_id":session_id}
#     return {"message": "No Seesion ID Provided, Showing default recommendation"}

# To check its working or not
# curl -H "Cookie: session_id=abc123" http://127.0.0.1:8000/products/recommendations






### Using Pydantic model
from fastapi import FastAPI, Cookie,Body
from typing import Annotated
from pydantic import BaseModel, Field


app = FastAPI()


# class ProductCookie(BaseModel):
#     session_id: str
#     preferred_category : str | None = None
#     tracking_id : str | None = None
     


# @app.get("/products/recommendations")
# async def get_recommendations(cookies: Annotated[ProductCookie, Cookie]):
#     response = {"session_id": cookies.session_id}
#     if cookies.preferred_category: 
#         response["message"] = f"Recommendations for {cookies.preferred_category} products"
#     else:
#         response["message"] = f"Default recommendations for session {cookies.session_id}"
#     if cookies.tracking_id:
#         response["message"] = cookies.tracking_id
#     return response


# curl -H "Cookie: session_id=abc123; preferred_category=Electronics; tracking_id=xyz786" http://127.0.0.1:8000/products/recommendations

# ===============================================================================================/

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

# =========================================================================================

# Forbidding Extra cookies 
# class ProductCookies(BaseModel):
#     model_config = {"extra": "forbid"}
#     session_id : str
#     preferred_category : str | None = None
#     tracking_id : str | None = None


# @app.get("/products/recommendations")
# async def get_recomendations(cookies: Annotated[ProductCookies, Cookie()]):
#     response = {"Session ID": cookies.session_id}
#     if cookies.preferred_category:
#         response["message"] = f"Recommendations for {cookies.preferred_category} products"
#     else:
#         response["message"] = f"default Recommendations for session {cookies.session_id}"
#     if cookies.tracking_id:
#         response["tracking_id"] = cookies.tracking_id
#     return response

# heat Below curl command on cmd
# curl -H "Cookie: session_id=abc123; preferred_category=Mobile" http://127.0.0.1:8000/products/recommendations
# curl -H "Cookie: session_id=abc123; extra-data=mydata; preferred_category=Mobile" http://127.0.0.1:8000/products/recommendations


# ============++++++++=======================+++++++++++++++++++++++++++++


## Combining with Body Parameters
class ProductCookies(BaseModel):
    model_config = {"extra": "forbid"}
    session_id : str = Field(title="Session ID", description="User Session Identifier")
    preferred_category : str | None = None


class PriceFilter(BaseModel):
    min_price : float = Field(ge=0, title="Minimum Price", description="Minimum price for recommendations")
    max_price : float | None = Field(default=None, title="maximum Price", description="Maximum price for recommendations")



@app.post("/products/recommendations")
async def get_recomendations(
        cookies: Annotated[ProductCookies, Cookie()],
        price_filter: Annotated[PriceFilter,Body(embed=True)]):
    response = {"Session ID": cookies.session_id}
    if cookies.preferred_category:
        response["message"] = cookies.preferred_category
    response["price_range"] = {
        "min_price": price_filter.min_price,
        "max_price": price_filter.max_price
    }
    response["message"] = f"Recommendations for session {cookies.session_id} with price range {price_filter.min_price} to {price_filter.max_price or 'unlimited'}"
    return response
     

# curl -H "Cookie: session_id=abc123; preferred_category=Mobile" -H "Content-Type:application/json" -d "{\"price_filter\":{\"price_filter\":{\"min_price\":50.0\"max_price\":1000.0}}" http://127.0.0.1:8000/products/recommendations