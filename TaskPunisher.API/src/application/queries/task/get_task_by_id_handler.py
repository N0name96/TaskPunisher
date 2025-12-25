from typing import List

from src.domain.repositories.task.task_repository import TaskRepository
from src.application.dtos.task import TaskBaseDTO


class GetTaskByIdHandler:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    
    async def execute(self, task_id: int) -> TaskBaseDTO:
        """
        Handler que obtiene un task filtrado por id
        """

        return await self.repository.get_task_by_id(task_id)