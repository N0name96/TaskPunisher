from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Annotated


from Database.Connection import get_db
from Models.task_Model import Tasks as TasksModel
from Schemas.task_schemas import TaskCreate, TaskUpdate, Task as TaskSchema


router = APIRouter()

SessionDB = Annotated[Session, Depends(get_db)]

@router.get('/read_tasks/', response_model=List[TaskSchema])
async def read_tasks(db: SessionDB):
    '''Function that reads all tasks'''

    result = db.execute(select(TasksModel)).scalars().all()
    print(result)
    return result
