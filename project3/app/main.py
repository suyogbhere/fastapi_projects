from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message":"I am exited to learn fastapi !!!"}