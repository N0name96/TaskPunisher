from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Annotated


from Database.Connection import get_db
from Models.task_Model import Tasks as TasksModel
from Schemas.task_schemas import TaskCreate, TaskUpdate, TaskBase as TaskSchema



router = APIRouter(
    prefix="/task",
    tags=["task"]
)



SessionDB = Annotated[Session, Depends(get_db)] #Instance the db in a variable



@router.post('/create_task/')
async def create_task(task: TaskCreate, db: SessionDB):
    """Function that creates a new task"""

    db_task = TasksModel(**task.model_dump()) # map schema to model
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {"Ok": True}



@router.get('/read_tasks/', response_model=List[TaskSchema])
async def get_tasks(db: SessionDB):
    """Function that reads all tasks"""

    result = db.execute(select(TasksModel)).scalars().all()
    return result



@router.get('/read_task_by_id/{task_id}', response_model=TaskSchema)
async def get_task_by_id(task_id: int, db: SessionDB):
    """Function that reads a single task"""

    result = db.get(TasksModel, task_id)

    if not result:
        raise HTTPException(status_code=404, detail='Task not found')

    return result



@router.put('/update_task/{task_id}/{updated_task}')
async def update_task(task_id: int, taskupdate: TaskUpdate, db: SessionDB):
    """Function that updates a single task"""

    task = db.get(TasksModel, task_id)

    if not task:
        raise HTTPException(status_code=404, detail='Task not found')

    # Update only sended attributes
    updated_task = taskupdate.model_dump(exclude_unset=True) #transform the object to a dictionary

    for key, value in updated_task.items():
        setattr(task, key, value)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task



@router.put('/update_tasks_false/')
async def update_tasks_false(db: SessionDB):
    """Function that updates a list of tasks false"""

    db.query(TasksModel).update({TasksModel.isCompleted: False})
    db.commit()

    return {"Ok": True}



@router.delete('/delete_task/{task_id}')
async def delete_task(task_id: int, db: SessionDB):
    """Function that deletes a single task"""

    task = db.get(TasksModel, task_id)

    if not task:
        raise HTTPException(status_code=404, detail='Task not found')

    db.delete(task)
    db.commit()
    return {"Ok": True}