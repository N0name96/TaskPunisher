from fastapi import APIRouter, Depends
from typing import Annotated

from Schemas.ResponseSchema import ResponseSchemaBase as ResponseBase
from Schemas.TaskSchema import TaskSchemaBase
from database.engine import get_async_session, AsyncSession
from Services.TaskService import TaskService as Service


task_router = APIRouter(
    prefix="/task",
    tags=["Task"]
)


sessiondb = Annotated[AsyncSession, Depends(get_async_session)]


@task_router.get(path="/read_task/", response_model=ResponseBase[list[TaskSchemaBase]])
async def read_all_task(db: sessiondb):
    """Endponit que obtiene todas las tareas"""

    try:
        lista_tareas = await Service.read_all_task(db)

        if not lista_tareas:
            return ResponseBase(status=200, message="No tareas existente", response=None)

        return ResponseBase(status=200, message="Tareas existentes", response=lista_tareas)

    except Exception as err:
        return ResponseBase(
            status=500,
            message=f"Error en obtener las tareas. Descripcion del error:{str(err)}",
            response=None
        )

#Todo -> Terminar de crear los demas endpoints