from sqlmodel import Field, SQLModel



class TaskBase(SQLModel):
    title : str
    content : str


class TaskCreate(TaskBase):
    pass



class Taskupdate(TaskBase):
    pass



class Taskpatch(SQLModel):
    title : str | None = None
    content : str | None = None



class Taskout(TaskBase):
    id : int



class Task(TaskBase, table=True):
    id: int = Field(primary_key=True)




