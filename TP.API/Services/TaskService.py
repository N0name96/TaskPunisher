from sqlalchemy.ext.asyncio import AsyncSession

from Repositories.TaskRepository import TaskRepositoryRead as Repository


class TaskService:
    @staticmethod
    async def read_all_task(db: AsyncSession):
        """Servicio que obtiene la lista de todos los tasks"""

        return await Repository.read_all_task(db)


    @staticmethod
    async def read_task_by_id(db: AsyncSession, task_id: int):
        """Servicio que obtiene una task"""

        return await Repository.read_task_by_id(db, task_id)