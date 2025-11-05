from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Annotated

from Database.Connection import get_db
from Models.task_Model import Tasks as TasksModel
from Schemas.task_schemas import TaskCreate, TaskUpdate, TaskBase as TaskSchema
from Schemas.response_model import ResponseModel

router = APIRouter(
    prefix="/task",
    tags=["task"]
)

SessionDB = Annotated[Session, Depends(get_db)]  #Instance the db in a variable


@router.post('/create_task/', response_model=ResponseModel)
async def create_task(task: TaskCreate, db: SessionDB):
    """Function that creates a new task"""

    try:
        db_task = TasksModel(**task.model_dump())  # map schema to model
        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        response = ResponseModel(
            status_code=200,
            message="Task created successfully",
            response=None
        )
    except Exception:
        response = ResponseModel(
            status_code=400,
            message="An error occured while creating task",
            response=None
        )
    return response


@router.get('/read_tasks/', response_model=ResponseModel)
async def get_tasks(db: SessionDB):
    """Function that reads all tasks"""

    try:
        result = db.execute(select(TasksModel)).scalars().all()

        response = ResponseModel(
            status_code=200,
            message="",
            response=result
        )
    except Exception:
        response = ResponseModel(
            status_code=400,
            message="An error occured while fetching tasks",
            response=None
        )

    return response


@router.get('/read_task_by_id/{task_id}', response_model=ResponseModel)
async def get_task_by_id(task_id: int, db: SessionDB):
    """Function that reads a single task"""

    response: ResponseModel

    try:
        result = db.get(TasksModel, task_id)

        if not result:
            raise HTTPException(status_code=404, detail='Task not found')

        response = ResponseModel(
            status_code=200,
            message="",
            response=result
        )
    except HTTPException as ht:
        response = ResponseModel(
            status_code = ht.status_code,
            message = ht.detail,
            response = None
        )
    except Exception:
        response = ResponseModel(
            status_code=400,
            message="An error ocurred while fetching this task",
            response=None
        )
    return response



@router.put('/update_task/{task_id}/{updated_task}', response_model=ResponseModel)
async def update_task(task_id: int, taskupdate: TaskUpdate, db: SessionDB):
    """Function that updates a single task"""

    try:
        task = db.get(TasksModel, task_id)

        if not task:
            raise HTTPException(status_code=404, detail='Task not found')

        # Update only sended attributes
        updated_task = taskupdate.model_dump(exclude_unset=True)  # transform the object to a dictionary

        for key, value in updated_task.items():
            setattr(task, key, value)

        db.add(task)
        db.commit()
        db.refresh(task)

        response = ResponseModel(
            status_code=200,
            message="Task updated successfully",
            response=None
        )
    except HTTPException as ht:
        response = ResponseModel(
            status_code=ht.status_code,
            message=ht.detail,
            response = None
        )
    except Exception:
        response = ResponseModel(
            status_code=400,
            message="An error occured while updating task",
            response = None
        )
    return response


@router.put('/update_tasks_false/', response_model=ResponseModel)
async def update_tasks_false(db: SessionDB):
    """Function that updates a list of tasks false"""

    try:
        db.query(TasksModel).update({TasksModel.isCompleted: False})
        db.commit()

        response = ResponseModel(
            status_code=200,
            message="Tasks updated false successfully",
            response=None
        )
    except Exception:
        response = ResponseModel(
            status_code=400,
            message="An error occured while updating tasks false",
            response = None
        )
    return response


@router.delete('/delete_task/{task_id}', response_model=ResponseModel)
async def delete_task(task_id: int, db: SessionDB):
    """Function that deletes a single task"""

    try:
        task = db.get(TasksModel, task_id)

        if not task:
            raise HTTPException(status_code=404, detail='Task not found')

        db.delete(task)
        db.commit()

        response = ResponseModel(
            status_code=200,
            message="Task deleted successfully",
            response=None
        )
    except Exception:
        response = ResponseModel(
            status_code=400,
            message="An error occured while deleting task",
            response = None
        )
    return response
