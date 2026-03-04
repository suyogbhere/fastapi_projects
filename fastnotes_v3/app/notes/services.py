from app.db.config import async_session
from app.notes.models import Notes
from sqlalchemy import select
from fastapi import HTTPException
from app.notes.schemas import NoteBase, NoteCreate,NoteUpdate,NotePatch,  NoteOut
from typing import List
from app.db.config import SessionDep
from sqlalchemy.ext.asyncio import AsyncSession

# async def create_note(new_note: NoteCreate, session: AsyncSession)-> NoteOut:


## Create new data
async def create_note(session: AsyncSession, new_note: NoteCreate) -> NoteOut:
        note = Notes(title = new_note.title, content=new_note.content)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note
    

## Get single Data
async def get_note(session: AsyncSession,note_id:int) -> NoteOut:
        note = await session.get(Notes, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return note
    

## fetch all data
async def get_all_notes(session: AsyncSession,) -> List[NoteOut]:
        stmt = select(Notes)
        notes = await session.scalars(stmt)
        return notes.all()
    


## Complete Update
async def update_note(session: AsyncSession,note_id:int, new_note: NoteUpdate) -> NoteOut:
        note = await session.get(Notes, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        note.title = new_note.title
        note.content = new_note.content
        await session.commit()
        await session.refresh(note)
        return note
    

## Partial update
async def patch_note(session: AsyncSession,note_id:int, new_note: NotePatch) -> NoteOut:
        note = await session.get(Notes, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        if new_note.title is not None:
            note.title = new_note.title
        if new_note.content is not None:
            note.content = new_note.content
        await session.commit()
        await session.refresh(note)
        return note
    

## delete the data
async def delete_note(session: AsyncSession,note_id: int):
        note = await session.get(Notes, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note is not found")
        await session.delete(note)
        await session.commit()
        return {"message": 'Deleted'}
