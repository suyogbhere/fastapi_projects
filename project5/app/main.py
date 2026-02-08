from fastapi import FastAPI


app = FastAPI()


#Order Matters   ( Always keep Static function above of dynamic function)

@app.get("/product/led_display")
async def single_predefind_product():
    return {"response": "Single Data fetched"}

@app.get("/product/{product_title}")
async def single_product(product_title: str):
    return {"response": "Single Data fetched", "product title": product_title}



