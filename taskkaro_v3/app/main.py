from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_tables, SessionDep
from app.task.services import *
from app.task.models import *



@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/task", response_model=Taskout)
def task_create(session: SessionDep ,new_task: TaskCreate):
    task = create_task(session,new_task)
    return task




@app.get("/tasks", response_model=list[Taskout])
def all_tasks(session: SessionDep ):
    tasks = get_all_task(session)
    return tasks


@app.get("/task/{task_id}", response_model=Taskout)
def get_task(session: SessionDep ,task_id: int):
    task = get_task_by_id(session,task_id)
    return task



@app.put("/task/{task_id}", response_model=Taskout)
def put_task(session: SessionDep ,task_id: int, new_task: Taskupdate):
    task = update_task(session,task_id, new_task)
    return task



@app.patch("/task/{task_id}", response_model=Taskout)
def task_patch(session: SessionDep ,task_id: int, new_task:Taskpatch):
    task = patch_task(session,task_id, new_task)
    return task



@app.delete("/task/{task_id}")
def task_delete(session: SessionDep ,task_id: int):
    task = delete_task(session,task_id)
    return task


