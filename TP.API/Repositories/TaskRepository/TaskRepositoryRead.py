from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from Models.TaskModel import TaskModel


class TaskRepositoryRead:
    @staticmethod
    async def read_all_task(db: AsyncSession):
        """Funcion que obtiene todos los task de la bbdd"""

        result = await db.execute(select(TaskModel))

        return result.scalars().all()


    @staticmethod
    async def read_task_by_id(db: AsyncSession, task_id: int):
        """Funcion que obtiene un task de la bbdd"""

        ressult = await db.get(TaskModel, task_id)

        if not ressult:
            return False

        return ressult