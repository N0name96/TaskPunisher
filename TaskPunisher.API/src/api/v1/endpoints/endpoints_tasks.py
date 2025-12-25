from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.v1.schemas.response import StandardResponse
from src.application.dtos.task import TaskBaseDTO, TaskCreateDTO
from src.application.queries.task import GetAllTasksHandler, GetTaskByIdHandler
from src.application.commands.task import CreateTaskHandler
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
    """Endpoiint que obtiene todas las tareas"""
    
    try:
        # Hacemos la inyeccion de dependencias de la BD en el repository
        repository = SQLAlchemyTaskRepository(db)

        # Hacemos que el handler de la query reciba el repositorio (inyeccion de dependencia)
        handler = GetAllTasksHandler(repository)

        # Realizamos el ejecute y recuperamos los resultados
        result: List[TaskBaseDTO] = await handler.execute()

        # Devolvemos el objeto generico
        return StandardResponse(status=200, message="Lista de tareas", data=result)
    except Exception as err:
        return StandardResponse(status=500, message=f"Error a la hora de obtener la lista de tareas, {err}", data=None)
    


@router.get(
    path="/get_task_by_id",
    response_model=StandardResponse[TaskBaseDTO]
)
async def get_task_by_id(task_id: int, db: AsyncSession = sessionDb) -> StandardResponse:
    """Endpoint que obtiene una tarea filtrada por id"""
    
    try:
        repository = SQLAlchemyTaskRepository(db)

        handler = GetTaskByIdHandler(repository)

        result: TaskBaseDTO = await handler.execute(task_id)

        if not result:
            return StandardResponse(
                status=404,
                message="La tarea solictada no existe",
                data=None
            )
        else:
            return StandardResponse(
                status=200,
                message="Tarea encontrada",
                data=result
            )
    except Exception as err:
        return StandardResponse(
            status=500,
            message=f"Error a la hora de obtener una tarea por id, Error: {err}",
            data=None
        )
    

@router.post(
    path="/create_task",
    response_model=StandardResponse
)
async def create_task(new_task: TaskCreateDTO, db: AsyncSession = sessionDb) -> StandardResponse:
    """Endopint que crea una nueva tarea"""

    try:
        respository = SQLAlchemyTaskRepository(db)

        handler = CreateTaskHandler(respository)

        result = await handler.execute(new_task)

        if result == 0:
            raise Exception("Error a la hora de realizar la creación de la tarea")
        else:
            return StandardResponse(
                status=200,
                message="Tarea creada correctamente",
                data=None
            )
    except Exception as err:
        return StandardResponse(
            status=500,
            message=f"Error a la hora de crear la tarea",
            data=None
        )