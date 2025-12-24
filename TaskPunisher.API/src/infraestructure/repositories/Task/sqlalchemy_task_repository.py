from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.repositories.task.task_repository import TaskRepository
from src.domain.entities.task.task_entity import Tasks


class SQLAlchemyTaskRepository(TaskRepository):
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all_tasks(self) -> list[Tasks]:
        """
        Funcion que obtiene todos los registro de la tabla de tasks
        :return:
        """

        result = await self.session.execute(select(Tasks))
        return list(result.scalars().all())


    async def get_task_by_id(self, task_id: int) -> Tasks:
        """
        Funcion para obtener una tarea filtrado por id
        """

        task = await self.session.get(Tasks, task_id)
        return task

    
    async def create_task(self):
        pass