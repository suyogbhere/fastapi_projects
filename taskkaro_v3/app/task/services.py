from sqlmodel import select, Session
from app.db.config import engine
from app.task.models import  *
from fastapi import HTTPException



def create_task(session: Session,new_task =Task) -> Taskout:
    task = Task(title=new_task.title, content=new_task.content)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
    

def get_all_task(session: Session) -> list[Taskout]:
    stmt = select(Task)
    tasks = session.exec(stmt)
    return tasks.all()
    
    

def get_task_by_id(session: Session, task_id: int) -> Taskout:
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
    

def update_task(session:Session, task_id: int, new_task: Taskupdate) -> Taskout:
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # task.title = new_task.title
    # task.content = new_task.content
    task_data = new_task.model_dump()
    task.sqlmodel_update(task_data)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


    
def patch_task(session: Session, task_id: int, new_task: Taskpatch) -> Taskout:
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # if new_task.title is not None:
    #     task.title = new_task.title
    # if new_task.content is not None:
    #     task.content = new_task.content
    task_data = new_task.model_dump(exclude_unset=True)
    task.sqlmodel_update(task_data)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def delete_task(session: Session,task_id: int):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"ok": True}


