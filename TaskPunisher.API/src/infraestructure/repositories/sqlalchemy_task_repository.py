from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.domain.models import TaskModel
from src.infraestructure.persistence import TaskTable

class SqlAlchemyTaskRepository:
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def get_all_tasks(self) -> List[TaskModel]:
        """Funcion que obtiene todas las tareas de la bbdd"""

        result = await self.session.execute(select(TaskTable))

        db_task_list = result.scalars().all()

        return [TaskModel.model_validate(task) for task in db_task_list]


    async def get_task_by_id(self, task_id: int) -> Optional[TaskModel]:
        """Funcion que obtiene una tarea filtrada por id"""

        result = await self.session.get(TaskTable, task_id)

        return TaskModel.model_validate(result) if result else None