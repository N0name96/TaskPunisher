import random

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated, List, Any

from Database.Connection import get_db
from Schemas.punishment_schemas import PunishmentBase, PunishmentCreate, PunishmentUpdate
from Models.punishment_model import Punishments as PunishmentsModel
from Schemas.response_model import ResponseModel


router = APIRouter(
    prefix="/punishment",
    tags=["punishment"]
)


SessionDB = Annotated[Session, Depends(get_db)]

#todo -> create a get random punishment


@router.post('/create_punishment/{punisment}', response_model=ResponseModel[Any])
async def create_punishment(newpunishment: PunishmentCreate, db: SessionDB):
    """Function to create new punishment"""

    try:
        punishment = PunishmentsModel(**newpunishment.model_dump())
        db.add(punishment)
        db.commit()
        db.refresh(punishment)

        return ResponseModel(
            status_code=200,
            message="Punishment created successfully",
            response=None
        )
    except Exception:
        return ResponseModel(
            status_code=400,
            message="Punishment creation failed",
            response=None
        )


@router.get('/read_punishments/', response_model=ResponseModel[List[PunishmentBase]])
async def get_punishments(db: SessionDB):
    """Function to get all punishments"""

    try:
        punishments = db.query(PunishmentsModel).all()
        return ResponseModel(
            status_code=200,
            message="All punishments found",
            response=punishments
        )
    except Exception:
        return ResponseModel(
            status_code=400,
            message="Punishment read failed",
            response=None
        )


@router.get('/read_punishment_by_id/{punishment_id}', response_model=ResponseModel[PunishmentBase])
async def get_punishment_by_id(punishment_id: int, db: SessionDB):
    """Function to get punishment by id"""

    try:
        punishment = db.get(PunishmentsModel, punishment_id)

        if not punishment:
            raise HTTPException(status_code=404, detail="Punishment not found")

        return ResponseModel(
            status_code=200,
            message="Punishment found successfully",
            response=punishment
        )
    except HTTPException as err:
        return ResponseModel(
            status_code=err.status_code,
            message=err.detail,
            response=None
        )
    except Exception:
        return ResponseModel(
            status_code=400,
            message="Punishment read failed",
            response=None
        )


@router.get('/get_random_punishment/', response_model=ResponseModel[PunishmentBase])
async def get_random_punishment(db: SessionDB):
    """Function to get random punishment"""

    try:
        punishment_list = db.query(PunishmentsModel).all()

        response = random.choice(punishment_list)

        return ResponseModel(
            status_code=200,
            message="Random punishment found",
            response=response
        )
    except Exception:
        return ResponseModel(
            status_code=400,
            message="Random Punishment failed",
            response=None
        )


@router.put('/update_punishment/{punishment_id}/{updated_punishment}', response_model=ResponseModel[Any])
async def update_punishment(punishment_id: int, punishment_update: PunishmentUpdate, db: SessionDB):
    """Function to update punishment by id"""

    try:
        punishment = db.get(PunishmentsModel, punishment_id)

        if not punishment:
            raise HTTPException(status_code=404, detail="Punishment not found")

        dict_punishment = punishment_update.model_dump(exclude_unset=True)

        for key, value in dict_punishment.items():
            setattr(punishment, key, value)

        db.add(punishment)
        db.commit()
        db.refresh(punishment)

        return ResponseModel(
            status_code=200,
            message="Punishment updated successfully",
            response=punishment
        )
    except HTTPException as err:
        return ResponseModel(
            status_code=err.status_code,
            message=err.detail,
            response=None
        )
    except Exception:
        return ResponseModel(
            status_code=400,
            message="Punishment update failed",
            response=None
        )


@router.put('/update_punishments_false/', response_model=ResponseModel[Any])
async def update_punishments_false(db: SessionDB):
    """Function to update punishments false"""

    try:
        db.query(PunishmentsModel).update({PunishmentsModel.isCompleted: False})
        db.commit()

        return ResponseModel(
            status_code=200,
            message="Punishments updated successfully",
            response=None
        )
    except Exception:
        return ResponseModel(
            status_code=400,
            message="Punishments update failed",
            response=None
        )


@router.delete('/delete_punishment/{punishment_id}', response_model=ResponseModel[Any])
async def delete_punishment(punishment_id: int, db: SessionDB):
    """Function to delete punishment by id"""

    try:
        punishment = db.get(PunishmentsModel, punishment_id)

        if not punishment:
            raise HTTPException(status_code=404, detail="Punishment not found")

        db.delete(punishment)
        db.commit()

        return ResponseModel(
            status_code=200,
            message="Punishment deleted successfully",
            response=punishment
        )
    except HTTPException as err:
        return ResponseModel(
            status_code=err.status_code,
            message=err.detail,
            response=None
        )
    except Exception:
        return ResponseModel(
            status_code=400,
            message="Punishment delete failed",
            response=None
        )