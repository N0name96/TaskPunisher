from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Annotated


from Database.Connection import get_db
from Models.task_Model import Tasks as TasksModel
from Schemas.task_schemas import TaskCreate, TaskUpdate, Task as TaskSchema


router = APIRouter()

SessionDB = Annotated[Session, Depends(get_db)] #Instance the db in a variable


@router.post('/create_task/')
async def create_task(task: TaskCreate, db: SessionDB):
    """Function that creates a new task"""

    db_task = TasksModel(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {"Ok": True}



@router.get('/read_tasks/', response_model=List[TaskSchema])
async def read_tasks(db: SessionDB):
    """Function that reads all tasks"""

    result = db.execute(select(TasksModel)).scalars().all()
    return result



@router.get('/read_task/{task_id}', response_model=TaskSchema)
async def read_task(task_id: int, db: SessionDB):
    """Function that reads a single task"""

    result = db.get(TasksModel, task_id)

    if not result:
        raise HTTPException(status_code=404, detail='Task not found')

    return result



@router.delete('/delete_task/{task_id}')
async def delete_task(task_id: int, db: SessionDB):
    """Function that deletes a single task"""

    task = db.get(TasksModel, task_id)

    if not task:
        raise HTTPException(status_code=404, detail='Task not found')

    db.delete(task)
    db.commit()
    return {"Ok": True}



@router.put('/update_task/{task_id}/{updated_task}')
async def update_task(task_id: int, taskupdate: TaskUpdate, db: SessionDB):
    """Function that updates a single task"""

    task = db.get(TasksModel, task_id)

    if not task:
        raise HTTPException(status_code=404, detail='Task not found')

    # Update only sended attributes
    updated_task = taskupdate.model_dump(exclude_unset=True) # take and serialize the objet

    for key, value in updated_task.items():
        setattr(task, key, value)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task