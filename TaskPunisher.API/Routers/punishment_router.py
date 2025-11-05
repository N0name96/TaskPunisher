from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated, List

from Database.Connection import get_db
from Schemas.punishment_schemas import PunishmentBase, PunishmentCreate, PunishmentUpdate
from Models.punishment_model import Punishments as PunishmentsModel



router = APIRouter(
    prefix="/punishment",
    tags=["punishment"]
)



SessionDB = Annotated[Session, Depends(get_db)]



@router.post('/create_punishment/{punisment}')
async def create_punishment(newpunishment: PunishmentCreate, db: SessionDB):
    """Function to create new punishment"""

    punishment = PunishmentsModel(**newpunishment.model_dump())
    db.add(punishment)
    db.commit()
    db.refresh(punishment)

    return {"OK": True}



@router.get('/read_punishments/', response_model=List[PunishmentBase])
async def get_punishments(db: SessionDB):
    """Function to get all punishments"""

    list_punishment = db.query(PunishmentsModel).all()
    return list_punishment



@router.get('/read_punishment_by_id/{punishment_id}', response_model=PunishmentBase)
async def get_punishment_by_id(punishment_id: int, db: SessionDB):
    """Function to get punishment by id"""

    punishment = db.get(PunishmentsModel, punishment_id)

    if not punishment:
        raise HTTPException(status_code=404, detail="Punishment not found")

    return punishment


@router.put('/update_punishment/{punishment_id}/{updated_punishment}')
async def update_punishment(punishment_id: int, punishment_update: PunishmentUpdate, db: SessionDB):
    """Function to update punishment by id"""

    punishment = db.get(PunishmentsModel, punishment_id)

    if not punishment:
        raise HTTPException(status_code=404, detail="Punishment not found")

    dict_punishment = punishment_update.model_dump(exclude_unset=True)

    for key, value in dict_punishment.items():
        setattr(punishment, key, value)

    db.add(punishment)
    db.commit()
    db.refresh(punishment)

    return {"OK": True}



@router.put('/update_punishments_false/')
async def update_punishments_false(db: SessionDB):
    """Function to update punishments false"""

    db.query(PunishmentsModel).update({PunishmentsModel.isCompleted: False})
    db.commit()

    return {"OK": True}



@router.delete('/delete_punishment/{punishment_id}')
async def delete_punishment(punishment_id: int, db: SessionDB):
    """Function to delete punishment by id"""

    punishment = db.get(PunishmentsModel, punishment_id)

    if not punishment:
        raise HTTPException(status_code=404, detail="Punishment not found")

    db.delete(punishment)
    db.commit()

    return {"OK": True}