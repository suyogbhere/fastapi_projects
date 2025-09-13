from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message":"Hello i am exited to learn the python Fastapi!!"}
