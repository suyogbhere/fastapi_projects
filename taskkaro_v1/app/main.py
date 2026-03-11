from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_tables
from app.task.services import *



@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)



@app.get("/tasks")
def all_tasks():
    tasks = get_all_task()
    return tasks


@app.get("/task/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)
    return task



@app.put("/task/{task_id}")
def put_task(task_id: int, new_task: dict):
    task = update_task(task_id, title=new_task["title"], content=new_task["content"])
    return task



@app.patch("/task/{task_id}")
def patch_task(task_id: int, new_task:dict):
    task = patch_task(task_id, title = new_task.get("title"), content=new_task.get("content"))
    return task


