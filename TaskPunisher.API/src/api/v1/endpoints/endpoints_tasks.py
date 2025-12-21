from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.v1.schemas.response import StandardResponse
from src.application.dtos.task.TaskBaseDTO import TaskBaseDTO
from src.application.queries.task.get_all_tasks_handler import GetAllTasksHandler
from src.infraestructure.database.init_db import get_db
from src.infraestructure.repositories.Task.sqlalchemy_task_repository import SQLAlchemyTaskRepository


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


sessionDb = Annotated[AsyncSession, Depends(get_db)]


@router.get(
    path="/get_all_tasks",
    response_model=StandardResponse[List[TaskBaseDTO]]
)
async def get_all_tasks(db: AsyncSession = sessionDb) -> StandardResponse:
    try:
        # Hacemos la inyeccion de dependencias de la BD en el repository
        repository = SQLAlchemyTaskRepository(db)

        # Hacemos que el handler de la query reciba el repositorio (inyeccion de dependencia)
        handler = GetAllTasksHandler(repository)

        # Realizamos el ejecute y recuperamos los resultados
        result = await handler.execute()

        # Devolvemos el objeto generico
        return StandardResponse(status=200, message="Lista de tareas", data=result)
    except Exception as err:
        return StandardResponse(status=500, message=f"Error a la hora de obtener la lista de tareas, {err}", data=None)