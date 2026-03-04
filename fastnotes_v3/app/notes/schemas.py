from pydantic import BaseModel, ConfigDict


#shared base fields
class NoteBase(BaseModel):
    title : str
    content : str


# for creation
class NoteCreate(NoteBase):
    pass


# For full update (PUT)
class NoteUpdate(NoteBase):
    pass


# for partial update (PATCH)
class NotePatch(BaseModel):
    title: str | None = None
    content: str | None = None


# For responce serialization
class NoteOut(NoteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    # class Config:
    #     orm_mode = True

