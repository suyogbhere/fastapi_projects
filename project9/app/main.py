from fastapi import FastAPI

app = FastAPI()


#Single Query Parameter
# @app.get("/product")
# async def product(category:str):
#     return {"status":"Ok", "category":category}




#Multiple Query Parameter
# @app.get("/product")
# async def product(category:str, limit:int):
#     return {"status":"Ok", "category":category, "limit":limit}




#Default Query Parameter
# @app.get("/product")
# async def product(category:str, limit:int = 10):
#     return {"status":"Ok", "category":category, "limit":limit}


#optional Query Parameter
# @app.get("/product")
# async def product( limit:int, category:str |None = None):
    # return {"status":"Ok", "category":category, "limit":limit}



#path & Query Parameter
@app.get("/product/{year}")
async def product( year:str, category:str):
    return {"status":"Ok", "category":category, "Year":year}



